#get purspective from image..
import cv2
import numpy as np

img=cv2.imread("resources/pen.jpg")
height=500
width=500

pts1=np.float32([[110,210],[287,120],[154,482],[352,440]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)
wrapedimg=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("pen image",wrapedimg)
cv2.waitKey(0)
print(img.shape)