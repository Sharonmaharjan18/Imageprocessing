import cv2
cap = cv2.VideoCapture('myrecordedvideo.avi')
while cap.isOpened(): # Check that the frame are correctly loaded
    ret, frame = cap.read() # read each frame
    if not ret: # if a frame is defective, print a message
        print(f"problem with frame")
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) == ord('q'): # print a frame every 25 ms or quit with "q"
        break
cap.release()
cv2.destroyAllWindows()
