import cv2
from matplotlib import pyplot as plt
# read image
image= cv2.imread('image.png', 0) # 0 to read in grayscale
# Get histogram from 0 to 255
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE() #clipLimit=40.0, tileGridSize=(8,8)
claheimage = clahe.apply(image)
CLAHEhisteq = cv2.calcHist([claheimage], [0], None, [256], [0, 256])
cv2.imshow('Loaded image',image) # Plot original image
cv2.imshow('CLAHE image 8x8',claheimage) # Plot CLAHE image
# show the plotting graph of an image
plt.plot(hist)
plt.title('Loaded image histogram')
plt.show()
plt.plot(CLAHEhisteq)
plt.title('CLAHE histogram 8x8')
plt.show()
cv2.waitKey(0) # Close the windows