import cv2

# Read image using imread function
image = cv2.imread("logo.png", cv2.IMREAD_COLOR)
#image_gray = cv2.imread("logo.png", cv2.IMREAD_GRAYSCALE)

# Display image using imshow('title', variable)
cv2.imshow("logo BU-TM", image)

# Need to use waitKey(0) to keep the image displayed on
# waitKey(time_in_millisecond) to keep it on for a specified time or 0 for the user to manually close it (pressing keyboard)
cv2.waitKey(0)

# clearing window and memory using (destralAllWindows)
cv2.destroyAllWindows()