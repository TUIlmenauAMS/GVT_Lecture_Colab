import numpy as np
import cv2

#Program to capture a video from a camera and display Original and R,G,B, compinents live on the screen

cap = cv2.VideoCapture(0)

cap.set(3,1024) #sets horizontal resolutio to other value than 640
cap.set(4, 576) #sets vertical resolution

cv2.namedWindow('Original')
cv2.namedWindow('B Komponente')
cv2.namedWindow('G Komponente')
cv2.namedWindow('R Komponente')

ret=False
while(True):
    # Capture frame-by-frame
    [ret, frame] = cap.read()
    #print("ret=",ret)
    # Display the resulting frame
    cv2.imshow('Original',frame)
    cv2.imshow('B Komponente',frame[:,:,0])
    cv2.imshow('G Komponente',frame[:,:,1])
    cv2.imshow('R Komponente',frame[:,:,2])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
