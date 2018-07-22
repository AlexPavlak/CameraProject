import numpy as np 
import cv2

#Create a video capture object
cap = cv2.VideoCapture(0)
background = cv2.createBackgroundSubtractorMOG2()

while(True):

    #Retrieve input from the camera frame by frame
    ret, frame = cap.read()

    foreground = background.apply(frame)

    #Display the captured frames
    cv2.imshow('frame',frame)
    cv2.imshow('foreground', foreground)

    #Continue displaying until q is pressed to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Cleanup, release the capture and destroy created windows.
cap.release()
cv2.destroyAllWindows()
