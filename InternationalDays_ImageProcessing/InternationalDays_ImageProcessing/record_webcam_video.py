import cv2
# Capture video from webcam
cap = cv2.VideoCapture(0)
# frame counter
currentFrame = 0
# Get webcam width
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# Get webcam height
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# Set codec
codec = cv2.VideoWriter_fourcc(*"DIVX")
out = cv2.VideoWriter('myrecordedvideo.avi', codec, 24.0, (int(width), int(height)))
while cap.isOpened():
    ret_val, frame = cap.read()
    frame = cv2.flip(frame, 1)     # flip the video
    out.write(frame) # save the frame
    cv2.imshow('Live webcam', frame)
    if cv2.waitKey(1) == 27:
        break  # esc to quit and stop the video
    currentFrame += 1
cap.release() # release camera
out.release() # release video
cv2.destroyAllWindows()