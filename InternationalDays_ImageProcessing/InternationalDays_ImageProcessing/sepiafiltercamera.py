import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow('Webcam frame',cv2.WINDOW_AUTOSIZE)
while True:
    ret_val, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame64 = np.array(frame, dtype=np.float64) # convert the frame into 64 floating point
    sepiamatrix = np.matrix([[0.272, 0.534, 0.131],
                            [0.349, 0.686, 0.168],
                            [0.393, 0.769, 0.189]])
    framesepia = cv2.transform(frame64, sepiamatrix)  # applying sepia matrix to colorspaces
    framesepia[np.where(framesepia > 255)] = 255  # Limiting value to 255
    framesepia = np.array(framesepia, dtype=np.uint8) # Converting back to 8 bits unsigned integer
    cv2.imshow('Sepia image', framesepia)
    if cv2.waitKey(1) == 27:
        break  # esc to quit
cap.release()
cv2.destroyAllWindows()
