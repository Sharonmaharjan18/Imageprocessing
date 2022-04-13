import cv2

image = cv2.imread("logo.png", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("logo BU-TM", image)
cv2.imshow("Gray converted logo BU-TM", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()