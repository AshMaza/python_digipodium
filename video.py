import cv2
import numpy as np

cam = cv2.VideoCapture(r'M:\MyEdits\Virat X Siraj.mp4')   #link to webcam

while cam.isOpened():
    status,img =cam.read()
    if status is None:
        break
    rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    stack = np.hstack((img,rgb))
    cv2.imshow('Webcam',stack)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cam.release()

