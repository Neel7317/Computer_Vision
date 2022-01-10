import cv2
#reading image...
img=cv2.imread('15.png')
cv2.imshow("output",img)
cv2.waitKey(0)

##reading videofile..
cap=cv2.VideoCapture("1.mp4")
while True:
    success,frame=cap.read()
    cv2.imshow("video",frame)
    if cv2.waitKey(30) & 0xFF==ord('q'):
        break
##reading webcame..
import cv2
cap=cv2.VideoCapture(0)

while True:
    success,frame=cap.read()
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break