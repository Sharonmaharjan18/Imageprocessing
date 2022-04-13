import cv2

image = cv2.imread("image.png", cv2.IMREAD_COLOR)
blurim9 = cv2.blur(image, (9,9))
blurim15 = cv2.blur(image, (15,15))
cv2.imshow("Original Image", image)
cv2.imshow("Original Image blurred with 9x9 kernel", blurim9)
cv2.imshow("Original Image blurred with 15x15 kernel", blurim15)
cv2.waitKey(0)
cv2.destroyAllWindows()