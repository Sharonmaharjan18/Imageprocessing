import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow('Webcam frame',cv2.WINDOW_AUTOSIZE)
while True:
    ret_val, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retotsu, threshotsu = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Apply binarization with Otsu
    cv2.imshow('Otsu threshold', threshotsu)
    print(f'Otsu threshold: {retotsu}')
    if cv2.waitKey(1) == 27:
        break  # esc to quit
cap.release()
cv2.destroyAllWindows()