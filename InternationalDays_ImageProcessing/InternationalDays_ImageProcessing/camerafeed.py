import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow('Webcam Life2Coding',cv2.WINDOW_AUTOSIZE)
while True:
    ret_val, frame = cap.read()
    print(f'{ret_val}')
    # flip the video
    frame = cv2.flip(frame, 1)
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) == 27:
        break  # esc to quit
cap.release()
cv2.destroyAllWindows()