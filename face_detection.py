import cv2
import numpy as np

cam = cv2.VideoCapture(0)   #link to webcam
face_cascade = cv2.CascadeClassifier()
face_cascade.load(r'classifier/haarcascade_frontalface_default.xml')
while cam.isOpened():
    status,img =cam.read()
    if status is None:
        break
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = face_cascade.detectMultiScale(gray)
    height, width , _ = img.shape
    if len(faces) > 0:
        print(f'{len(faces)} face(s) found')
        for i , (x,y,w,h) in enumerate(faces):
            #draw rectangle around faces
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
            faceROI= gray[y:y+h,x:x+w]
            cv2.imshow('Face{i}',faceROI)
            eyes =  eyes_cascade.detectMultiScale(faceROI)
            

    else:
        #display no face found
        cv2.putText(
            img,'No face found',(10,height-50),cv2.FONT_HERSHEY_SIMPLEX , 1,(0,0,255),2
        )
    cv2.imshow('Webcam',img)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cam.release()

