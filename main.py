import cv2
import numpy as np

img = cv2.imread('./images/box.jpg')



def empty(a):
    pass

cv2.namedWindow('Parameters')
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 150, 254, empty)
cv2.createTrackbar("Threshold2", "Parameters", 254, 254, empty)
#
while True:
    imgBlur = cv2.GaussianBlur(img, (3, 3), 1)
    imgContours = img.copy()

    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")

    imgCanny = cv2.Canny(imgBlur, threshold1, threshold2)

    kernel = np.ones((1, 1), np.uint8)

    imgDilated = cv2.dilate(imgCanny, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(imgDilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(imgContours, contours, -1, (255, 0, 255), 2)

    min_area = 5000  # Minimum area threshold
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

    # Create a blank image to draw the contours
    # Draw the filtered contours as a complete outline
    cv2.drawContours(imgContours, filtered_contours, -1, (0, 0, 0), 2)

    # Display the image with contours
    cv2.imshow("Image with Contours", imgContours)

    # for cnt in contours:
    #     area = cv2.contourArea(cnt)
    #     if area > 28000:
    #         cv2.drawContours(imgContours, cnt, -1, (0, 0, 0), 2)


    cv2.imshow("Image", imgContours)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# imgBlur = cv2.GaussianBlur(img, (3, 3), 1)

# imgContours = img.copy()

# imgCanny = cv2.Canny(imgBlur, 150, 254)

# kernel = np.ones((1, 1), np.uint8)

# imgDilated = cv2.dilate(imgCanny, kernel, iterations=1)

# contours, hierarchy = cv2.findContours(imgDilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawContours(imgContours, contours, -1, (255, 0, 255), 7)

# cv2.imshow("Image", imgContours)

cv2.waitKey(0)
cv2.destroyAllWindows()
