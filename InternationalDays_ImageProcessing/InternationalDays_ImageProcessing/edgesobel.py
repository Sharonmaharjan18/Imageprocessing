import cv2

image = cv2.imread('cameraman.png')
grayim = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sobelx = cv2.Sobel(grayim, cv2.CV_64F, 1, 0) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(grayim, cv2.CV_64F, 0, 1) # Sobel Edge Detection on the Y axis
sobelx = cv2.convertScaleAbs(sobelx) # Convert to unsigned integer
sobely = cv2.convertScaleAbs(sobely)
sobelxy = cv2.bitwise_or(sobelx, sobely) # Combined X and Y Sobel Edge Detection
sobelxy = cv2.convertScaleAbs(sobelxy)
cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()