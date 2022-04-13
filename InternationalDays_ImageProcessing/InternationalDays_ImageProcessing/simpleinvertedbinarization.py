import cv2

image = cv2.imread('imgcolor.png',0) #Read image in grayscale
cv2.imshow('Loaded image',image) # Plot grayscale image
ret, thresh1 = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV) # Apply binarization with threshold of 120
cv2.imshow('Thresholded image: 150',thresh1) # Plot the binarized image
cv2.waitKey(0) # Close windows
cv2.destroyAllWindows()