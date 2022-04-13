import cv2

image = cv2.imread('cameraman.png')
grayim = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurim = cv2.GaussianBlur(grayim, (3,3), cv2.BORDER_DEFAULT)
lowerT = 75
upperT =150
cannyim = cv2.Canny(blurim, lowerT, upperT)
cv2.imshow(f'Canny() function', cannyim)
cv2.waitKey(0)
cv2.destroyAllWindows()