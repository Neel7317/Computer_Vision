import cv2
import numpy as np
img=cv2.imread("resources/zoo.jpg")

#convert into grayscale image..
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('image',imgray)
cv2.waitKey(0)
#convert into blur image..
imgblur=cv2.GaussianBlur(img,(7,7),1)
cv2.imshow('image',imgblur)
cv2.waitKey(0)
#convert into canny image..
imgcanny=cv2.Canny(img,300,300)
cv2.imshow('canny image',imgcanny)
cv2.waitKey(0)

#convert image dialation..(thik liness)
kernal=np.ones((5,5),np.uint8)
imgdialation=cv2.dilate(imgcanny,kernel=kernal,iterations=1)
cv2.imshow('dialation image',imgdialation)
cv2.waitKey(0)

#Erorde image..(thin liness)
imgerorded=cv2.erode(imgdialation,kernel=kernal,iterations=1)
cv2.imshow('Erorded image',imgerorded)
cv2.waitKey(0)







