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
def mouseClick(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if event == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1=pos
            if x1+width>x>x1 and y1+height>y>y1:
                
                posList.pop(i)


while True:
    cv2.namedWindow("CarParking")
    img = cv2.imread('carParkImg.png')
    img = cv2.resize(img,(img.shape[1]-30,img.shape[0]-30))
    cv2.setMouseCallback('CarParking',mouseClick)
    for pos in posList:
        x,y=pos
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,0),2)
    
    with open('rectangle.pkl','wb') as f:
        pickle.dump(posList,f)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
