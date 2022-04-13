import cv2
from matplotlib import pyplot as plt
image = cv2.imread('imgcolor.png')
color = ('Blue','Green','Red')
histb = cv2.calcHist([image],[0],None,[256],[0,256]) # extract hist of b
histg = cv2.calcHist([image],[1],None,[256],[0,256]) # extract hist of g
histr = cv2.calcHist([image],[2],None,[256],[0,256]) # extract hist of r
plt.subplot(3,1,1) # use subplot
plt.plot(histb,color = 'Blue')
plt.title('Blue histogram')
plt.subplot(3,1,2)
plt.plot(histg,color = 'Green')
plt.title('Green histogram')
plt.subplot(3,1,3)
plt.plot(histr,color = 'Red')
plt.title('Red histogram')
plt.suptitle('Loaded image histogram')
plt.show()
cv2.imshow('Loaded image',image)
cv2.waitKey(0)