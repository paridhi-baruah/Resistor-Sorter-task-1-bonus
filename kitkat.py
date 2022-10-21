# importing Modules
from asyncio.windows_events import NULL
import cv2 as cv
import numpy as np
from datetime import datetime

# Capturing Video
cap=cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output1.avi', fourcc, 20.0, (640, 480))

flagrec=False
starttime=NULL
font = cv.FONT_HERSHEY_SIMPLEX
flagshow=True
fooledyou=NULL
def mouse_click(event,x ,y , flags, param):
    global flagshow
    global flagrec
    global fooledyou
    global starttime
    if x<=370 and x>=270 and y<=290 and y>=190:
        if event == cv.EVENT_RBUTTONDOWN:
            flagshow=False
            flagrec=True
            fooledyou=datetime.now()
            starttime=NULL
# Recording 
while(True):
    ret, frame = cap.read()
    if ret == True: 
        if cv.waitKey(1) & 0xFF == ord('p'):
            flagrec=True
            starttime=datetime.now()
        if starttime:
            if starttime.time().second+5<=datetime.now().time().second:
                frame=cv.rectangle(frame,(270,190),(370,290),(0,0,255),-1)
                frame=cv.putText(frame,'Paridhi',(290,240) ,font ,0.5 ,(255,255,255) ,1 ,cv.LINE_AA)
                flagrec=False
        if fooledyou:
            if fooledyou.time().second+10<=datetime.now().time().second:
                print("check")
                frame=np.zeros((480,640,3),np.uint8)
                frame=cv.putText(frame,'Fooled You',(100,240) ,font ,2 ,(255,255,255) ,2 ,cv.LINE_AA)
                flagshow=True
        if cv.waitKey(1) & 0xFF == ord('l'):
            break
        if flagshow:
            cv.imshow('frame',frame)
            cv.setMouseCallback('frame',mouse_click)
        else:
            cv.destroyAllWindows()
        if flagrec:
            out.write(frame)
       
    else:
        break 
cap.release()
out.release()
cv.destroyAllWindows()