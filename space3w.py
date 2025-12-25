import cv2
import numpy as np
import streamlit as st
import time
from util import get_parking_spots_bboxes, empty_or_not


def calculate_difference(img1, img2):
    return np.abs(np.mean(img1) - np.mean(img2))


def main():
    st.title("Live Parking Spot Detection")

    # Load mask and initialize
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
    video_placeholder = st.empty()
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

        # Draw annotations
        for i, (x, y, w, h) in enumerate(parking_spots):
            color = (0, 255, 0) if spot_status[i] else (0, 0, 255)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

        available = sum(spot_status)
        total = len(spot_status)
        cv2.rectangle(frame, (80, 20), (550, 80), (0, 0, 0), -1)
        cv2.putText(frame, f'Available spots: {available} / {total}', (100, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_placeholder.image(rgb_frame, channels="RGB")

        time.sleep(0.001)  # Simulate real-time playback (50 FPS approx)
        frame_counter += 1

    cap.release()


if __name__ == "__main__":
    main()
