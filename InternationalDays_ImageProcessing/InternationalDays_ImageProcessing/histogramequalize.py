import cv2
from matplotlib import pyplot as plt
image= cv2.imread('image.png', 0) # 0 to read in grayscale
# Get histogram from 0 to 255
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
histeqimage = cv2.equalizeHist(image) # apply histogram equalization
histeq = cv2.calcHist([histeqimage], [0], None, [256], [0, 256]) # Get the new histogram
cv2.imshow('Loaded image',image) # Display original image
cv2.imshow('Equalized histogram image',histeqimage) # Display equalized histogram image
# Plot each histogram
plt.plot(hist)
plt.title('Loaded image histogram')
plt.show()
plt.plot(histeq)
plt.title('Equalized histogram')
plt.show()
cv2.waitKey(0)