from ultralytics import YOLO
import cv2

# Load YOLOv8s model (auto-downloads if not available)
model = YOLO('yolov8s.pt')

# Load your parking lot image
image_path = 'overheadpark.jpg'  # Replace with your image path
image = cv2.imread(image_path)

# Run inference
results = model(image)

# Visualize results (bounding boxes, labels, confidence)
annotated_frame = results[0].plot()

# Display the result
cv2.imshow("YOLOv8 Parking Detection", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
