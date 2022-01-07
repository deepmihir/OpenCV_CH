
#________________ CH 8 shape detection ___________________#
import cv2
import numpy as np
# path = 'Resources/shape.jpg'
# img = cv2.imread(path)
# imgContour = img.copy()
#
# def getContours(img):
#     contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         print(area)
#         if area > 500 :
#             cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
#             peri = cv2.arcLength(cnt,True)
#             # print(peri)
#             approx =cv2.approxPolyDP(cnt,0.02*peri,True)
#             print(len(approx))
#             objCor = len(approx)
#             x,y,w,h = cv2.boundingRect(approx)
#             if objCor == 3:objectType = "Tri"
#             elif objCor == 4:
#                 aspratio = w/float(h)
#                 if aspratio > 0.8 and aspratio < 1.10: ObjectType="Square"
#                 else:objectType = "Rectangle"
#             elif objCor > 4: objectType="Cir"
#             else:objectType="None"
#             cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
#             cv2.putText(imgContour,objectType,
#                         (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,50),2)
#
#
#
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
# imgCanny = cv2.Canny(imgBlur,50,50)
# imgBlank = np.zeros_like(img)
# getContours(imgCanny)
#
#
# cv2.imshow("Original",img)
# cv2.imshow("Gray",imgGray)
# cv2.imshow("Blur",imgBlur)
# cv2.imshow("Canny",imgCanny)
# cv2.imshow("COntour",imgContour)
#
#
# cv2.waitKey(0)



#______________________ CH 8 Face detection _________________ #

faceCascade=cv2.CascadeClassifier("Resources/frontalface.xml")



cap = cv2.VideoCapture(0)


cap.set(3,640) #Width id=3 as 640
cap.set(4,480) #hight id=4 as 480
cap.set(10,100) #ID=10 is for brightness
while True:
    success, img = cap.read()


    # img = cv2.imread('Resources/face.png')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Webcam",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# cv2.imshow("Result",img)
# cv2.waitKey(0)
