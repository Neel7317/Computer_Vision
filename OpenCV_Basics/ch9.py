#face detection using opencv
import cv2
cap=cv2.VideoCapture(0)
harr=cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")#load casecased classifier
while True:
    suc,img=cap.read()
    
    #img=cv2.imread("resources/download.jpg")#read image
    faces=harr.detectMultiScale(img,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)#draw rectangle on faces
    cv2.imshow("hot",img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break