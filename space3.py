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


def calculate_difference(img1, img2):
    return np.abs(np.mean(img1) - np.mean(img2))
def main():
    st.title("Live Parking Spot Detection of City Center")

    # Set up two columns for layout
    col1, col2 = st.columns([1, 2])

    # Welcome and slot info will appear in left column
    with col1:
        st.markdown("### 🚗 Welcome to City Center")
        slot_status_placeholder = st.empty()

    # Right column will show video
    with col2:
        video_placeholder = st.empty()

    mask_path = 'maskspace3.png'
    video_path = 'space3speed.mp4'
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
    parking_spots = get_parking_spots_bboxes(components)

    cap = cv2.VideoCapture(video_path)

    spot_status = [None] * len(parking_spots)
    frame_diffs = [None] * len(parking_spots)
    previous_frame = None

    step = 1
    frame_counter = 0
    run_video = st.checkbox("Run Detection", value=True)

    while run_video:
        ret, frame = cap.read()
        if not ret:
            st.warning("End of video.")
            break

        if frame_counter % step == 0 and previous_frame is not None:
            for i, (x, y, w, h) in enumerate(parking_spots):
                crop_current = frame[y:y + h, x:x + w]
                crop_previous = previous_frame[y:y + h, x:x + w]
                frame_diffs[i] = calculate_difference(crop_current, crop_previous)

        if frame_counter % step == 0:
            if previous_frame is None:
                indices = range(len(parking_spots))
            else:
                max_diff = np.max(frame_diffs)
                indices = [i for i in np.argsort(frame_diffs) if frame_diffs[i] / max_diff > 0.4]

            for i in indices:
                x, y, w, h = parking_spots[i]
                crop_img = frame[y:y + h, x:x + w]
                spot_status[i] = empty_or_not(crop_img)

            previous_frame = frame.copy()

        # Draw rectangles on the frame
        for i, (x, y, w, h) in enumerate(parking_spots):
            color = (0, 255, 0) if spot_status[i] else (0, 0, 255)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

        available = sum(spot_status)
        total = len(spot_status)

        # Display info in left column
        slot_status_placeholder.markdown(
            f"""
            ### 🟢 Available Spots: {available} / {total}
            - 🔴 Red: Occupied
            - 🟢 Green: Available
            """
        )

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_placeholder.image(rgb_frame, channels="RGB")

        time.sleep(0.001)
        frame_counter += 1

    cap.release()