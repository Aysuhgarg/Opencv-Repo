import cv2
img=cv2.imread("anon-hack.png")
                                             #1 BGR to Gray
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image",img2)
cv2.waitKey(0)
                                            #2 GaussianBlur
imgblur=cv2.GaussianBlur(img2,(7,7),0)
cv2.imshow("Gaussian image",imgblur)
cv2.waitKey(0)
