# ----------- File Serialization -----------
import pickle
# Used to save and load Python objects (e.g., ML models, feature data) in binary format

# ----------- Image Processing -----------
from skimage.transform import resize
# Resizes images to a consistent shape for processing or ML models
import cv2
# OpenCV library for real-time image and video processing

# ----------- Scientific Computing -----------
import numpy as np
# Used for numerical operations and managing image data as arrays



EMPTY = True
NOT_EMPTY = False

MODEL = pickle.load(open("model.p", "rb"))


def empty_or_not(spot_bgr):

    flat_data = []

    img_resized = resize(spot_bgr, (15, 15, 3))
    flat_data.append(img_resized.flatten())
    flat_data = np.array(flat_data)

    y_output = MODEL.predict(flat_data)

    if y_output == 0:
        return EMPTY
    else:
        return NOT_EMPTY


def get_parking_spots_bboxes(connected_components):
    (totalLabels, label_ids, values, centroid) = connected_components

    slots = []
    coef = 1
    for i in range(1, totalLabels):

        # Now extract the coordinate points
        x1 = int(values[i, cv2.CC_STAT_LEFT] * coef)
        y1 = int(values[i, cv2.CC_STAT_TOP] * coef)
        w = int(values[i, cv2.CC_STAT_WIDTH] * coef)
        h = int(values[i, cv2.CC_STAT_HEIGHT] * coef)

        slots.append([x1, y1, w, h])

    return slots
