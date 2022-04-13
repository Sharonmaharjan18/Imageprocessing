import cv2

# Read image using imread function
image = cv2.imread("color.png", cv2.IMREAD_COLOR)

B = image[:,:,0]
G = image[:,:,1]
R = image[:,:,2]

# Display original image
cv2.imshow("Original image", image)
cv2.imshow("Blue color plan", B)
cv2.imshow("Green color plan", G)
cv2.imshow("Red color plan", R)
cv2.waitKey(0)

cv2.destroyAllWindows()
