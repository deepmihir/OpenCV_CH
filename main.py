
#------------------ This File contain CH 2 to CH 7 programs of Learning Open CV-----------------------------#


import cv2
import numpy as np
#CH-2 Basic Functions
# img = cv2.imread("Resources/creta.jpg")
# kernel = np.ones((5,5),np.uint8)
# imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgblur = cv2.GaussianBlur(imgray,(7,7),0)
# imgcanny = cv2.Canny(img,150,200)
# imgDialation = cv2.dilate(imgcanny,kernel,iterations=1)
# imgEroded = cv2.erode(imgcanny,kernel,iterations=1)
# cv2.imshow("Gray image",imgray)
# cv2.imshow("blur image",imgblur)
# cv2.imshow("canny image",imgcanny)
# cv2.imshow("Dialate image",imgDialation)
# cv2.imshow("Eroded image",imgEroded)
# cv2.waitKey(0)

#ch3 Resizing and cropping
# print(img.shape)
# # imgResized = cv2.resize(img,(400,250)) #(width, hight)
# # cv2.imshow("Resized",imgResized)
# cv2.imshow("Normal",img)
# imgCrop = img[0:200,0:400]
# cv2.imshow("cropped",imgCrop)
# # print(imgResized.shape)
# cv2.waitKey(0)

#ch 4 shapes and text
# img = np.zeros((512,512,3),np.uint8)

# img[100:200,100:200] = 255,0,0 #BGR
# print(img)
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
# cv2.circle(img,(400,50),100,(255,255,0),3)
# cv2.putText(img,"  OpenCV  ",(300,100),cv2.FONT_ITALIC,1,(0,150,0),3)
# cv2.imshow("shapes",img)
# cv2.waitKey(0)

#ch 5 warp perspective
# width, height = 250,350
# pts1 = np.float32([[244,117],[397,215],[266,430],[104,325]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv2.warpPerspective(img,matrix,(width,height))
#
# cv2.imshow("Image",img)
# cv2.imshow("warp",imgOutput)
# cv2.waitKey(0)

#CH 6 is related to image stack that is skipped in my case
#where we can create horizontal or vertical image stack
#Here is stack images without a Function
# imgHor = np.hstack((img,img,img))
# imgver = np.vstack((img,img,img))
# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgver)
# cv2.waitKey(0)

# Here is stack images without a Function
# def stackImages(imgArray,scale,lables=[]):
#     sizeW= imgArray[0][0].shape[1]
#     sizeH = imgArray[0][0].shape[0]
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 imgArray[x][y] = cv2.resize(imgArray[x][y], (sizeW, sizeH), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#             hor_con[x] = np.concatenate(imgArray[x])
#         ver = np.vstack(hor)
#         ver_con = np.concatenate(hor)
#     else:
#         for x in range(0, rows):
#             imgArray[x] = cv2.resize(imgArray[x], (sizeW, sizeH), None, scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor= np.hstack(imgArray)
#         hor_con= np.concatenate(imgArray)
#         ver = hor
#     if len(lables) != 0:
#         eachImgWidth= int(ver.shape[1] / cols)
#         eachImgHeight = int(ver.shape[0] / rows)
#         print(eachImgHeight)
#         for d in range(0, rows):
#             for c in range (0,cols):
#                 cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
#                 cv2.putText(ver,lables[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
#     return ver

#................ Here is the CH 7 Color detection.............#
def empty(a):
    pass


path = 'Resources/lambo.jpg'
#Creting trackbar window
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",31,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",96,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)
cv2.createTrackbar("Val Min","Trackbars",57,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)

while True:

    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV,lower,upper)

    imgResult = cv2.bitwise_and(img,img,mask=mask) #work like and gate


    print(h_min,h_max,s_min,s_max,v_min,v_max)
    cv2.imshow("Original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("ImageResult", imgResult)
    cv2.waitKey(1)