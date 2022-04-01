from handDetection import HandDetection
import cv2

handDetection = HandDetection(min_detection_confidence=0.5,min_tracking_confidence=0.5)

webcam = cv2.VideoCapture()
webcam.open(0,cv2.CAP_DSHOW)

min_dest,max_dest = 25,190
while True:
    status , frame = webcam.read()
    frame = cv2.flip(frame,1)
    handLandMarks = handDetection.findHandLandMark(image=frame,draw=True)
    if len(handLandMarks) !=0:
        x4, y4 = handLandMarks[4][1],handLandMarks[4][2]
        x8, y8 = handLandMarks[8][1],handLandMarks[8][2]

        #circle
        cv2.circle(frame,(x4,y4),10,(255,255,0),cv2.FILLED)
        cv2.circle(frame,(x8,y8),10,(255,255,0),cv2.FILLED)
        xTengah,yTengah = int((x4+x8)/2),int((y4+y8)/2)
        cv2.circle(frame,(xTengah,yTengah),10,(255,255,0),cv2.FILLED)
        cv2.line(frame,(x4,y4),(x8,y8),(255,255,0),5)


    cv2.imshow("Hand Tapak", frame)
    if cv2.waitKey(1) == ord('p'):
        break
cv2.destroyAllWindows()
webcam.release()