import cv2
import numpy as np

img = cv2.imread('./box.jpg')



def empty(a):
    pass

cv2.namedWindow('Parameters')
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 150, 254, empty)
cv2.createTrackbar("Threshold2", "Parameters", 254, 254, empty)
#
# while True:
#     imgBlur = cv2.GaussianBlur(img, (3, 3), 1)
#
#     threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
#     threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
imgBlur = cv2.GaussianBlur(img, (0, 0), 1)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
