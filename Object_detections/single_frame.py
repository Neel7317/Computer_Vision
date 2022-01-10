import cv2
import numpy as np
cnf_thras=0.4
nms_thras=0.4
classes_name=[]
#color=[(0,0,255),(0,0,255),(0,0,255),(0,255,0),(0,255,0)]
image_size = 480

with open("yolov4.txt","r") as f:
    classes_name=[cname.strip()for cname in f.readlines()]

colors = np.random.randint(0, 255, size=(len(classes_name), 3), dtype='uint8')

net=cv2.dnn.readNet("yolov4.weights","yolov4.cfg")

net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(image_size,image_size), scale=1/255)

img=cv2.imread("../dnn_model/dog.jpg")

def draw_bounding_box(classes,scores,boxes):
    
    for i in range(len(classes)):
            x,y,w,h=boxes[i]
            score=scores[i]
            score="{:.2f}".format(score)
            label=str(classes_name[classes[i]])
            color = [int(c) for c in colors[classes[i]]]
            color=tuple(color)
            cv2.rectangle(img, (x,y), (x+w,y+h), color, 2)

            cv2.putText(img, (label+str(score)), (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)


classes,scores,boxes=model.detect(img,cnf_thras,nms_thras)

draw_bounding_box(classes,scores,boxes)

cv2.imshow("img",img)
cv2.waitKey(0)


