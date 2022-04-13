import cv2
cap = cv2.VideoCapture(0)
cv2.namedWindow('Webcam frame',cv2.WINDOW_AUTOSIZE)
while True:
    ret_val, frame = cap.read()
    frame = cv2.flip(frame, 1)
    invertedimage = cv2.bitwise_not(frame)
    cv2.imshow('Inverted image', invertedimage)
    if cv2.waitKey(1) == 27:
        break  # esc to quit
cap.release()
cv2.destroyAllWindows()