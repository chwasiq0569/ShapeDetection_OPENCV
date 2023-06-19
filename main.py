import cv2
import numpy as np

img = cv2.imread('./images/card333.jpg')



def empty(a):
    pass

cv2.namedWindow('Parameters')
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 150, 254, empty)
cv2.createTrackbar("Threshold2", "Parameters", 254, 254, empty)
#
while True:
    imgBlur = cv2.GaussianBlur(img, (3, 3), 1)

    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")

    imgCanny = cv2.Canny(imgBlur, threshold1, threshold2)
    print(imgCanny)
    cv2.imshow("Image", imgCanny)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
