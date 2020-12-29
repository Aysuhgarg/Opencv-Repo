import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface.xml")
img=cv2.imread("lena.png")
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face= faceCascade.detectMultiScale(imggray,1.1,4)

for(x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,189,0),3)

cv2.imshow("result",img)

cv2.waitKey(0)