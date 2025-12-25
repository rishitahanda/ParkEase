# -------------------- Import Libraries --------------------
import cv2  # OpenCV library for image and video processing
import pandas as pd  # Pandas for handling structured data (like bounding box info)
import numpy as np  # NumPy for numerical operations and handling arrays
from ultralytics import YOLO  # YOLOv8 object detection model
import time  # Time library to introduce delays between frames

# -------------------- Load the YOLOv8 Pre-trained Model --------------------
model = YOLO('yolov8s.pt')  # Loads the small YOLOv8 model (pretrained weights)

# -------------------- Define Main Detection Function --------------------
def space1():
    # Helper function to get (x, y) coordinates on mouse movement in the video window
    def RGB(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            colorsBGR = [x, y]  # Record coordinates
            print(colorsBGR)  # Print to console (can help in annotating parking areas)

    # Create a named window and bind mouse callback for getting pixel locations
    cv2.namedWindow('RGB')
    cv2.setMouseCallback('RGB', RGB)

    # Load the video file (change filename as required)
    cap = cv2.VideoCapture('space1.mp4')

    # Load list of object class names from a text file
    my_file = open("space2list.txt", "r")  # File contains class names (like car, person, etc.)
    data = my_file.read()
    class_list = data.split("\n")  # Split each line as a class label

    # -------------------- Define Parking Spot Coordinates (12 Spots) --------------------
    # Each parking area is a polygon defined by 4 points (tuples of x, y)
    area1 = [(52, 364), (30, 417), (73, 412), (88, 369)]
    area2 = [(105, 353), (86, 428), (137, 427), (146, 358)]
    area3 = [(159, 354), (150, 427), (204, 425), (203, 353)]
    area4 = [(217, 352), (219, 422), (273, 418), (261, 347)]
    area5 = [(274, 345), (286, 417), (338, 415), (321, 345)]
    area6 = [(336, 343), (357, 410), (409, 408), (382, 340)]
    area7 = [(396, 338), (426, 404), (479, 399), (439, 334)]
    area8 = [(458, 333), (494, 397), (543, 390), (495, 330)]
    area9 = [(511, 327), (557, 388), (603, 383), (549, 324)]
    area10 = [(564, 323), (615, 381), (654, 372), (596, 315)]
    area11 = [(616, 316), (666, 369), (703, 363), (642, 312)]
    area12 = [(674, 311), (730, 360), (764, 355), (707, 308)]

    # -------------------- Frame-by-Frame Processing --------------------
    while True:
        ret, frame = cap.read()  # Read a frame from video
        if not ret:
            break  # Break loop if video ends

        time.sleep(1)  # Delay between frames for clearer observation (1 second)

        frame = cv2.resize(frame, (1020, 500))  # Resize frame for consistency

        # Run YOLOv8 object detection on the frame
        results = model.predict(frame)

        # Extract bounding boxes from results
        a = results[0].boxes.data
        px = pd.DataFrame(a).astype("float")  # Convert to DataFrame for easy iteration

        # Initialize empty lists for each parking spot
        list1, list2, list3, list4, list5, list6 = [], [], [], [], [], []
        list7, list8, list9, list10, list11, list12 = [], [], [], [], [], []

        # -------------------- Process Detected Objects --------------------
        for index, row in px.iterrows():
            x1, y1, x2, y2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])  # Bounding box corners
            d = int(row[5])  # Class ID
            c = class_list[d]  # Class name (e.g., 'car')

            if 'car' in c:  # Only consider detected cars
                cx = (x1 + x2) // 2  # Center X
                cy = (y1 + y2) // 2  # Center Y

                # Check which area the center point of car lies in using pointPolygonTest
                for i, area in enumerate([area1, area2, area3, area4, area5, area6,
                                          area7, area8, area9, area10, area11, area12], 1):
                    if cv2.pointPolygonTest(np.array(area, np.int32), (cx, cy), False) >= 0:
                        eval(f"list{i}").append(c)  # Append to corresponding area list
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw box
                        cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)  # Draw center
                        if i == 1:
                            cv2.putText(frame, str(c), (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

        # -------------------- Count and Display Free Spaces --------------------
        # Number of cars detected in each area
        counts = [len(eval(f"list{i}")) for i in range(1, 13)]
        total_occupied = sum(counts)
        free_spaces = 12 - total_occupied
        print(free_spaces)  # Print number of free spaces

        # -------------------- Draw Status of Each Parking Space --------------------
        for i, (area, count) in enumerate(zip(
            [area1, area2, area3, area4, area5, area6, area7, area8, area9, area10, area11, area12], counts), 1):
            
            color = (0, 0, 255) if count == 1 else (0, 255, 0)  # Red if occupied, Green if free
            text_color = (0, 0, 255) if count == 1 else (255, 255, 255)
            cv2.polylines(frame, [np.array(area, np.int32)], True, color, 2)
            
            # Coordinates for label text (manually adjusted to match visual layout)
            label_positions = {
                1: (50, 441), 2: (106, 440), 3: (175, 436), 4: (250, 436), 5: (315, 429),
                6: (386, 421), 7: (456, 414), 8: (527, 406), 9: (591, 398), 10: (649, 384),
                11: (697, 377), 12: (752, 371)
            }
            cv2.putText(frame, str(i), label_positions[i], cv2.FONT_HERSHEY_COMPLEX, 0.5, text_color, 1)

        # -------------------- Display Free Space Counter --------------------
        cv2.putText(frame, str(free_spaces), (23, 30), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)

        # -------------------- Show the Output Frame --------------------
        cv2.imshow("RGB", frame)  # Display result in window

        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    # -------------------- Release Resources --------------------
    cap.release()
    cv2.destroyAllWindows()