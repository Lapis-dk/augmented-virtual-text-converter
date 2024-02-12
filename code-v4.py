import cv2
import numpy as np
import time 

capture = cv2.VideoCapture(0)

# # showing values of the properties
# print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(capture.get(cv2.CAP_PROP_FRAME_WIDTH)))
# print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# print("CAP_PROP_FPS : '{}'".format(capture.get(cv2.CAP_PROP_FPS)))
# print("CAP_PROP_POS_MSEC : '{}'".format(capture.get(cv2.CAP_PROP_POS_MSEC)))
# print("CAP_PROP_FRAME_COUNT  : '{}'".format(capture.get(cv2.CAP_PROP_FRAME_COUNT)))
# print("CAP_PROP_BRIGHTNESS : '{}'".format(capture.get(cv2.CAP_PROP_BRIGHTNESS)))
# print("CAP_PROP_CONTRAST : '{}'".format(capture.get(cv2.CAP_PROP_CONTRAST)))
# print("CAP_PROP_SATURATION : '{}'".format(capture.get(cv2.CAP_PROP_SATURATION)))
# print("CAP_PROP_HUE : '{}'".format(capture.get(cv2.CAP_PROP_HUE)))
# print("CAP_PROP_GAIN  : '{}'".format(capture.get(cv2.CAP_PROP_GAIN)))
# print("CAP_PROP_CONVERT_RGB : '{}'".format(capture.get(cv2.CAP_PROP_CONVERT_RGB)))
  
frameWidth = 850
frameHeight = 500
framebrightness = 150
cap = cv2.VideoCapture(0)
capture.set(3, frameWidth)
capture.set(4, frameHeight)
# capture.set(10, framebrightness)

# myColors = [[5, 107, 0, 190, 255, 255]]
# myColors = [[60, 65, 120, 180, 200, 240]]


myColorValues = [[51, 153, 255]]

myPoints = []

while True:

    ret,frame = capture.read()

    # ORANGE_MIN = np.array([5, 50, 50],np.uint8)
    # ORANGE_MAX = np.array([15, 255, 255],np.uint8)

    # ORANGE_MIN = np.array(myColors[0][:3],np.uint8)
    # ORANGE_MAX = np.array(myColors[0][3:],np.uint8)

    hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # frame_threshed = cv2.inRange(hsv_img, ORANGE_MIN, ORANGE_MAX)
    frame_threshed = cv2.inRange(hsv_img,(4, 100, 20), (17, 230, 250) )


    cv2.imshow('frames', frame_threshed)

    if cv2.waitKey(10) & 0xFF == ord('q') :
        break

capture.release()
cv2.destroyAllWindows()