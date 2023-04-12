import numpy as np
import cv2
import matplotlib.pyplot as plt
import colorsys
import time

#Program to display a color mix on the screen 

b=0.3
g=0.4
r=0.1


#alternatively, use the "Hue, Saturation, Value" system:
#colors (hue) are on a circle, starting with red at h=0 , and blue at 0.5, and back at red at h=1.0.

for h in np.arange(0,1,0.02): 
   r, g, b= colorsys.hsv_to_rgb(h, 1.0, 1.0)
   print("r, g, b=", r, g, b, "\t h=", h)

   #make frames of 300x300 pixels with 3 equal color components:
   frame=np.zeros((300,300,3))
   frame[:,:,0]=np.ones((300,300))*b
   frame[:,:,1]=np.ones((300,300))*g
   frame[:,:,2]=np.ones((300,300))*r

   frame=frame*1.0;

   # Display the resulting frame
   cv2.imshow('frame',frame)
  
   if cv2.waitKey(200) & 0xFF == ord('q'):
        break

# When everything done, close windows

cv2.destroyAllWindows()
