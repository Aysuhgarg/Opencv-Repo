import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)   # id->10 is for brightness
while True:
    success,img=cap.read()
    cv2.imshow("webcam",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break