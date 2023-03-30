import cv2
import numpy as np
import pickle
import cvzone
try:  
    with open('rectangle.pkl','rb') as f:
        posList=pickle.load(f)
except:
    posList=[(50,140)]
width=(153-50)
height=(184-140)
cap=cv2.VideoCapture('carPark.mp4')

while True:
    _,img1=cap.read()
    if cap.get(cv2.CAP_PROP_POS_FRAMES)==cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    cv2.namedWindow("CarParking")
    img1 = cv2.resize(img1,(img1.shape[1]-30,img1.shape[0]-30))
    img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img=cv2.GaussianBlur(img,(3,3),1)
    img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    img=cv2.medianBlur(img,5)
    kernel=np.zeros((3,3),np.uint8)
    img=cv2.dilate(img,kernel,iterations=1)
    cv2.rectangle(img,(50,140),(153,184),(255,0,0),2)
    x=50
    y=140
    available=0
    n=len(posList)
    for pos in posList:
        x,y=pos
        imgCrop=img[y:y+height,x:x+width]
        count=cv2.countNonZero(imgCrop)
        if count<400:
            color=(0,255,0)
            thickness=2
            available+=1
        else:
            color=(0,0,255)
            thickness=1
        cv2.rectangle(img1,pos,(pos[0]+width,pos[1]+height),color,thickness)
        cvzone.putTextRect(img1,str(count),(x,y+height-2),scale=1,offset=0,thickness=2,colorR=(0,0,255))
        cvzone.putTextRect(img1,str('Free %d/%d'%(available,n)),(340,65),scale=3,thickness=3,colorR=(255,0,0))
        # cv2.imshow(str(x+y),imgCrop)
    cv2.imshow("Image", img1)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
