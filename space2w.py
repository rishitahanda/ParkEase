# # ==== LIBRARY IMPORTS ====

# # OpenCV for video processing, image reading, drawing rectangles
# import cv2

# # matplotlib (currently unused, can be used for plotting/debugging frames if needed)
# import matplotlib.pyplot as plt

# # numpy for numerical operations like array manipulation and calculations
# import numpy as np

# # Streamlit for web application interface (currently imported but not directly used here)
# import streamlit as st

# # PIL (Python Imaging Library) for image manipulation (currently not used directly here)
# from PIL import Image

# # Import helper functions from util.py:
# # - get_parking_spots_bboxes: to extract parking spots coordinates
# # - empty_or_not: predict if a parking spot is empty or not
# from util import get_parking_spots_bboxes, empty_or_not


# # ==== FUNCTION DEFINITIONS ====

# def calc_diff(im1, im2):
#     """
#     Calculate the absolute brightness difference between two frames.
#     This helps detect movement or change in a specific parking spot.
#     """
#     return np.abs(np.mean(im1) - np.mean(im2))

# def detect_small_object(spot_crop):
#     """
#     Detect if a small object (like a bike or small car) exists inside an empty spot
#     based on:
#     - Mean pixel intensity (brightness)
#     - Standard deviation (texture/variability inside the spot)
#     """
#     gray = cv2.cvtColor(spot_crop, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
#     mean_intensity = np.mean(gray)  # Average brightness value
#     std_intensity = np.std(gray)    # How much pixel values vary (flat ground = low std)

#     # If brightness is lower (darker) and texture is significant, assume small object
#     if mean_intensity < 180 and std_intensity > 20:
#         return True
#     else:
#         return False


# def space2():
#     """
#     Main function to read the parking lot video, process each frame,
#     detect available parking spots, detect small objects if needed,
#     and display the result with rectangles and labels.
#     """

#     # Load the parking spots mask (parking slot map)
#     mask = 'maskspace2.png'

#     # Load the video of the parking lot
#     video_path = 'space2loop.mp4'

#     # Read mask image in grayscale mode
#     mask = cv2.imread(mask, 0)

#     # Open video file
#     cap = cv2.VideoCapture(video_path)

#     # Identify connected parking spots from mask
#     connected_components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
#     spots = get_parking_spots_bboxes(connected_components)

#     # Initialize lists to keep track of each parking spot's status
#     spots_status = [None for _ in spots]
#     diffs = [None for _ in spots]

#     # Frame used for comparing changes
#     previous_frame = None

#     # Frame counter
#     frame_nmr = 0

#     # Status of video reading
#     ret = True

#     # How many frames to skip between processing
#     step = 30

#     while ret:
#         # Read a frame from the video
#         ret, frame = cap.read()

#         if not ret:
#             break

#         # Step 1: Calculate difference between current and previous frame
#         if frame_nmr % step == 0 and previous_frame is not None:
#             for spot_indx, spot in enumerate(spots):
#                 x1, y1, w, h = spot
#                 spot_crop = frame[y1:y1 + h, x1:x1 + w, :]  # Crop the spot from frame
#                 diffs[spot_indx] = calc_diff(spot_crop, previous_frame[y1:y1 + h, x1:x1 + w, :])

#         # Step 2: Check if any significant change happened in parking spots
#         if frame_nmr % step == 0:
#             if previous_frame is None:
#                 arr_ = range(len(spots))
#             else:
#                 arr_ = [j for j in np.argsort(diffs) if diffs[j] / np.amax(diffs) > 0.4]

#             for spot_indx in arr_:
#                 spot = spots[spot_indx]
#                 x1, y1, w, h = spot
#                 spot_crop = frame[y1:y1 + h, x1:x1 + w, :]
#                 spot_status = empty_or_not(spot_crop)  # Predict if spot is empty or occupied
#                 spots_status[spot_indx] = spot_status

