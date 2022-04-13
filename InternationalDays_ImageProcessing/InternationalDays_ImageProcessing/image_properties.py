import cv2

image = cv2.imread('logo.png',1)

# Shape returns 3 values: height, width and number of channel in the image
h, w, c = image.shape
image_size = image.size
image_type = image.dtype

print(f'The image height is {h}, the image width is {w}, the color channel {c}')
print(f'The image size is {image_size} and image type {image_type}')
# Display image
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()