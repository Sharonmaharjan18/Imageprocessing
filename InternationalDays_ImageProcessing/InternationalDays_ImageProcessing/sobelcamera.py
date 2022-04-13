import cv2
cap = cv2.VideoCapture(0)
cv2.namedWindow('Webcam frame',cv2.WINDOW_AUTOSIZE)
while True:
    ret_val, frame = cap.read()
    frame = cv2.flip(frame, 1)
    grayim = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(grayim, cv2.CV_64F, 1, 0)  # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(grayim, cv2.CV_64F, 0, 1)  # Sobel Edge Detection on the Y axis
    sobelx = cv2.convertScaleAbs(sobelx)  # Convert to unsigned integer
    sobely = cv2.convertScaleAbs(sobely)
    sobelxy = cv2.bitwise_or(sobelx, sobely)  # Combined X and Y Sobel Edge Detection
    sobelxy = cv2.convertScaleAbs(sobelxy)
    cv2.imshow('Webcam Sobel', sobelxy)
    if cv2.waitKey(1) == 27:
        break  # esc to quit
cap.release()
cv2.destroyAllWindows()