#         # Update previous frame
#         if frame_nmr % step == 0:
#             previous_frame = frame.copy()

#         # Step 3: Drawing rectangles based on spot status
#         for spot_indx, spot in enumerate(spots):
#             spot_status = spots_status[spot_indx]
#             x1, y1, w, h = spot
#             spot_crop = frame[y1:y1 + h, x1:x1 + w, :]

#             small_car = False

#             # If the spot is considered empty, double check if any small object exists
#             if spot_status:
#                 small_car = detect_small_object(spot_crop)

#             # Draw rectangle with color based on the status
#             if spot_status and not small_car:
#                 # Truly empty spot → Green rectangle
#                 frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
#             elif small_car:
#                 # Small object detected → Orange rectangle + label
#                 frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 165, 255), 2)  # Orange
#                 cv2.putText(frame, "Small Car", (x1, y1 - 10),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 165, 255), 2)
#             else:
#                 # Properly occupied spot → Red rectangle
#                 frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 0, 255), 2)

#         # Step 4: Draw black box at the top to show availability counter
#         cv2.rectangle(frame, (80, 20), (550, 80), (0, 0, 0), -1)
#         cv2.putText(frame, 'Available spots: {} / {}'.format(str(sum(spots_status)), str(len(spots_status))), (100, 60),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

#         # Display frame
#         cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
#         cv2.imshow('frame', frame)

#         # Handle user keypress
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break

#         # Move to next frame
#         frame_nmr += 1

#     # Release video and close windows after finishing
#     cap.release()
#     cv2.destroyAllWindows()

# # ==== RUN PROGRAM ====
# # space2()


# ==== LIBRARY IMPORTS ====

# OpenCV: used for image and video processing tasks such as reading frames, drawing, and grayscale conversion
import cv2

# Matplotlib: currently unused, but useful for plotting or displaying images in notebooks for debugging
import matplotlib.pyplot as plt

# NumPy: essential for handling numerical operations, image matrices, mean and standard deviation calculations
import numpy as np

# Streamlit: used to build the web application interface (imported for future use, not actively used here)
import streamlit as st

# PIL (Python Imaging Library): for advanced image manipulation (currently not used in this code)
from PIL import Image

# Importing helper functions from util.py:
# - get_parking_spots_bboxes: to extract bounding boxes of parking spots from the mask image
# - empty_or_not: ML-based or heuristic function to determine if a parking spot is empty
from util import get_parking_spots_bboxes, empty_or_not


# ==== FUNCTION DEFINITIONS ====

def calc_diff(im1, im2):
    """
    Calculate the absolute difference in brightness between two cropped images (frames).
    This function is used to detect whether any significant change has occurred in a parking spot
    by comparing the mean brightness values of the current and previous frames.

    Parameters:
        im1 (ndarray): Cropped image of the spot from current frame.
        im2 (ndarray): Cropped image of the same spot from previous frame.

    Returns:
        float: Absolute difference in mean brightness.
    """
    return np.abs(np.mean(im1) - np.mean(im2))


