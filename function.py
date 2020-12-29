import cv2
import numpy as np
img=cv2.imread("anon-hack.png")
                                             #1 BGR to Gray
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image",img2)
cv2.waitKey(0)
                                            #2 GaussianBlur
imgblur=cv2.GaussianBlur(img2,(7,7),0)
cv2.imshow("Gaussian image",imgblur)

imgcanny=cv2.Canny(img2,100,100)
cv2.imshow("Canny image",imgcanny)

kernel=np.ones((5,5),np.unit8)
imgDialation=cv2.dilate(imgcanny,Kernel,iterations=100)
#where kernel=np.ones((5,5),np.unit 8)
cv2.imshow("Canny image",imgcanny)

imgEroded=cv2.crode(imgDialation,kernel,iterations=100)
cv2.imshow("Canny image",imgEroded)

cv2.waitKey(0)
