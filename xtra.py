import cv2

# Load the image
img = cv2.imread('space1pic.png')  # Replace with your image path
if img is None:
    print("Failed to load image.")
    exit()
scale_percent = 50  # Change this to fit your screen
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

# Create a copy to restore each frame
base_img = resized_img.copy()
cv2.imshow('Image', base_img)
# Keep window open until key press
cv2.imshow('Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()