#Learn draw shapes(circle,rectangle,lines,etc..) and write text on images


import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)#create image
img2=np.zeros((512,512,3),np.uint8)#create image
img[:]=0,255,0#fill color in entire image 
img2[0:100,100:200]=0,255,0#fill color in image at custom location
cv2.imshow("image",img)
cv2.imshow("image2",img2)
cv2.waitKey(0)

##draw shapes..
# 1 draw lines
img3=np.zeros((250,250,3),np.uint8)
cv2.line(img3,(0,100),(100,200),(0,255,0),thickness=3)
cv2.line(img3,(0,0),(img3.shape[1],img3.shape[0]),(255,0,0),thickness=2)
cv2.imshow("image3",img3)
cv2.waitKey(0)
#draw reactangle
cv2.rectangle(img3,(0,0),(100,100),(255,255,0),2)
#draw circle
cv2.circle(img3,(200,200),50,(255,255,0),cv2.FILLED)

#write text over image..
cv2.putText(img3,"OpenCV tutorial",(100,100),cv2.FONT_ITALIC,1,(0,0,255),1)
cv2.imshow("image3",img3)
cv2.waitKey(0)