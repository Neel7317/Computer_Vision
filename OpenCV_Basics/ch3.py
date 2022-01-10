##Resizeing and cropping..
##Resizing images..
import cv2
img= cv2.imread('resources/zoo.jpg')
cv2.imshow("original image",img)
#cv2.waitKey(0)
print(img.shape)
resizedimg=cv2.resize(img,(500,200))
cv2.imshow('resized image',resizedimg)
print(resizedimg.shape)
cv2.waitKey(0)

#Cropping images..
croppedimg=img[0:200,0:200]#frist value for hight & second for width
cv2.imshow("cropped image",croppedimg)
cv2.waitKey(0)

#Note in opencv when we dealing with images there width came first and then hight came and then no of channel..