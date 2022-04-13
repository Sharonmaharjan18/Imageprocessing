import cv2

image = cv2.imread('imgcolor.png',0) #Read image in grayscale
cv2.imshow('Loaded image',image) # Plot grayscale image
ret, thresh1 = cv2.threshold(image, 150, 255, cv2.THRESH_TRUNC) # Apply binarization with threshold of 150
cv2.imshow('Thresholded image: 150',thresh1) # Plot the binarized image
cv2.waitKey(0) # Close windows
print(ret)
cv2.destroyAllWindows()
