import cv2
from matplotlib import pyplot as plt

image = cv2.imread('imgcolor.png')
color = ('Blue','Green','Red')
for i,col in enumerate(color):
    hist = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.title('Loaded image histogram')
plt.show()
cv2.imshow('Loaded image',image)
cv2.waitKey(0)