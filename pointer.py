import cv2
img= cv2.imread("space2pic.png")

# while True:
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()