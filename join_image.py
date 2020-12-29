import cv2
import numpy as np

img=cv2.imread("anon-hack.png")

imghor= np.hstack((img,img))
imgver= np.vstack((img,img))

cv2.imshow("horizontal",imghor)
cv2.imshow("vertical",imgver)

cv2.waitKey(0)
#Limitation--> This fails , if both images donot have same number of channels and size of image cant be resize
