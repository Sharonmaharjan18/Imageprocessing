import cv2

image = cv2.imread('imgcolor.png',0) #Read image in grayscale
cv2.imshow('Loaded image',image) # Plot grayscale image
retotsu, threshotsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) # Apply binarization with Otsu
cv2.imshow(f'Thresholded image: {retotsu}',threshotsu) # Plot the binarized image
print(f'Otsu threshold: {retotsu}')
cv2.waitKey(0) # Close windows
cv2.destroyAllWindows()