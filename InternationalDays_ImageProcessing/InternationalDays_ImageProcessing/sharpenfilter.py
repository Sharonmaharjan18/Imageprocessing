import cv2
import numpy as np

image = cv2.imread('image.png')
# Create kernel
kernel45 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
kernel90 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# Apply  filter
filterimg45 = cv2.filter2D(image, -1, kernel45)
filterimg90 = cv2.filter2D(image, -1, kernel90)
cv2.imshow('Original', image)
cv2.imshow('Sharpened image 45', filterimg45)
cv2.imshow('Sharpened image 90', filterimg90)
cv2.waitKey(0)
cv2.destroyAllWindows()