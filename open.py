import cv2
print("Package imported")
                                      #Reading image anan-hack.png
img =cv2.imread("anon-hack.png")
cv2.imshow("Image",img)
cv2.waitKey(0)
                                      #VideoCapturing
cap=cv2.VideoCapture()
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


