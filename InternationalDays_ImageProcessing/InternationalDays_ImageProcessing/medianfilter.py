import cv2

image = cv2.imread("image.png", cv2.IMREAD_COLOR)
med9 = cv2.medianBlur(image, 9)
med15 = cv2.medianBlur(image, 15)
cv2.imshow("Original Image", image)
cv2.imshow("Original Image blurred with 9 kernel size", med9)
cv2.imshow("Original Image blurred with 15 kernel size", med15)
cv2.waitKey(0)
cv2.destroyAllWindows()