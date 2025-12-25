# ----------- Image & Video Processing -----------
import cv2  # OpenCV library used for reading, writing, and processing image/video data

# ----------- Scientific Computing -----------
import numpy as np  # Used for numerical operations, matrix computations, and array handling

# ----------- Web App Framework -----------
import streamlit as st  # Streamlit library to build interactive and reactive web apps in Python

# ----------- Time Handling -----------
import time  # Used for delays, measuring elapsed time, or timestamps

# ----------- Project-Specific Utilities -----------
from util import get_parking_spots_bboxes, empty_or_not  
# Custom functions:
# - get_parking_spots_bboxes: extracts bounding boxes for each parking spot
# - empty_or_not: determines if a parking spot is occupied based on frame analysis


def calc_diff(im1, im2):
    return np.abs(np.mean(im1) - np.mean(im2))

def detect_small_object(spot_crop):
    gray = cv2.cvtColor(spot_crop, cv2.COLOR_BGR2GRAY)
    mean_intensity = np.mean(gray)
    std_intensity = np.std(gray)
    return mean_intensity < 180 and std_intensity > 20


def space2():
    st.title("Live Parking Spot Detection of Fun City")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("### 🚘 Welcome to Fun City")
        slot_status_placeholder = st.empty()

    with col2:
        video_placeholder = st.empty()

    mask_path = 'maskspace2.png'
    video_path = 'space2loop.mp4'
    mask = cv2.imread(mask_path, 0)

    cap = cv2.VideoCapture(video_path)

    components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
    spots = get_parking_spots_bboxes(components)

    spots_status = [None for _ in spots]
    diffs = [None for _ in spots]
    previous_frame = None
    step = 30
    frame_nmr = 0

    run_video = st.checkbox("Run Detection", value=True)

    while run_video:
        ret, frame = cap.read()
        if not ret:
            st.warning("End of video.")
            break

        if frame_nmr % step == 0 and previous_frame is not None:
            for i, spot in enumerate(spots):
                x1, y1, w, h = spot
                spot_crop = frame[y1:y1 + h, x1:x1 + w, :]
                diffs[i] = calc_diff(spot_crop, previous_frame[y1:y1 + h, x1:x1 + w, :])

        if frame_nmr % step == 0:
            if previous_frame is None:
                arr_ = range(len(spots))
            else:
                arr_ = [j for j in np.argsort(diffs) if diffs[j] / np.amax(diffs) > 0.4]

            for i in arr_:
                x1, y1, w, h = spots[i]
                spot_crop = frame[y1:y1 + h, x1:x1 + w, :]
                spot_status = empty_or_not(spot_crop)
                spots_status[i] = spot_status

        if frame_nmr % step == 0:
            previous_frame = frame.copy()

        for i, spot in enumerate(spots):
            x1, y1, w, h = spot
            spot_crop = frame[y1:y1 + h, x1:x1 + w, :]
            status = spots_status[i]

            small_car = False
            if status:
                small_car = detect_small_object(spot_crop)

            if status and not small_car:
                color = (0, 255, 0)
            elif small_car:
                color = (0, 165, 255)
                cv2.putText(frame, "Small Car", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 165, 255), 2)
            else:
                color = (0, 0, 255)

            cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), color, 2)

        available = sum([s for s in spots_status if s])
        total = len(spots_status)

        slot_status_placeholder.markdown(
            f"""
            ### 🟢 Available Spots: {available} / {total}
            - 🔴 Red: Occupied
            - 🟢 Green: Available
            - 🟠 Orange: Small Vehicle
            """
        )

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_placeholder.image(rgb_frame, channels="RGB")

        time.sleep(0.001)
        frame_nmr += 1

    cap.release()