import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow('Webcam frame',cv2.WINDOW_AUTOSIZE)
while True:
    ret_val, frame = cap.read()
    frame = cv2.flip(frame, 1)
    grayspim, colorspim = cv2.pencilSketch(frame, sigma_s=100, sigma_r=0.05, shade_factor=0.05)
    cv2.imshow('Pencil-like image', colorspim)
    if cv2.waitKey(1) == 27:
        break  # esc to quit
cap.release()
cv2.destroyAllWindows()