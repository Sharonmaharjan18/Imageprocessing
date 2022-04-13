import cv2

# Read image using imread function
image = cv2.imread("color.png", cv2.IMREAD_COLOR)

B, G, R = cv2.split(image)

# Display original image
cv2.imshow("Original image", image)
cv2.waitKey(0)

cv2.imshow("Blue color plan", B)
cv2.waitKey(0)

cv2.imshow("Green color plan", G)
cv2.waitKey(0)

cv2.imshow("Red color plan", R)
cv2.waitKey(0)

cv2.destroyAllWindows()