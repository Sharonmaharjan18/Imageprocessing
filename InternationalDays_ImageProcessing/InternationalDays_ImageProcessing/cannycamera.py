import cv2
cap = cv2.VideoCapture(0)
cv2.namedWindow('Webcam frame',cv2.WINDOW_AUTOSIZE)
while True:
    ret_val, frame = cap.read()
    frame = cv2.flip(frame, 1)
    grayim = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurim = cv2.GaussianBlur(grayim, (3, 3), cv2.BORDER_DEFAULT)
    lowerT = 50
    upperT = 150
    cannyim = cv2.Canny(blurim, lowerT, upperT)
    cv2.imshow('Webcam Canny', cannyim)
    if cv2.waitKey(1) == 27:
        break  # esc to quit
cap.release()
cv2.destroyAllWindows()