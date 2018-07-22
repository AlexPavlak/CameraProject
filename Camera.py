import numpy as np 
import cv2

#Create a video capture object
cap = cv2.VideoCapture(0)

while(True):

    #Retrieve input from the camera frame by frame
    ret, frame = cap.read()

    #Display the captured frames
    cv2.imshow('frame',frame)

    #Continue displaying until q is pressed to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Cleanup, release the capture and destroy created windows.
cap.release()
cv2.destroyAllWindows()
