import cv2

image = cv2.imread("image.png", cv2.IMREAD_COLOR)
gaussian9 = cv2.GaussianBlur(image, (9,9),cv2.BORDER_DEFAULT)
gaussian15 = cv2.GaussianBlur(image, (15,15),cv2.BORDER_DEFAULT)
cv2.imshow("Original Image", image)
cv2.imshow("Original Image blurred with 9x9 kernel size", gaussian9)
cv2.imshow("Original Image blurred with 15x15 kernel size", gaussian15)
cv2.waitKey(0)
cv2.destroyAllWindows()