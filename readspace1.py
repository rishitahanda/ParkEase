import cv2

# Load the image
img = cv2.imread('space1pic.png')  # Replace with your image path
if img is None:
    print("Failed to load image.")
    exit()

# Resize image if it's too large (optional)
scale_percent = 50  # Change this to fit your screen
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

# Create a copy to restore each frame
base_img = resized_img.copy()

# Mouse move callback function
def mouse_move(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        temp_img = base_img.copy()
        text = f"({x}, {y})"
        cv2.putText(temp_img, text, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 255, 255), 2)  # Yellow color (BGR), thickness 2
        cv2.imshow('Image', temp_img)

# Show image window
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('Image', mouse_move)

# Keep window open until key press
cv2.imshow('Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
