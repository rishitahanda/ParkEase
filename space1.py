# ----------- Image & Video Processing -----------
import cv2  # OpenCV library used for image and video capture, manipulation, and processing

# ----------- Data Manipulation & Scientific Computing -----------
import pandas as pd  # Used for working with tabular data (DataFrames)
import numpy as np  # Used for numerical computations and handling arrays

# ----------- Web App Framework -----------
import streamlit as st  # Streamlit library to build interactive web apps in Python

# ----------- Time Handling -----------
import time  # Used for timing operations such as delays and performance measurement

# ----------- Deep Learning / Object Detection -----------
from ultralytics import YOLO  
# Ultralytics YOLO - used for object detection in video/image frames

# -------------------- Load the YOLOv8 Pre-trained Model --------------------
model = YOLO('yolov8s.pt') 
# Loads the small YOLOv8 model (pretrained weights)

# -------------------- Define Main Detection Function --------------------
def space1():
    st.title("Live Parking Spot Detection of Ambience Mall")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("### 🚗 Welcome to Ambience Mall")
        slot_status_placeholder = st.empty()
    with col2:
        video_placeholder = st.empty()

    model = YOLO('yolov8s.pt')
    cap = cv2.VideoCapture('space1.mp4')

    with open("space2list.txt", "r") as f:
        class_list = f.read().split("\n")

    # Parking spots (12)
    areas = [
        [(52, 364), (30, 417), (73, 412), (88, 369)],
        [(105, 353), (86, 428), (137, 427), (146, 358)],
        [(159, 354), (150, 427), (204, 425), (203, 353)],
        [(217, 352), (219, 422), (273, 418), (261, 347)],
        [(274, 345), (286, 417), (338, 415), (321, 345)],
        [(336, 343), (357, 410), (409, 408), (382, 340)],
        [(396, 338), (426, 404), (479, 399), (439, 334)],
        [(458, 333), (494, 397), (543, 390), (495, 330)],
        [(511, 327), (557, 388), (603, 383), (549, 324)],
        [(564, 323), (615, 381), (654, 372), (596, 315)],
        [(616, 316), (666, 369), (703, 363), (642, 312)],
        [(674, 311), (730, 360), (764, 355), (707, 308)],
    ]

    run_video = st.checkbox("Run Detection", value=True)

    while run_video:
        ret, frame = cap.read()
        if not ret:
            st.warning("End of video.")
            break

        time.sleep(0.5)  # You can reduce this if too slow
        frame = cv2.resize(frame, (1020, 500))

        results = model.predict(frame)
        px = pd.DataFrame(results[0].boxes.data).astype("float")

        occupied = set()
        for _, row in px.iterrows():
            x1, y1, x2, y2, _, cls_id = map(int, row[:6])
            label = class_list[cls_id]
            if 'car' not in label:
                continue
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            for idx, area in enumerate(areas):
                if cv2.pointPolygonTest(np.array(area, np.int32), (cx, cy), False) >= 0:
                    occupied.add(idx)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)

        free_spaces = 12 - len(occupied)
        slot_status_placeholder.markdown(
            f"""
            ### 🅿️ Free Spaces: {free_spaces} / 12
            - 🟥 Red: Occupied  
            - 🟩 Green: Available  
            """
        )

        # Draw areas
        for i, area in enumerate(areas):
            color = (0, 0, 255) if i in occupied else (0, 255, 0)
            text_color = (255, 255, 255) if i not in occupied else (0, 0, 255)
            cv2.polylines(frame, [np.array(area, np.int32)], True, color, 2)
            x, y = area[0]
            cv2.putText(frame, str(i + 1), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, text_color, 2)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_placeholder.image(rgb_frame, channels="RGB")

    cap.release()