def detect_small_object(spot_crop):
    """
    Detects if a small object (e.g., a bike, scooter, or compact car) exists in what appears to be an empty spot.
    It does so based on pixel intensity and standard deviation analysis.

    Parameters:
        spot_crop (ndarray): Cropped image of the parking spot.

    Returns:
        bool: True if a small object is detected, otherwise False.
    """
    gray = cv2.cvtColor(spot_crop, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    mean_intensity = np.mean(gray)                      # Brightness of the cropped spot
    std_intensity = np.std(gray)                        # Texture/variance measure

    # Heuristic: small objects tend to be darker with higher texture
    if mean_intensity < 180 and std_intensity > 20:
        return True
    else:
        return False


def space2():
    """
    This is the main function that:
    - Loads the mask and video.
    - Detects parking spot positions using connected components.
    - Processes the video frame-by-frame to identify parking status.
    - Uses frame differencing to reduce computation and detect changes.
    - Marks spots with colors: Green (empty), Red (occupied), Orange (small object).
    - Displays total available spots on screen overlay.
    """

    # Load the grayscale parking spot segmentation mask image
    mask = 'maskspace2.png'

    # Load the corresponding parking lot video
    video_path = 'space2loop.mp4'

    # Read mask in grayscale mode (single channel)
    mask = cv2.imread(mask, 0)

    # Load the video for processing
    cap = cv2.VideoCapture(video_path)

    # Extract parking spot bounding boxes from the mask image
    connected_components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
    spots = get_parking_spots_bboxes(connected_components)

    # Initialize the status list for all parking spots (True = Empty, False = Occupied)
    spots_status = [None for _ in spots]

    # List to store brightness differences for each spot
    diffs = [None for _ in spots]

    # Frame used to compare with current frame (to detect change)
    previous_frame = None

    # Frame number counter
    frame_nmr = 0

    # Flag for video capture loop
    ret = True

    # Frame skip rate to reduce processing frequency (process every 'step' frames)
    step = 30

    # ==== VIDEO FRAME PROCESSING LOOP ====
    while ret:
        # Read the next frame from the video
        ret, frame = cap.read()

        if not ret:
            break  # Exit loop if no frame is read

        # === Step 1: Calculate differences in frame to detect changes ===
        if frame_nmr % step == 0 and previous_frame is not None:
            for spot_indx, spot in enumerate(spots):
                x1, y1, w, h = spot
                spot_crop = frame[y1:y1 + h, x1:x1 + w, :]  # Crop the parking spot from current frame
                diffs[spot_indx] = calc_diff(spot_crop, previous_frame[y1:y1 + h, x1:x1 + w, :])  # Compare to previous frame

        # === Step 2: If significant change is detected, re-evaluate the parking status ===
        if frame_nmr % step == 0:
            if previous_frame is None:
                arr_ = range(len(spots))  # If no previous frame exists, process all spots
            else:
                # Only process spots with notable brightness difference (change threshold: 0.4 of max)
                arr_ = [j for j in np.argsort(diffs) if diffs[j] / np.amax(diffs) > 0.4]

            for spot_indx in arr_:
                x1, y1, w, h = spots[spot_indx]
                spot_crop = frame[y1:y1 + h, x1:x1 + w, :]
                spot_status = empty_or_not(spot_crop)  # Predict occupancy
                spots_status[spot_indx] = spot_status  # Save result

        # === Step 3: Update the previous frame for future comparison ===
        if frame_nmr % step == 0:
            previous_frame = frame.copy()

        # === Step 4: Draw rectangles and labels on the frame ===
        for spot_indx, spot in enumerate(spots):
            spot_status = spots_status[spot_indx]
            x1, y1, w, h = spot
            spot_crop = frame[y1:y1 + h, x1:x1 + w, :]

            small_car = False

            # If declared empty, run a second check for small objects
            if spot_status:
                small_car = detect_small_object(spot_crop)

            # Draw colored rectangle based on occupancy status
            if spot_status and not small_car:
                # Truly empty spot → Green
                frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
            elif small_car:
                # Small vehicle detected → Orange with label
                frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 165, 255), 2)
                cv2.putText(frame, "Small Car", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 165, 255), 2)
            else:
                # Fully occupied spot → Red
                frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 0, 255), 2)

        # === Step 5: Overlay availability status at the top ===
        cv2.rectangle(frame, (80, 20), (550, 80), (0, 0, 0), -1)  # Black background box
        cv2.putText(frame, 'Available spots: {} / {}'.format(str(sum(spots_status)), str(len(spots_status))),
                    (100, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Display the processed frame
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.imshow('frame', frame)

        # Exit if 'q' key is pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        # Move to next frame
        frame_nmr += 1

    # === CLEANUP: Release resources ===
    cap.release()
    cv2.destroyAllWindows()


# ==== RUN PROGRAM ====
# space2()  # Uncomment this to run the video processing directly
