import cv2
from matplotlib import pyplot as plt

# read image
image= cv2.imread('imgcolor.png', 0) # 0 to read in grayscale

# Get histogram from 0 to 255
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
cv2.imshow('Loaded image',image)
# show the plotting graph of an image
plt.plot(hist)
plt.title('Loaded image histogram')
plt.show()
cv2.waitKey(0)