import cv2
import os
import glob
import time
import datetime
import requests
import sys
import re

from contextLedState import *
from defineFile import *
from dbServer import *
from ftpServer import *



class Camera():

    def __init__(self, idCamera):
        self.__dbServer = DbServer(hostDb, portDb, usernameDb, passwordDb, dbNameDb)
        self.__ftpServer = FtpServer(hostFtp, portFtp, usernameFtp, passwordFtp, uploadPathFtp)
        self.__idCamera = idCamera
        self.__cameraTime = None
        self.setTimeCamera()
        self.__cls = ContextLedState()
        self.__cls.switchLedState(CameraOff)
        self.__CameraTimer = 10
        self.__video_capture = cv2.VideoCapture(0)
        

    def captureAction(self):
        self.__ftpServer.connect()
        #self.__cls.switchLedState(cameraStart)
        cascPathFace = os.getcwd()+"/haarcascade_frontalface_default.xml"
        cascPathEyes = os.getcwd()+"/haarcascade_eye.xml"

        faceCascade = cv2.CascadeClassifier(cascPathFace)
        faceEyes = cv2.CascadeClassifier(cascPathEyes)

        #video_capture = cv2.VideoCapture(0)
        self.__dbServer.connect()

        fileNumber = 0
        now = datetime.datetime.now()
        finishTime = now.minute + self.__CameraTimer
        if finishTime > 60:
           finishTime = int(finishTime - 60)
           
        #print now.second
        #print finishTime
        pic = 3
        while 1: #now.minute < finishTime:
            print "pic in while: %d" %(pic)
            if pic < 3:
                pic += 1
            else :
                pic = 3
                
            if check_cmd_off():
                self.finishCaptureAction()
                return

            print "pic in after if else: %d" %(pic)
                
            ret, frame = self.__video_capture.read()
            ret, singlePic = self.__video_capture.read()
            """
            if not frame:
                print"if not ret"
                ret, frame = self.__video_capture.read()
                ret, singlePic = self.__video_capture.read()
                cv2.imshow('Video', frame)
                break
            else:
                cv2.imshow('Video', frame)
            """
            
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=3,
                minSize=(200, 200),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            """
            pic = 1
            while 1: #now.minute < finishTime:
            """                

            self.__cls.switchLedState(noRecognize)
            for (x, y, w, h) in faces:
                
                #cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = faceEyes.detectMultiScale(roi_gray)
                for (x, y, w, h) in eyes:
                    if pic == 3:
                        print "in"
                        self.__cls.switchLedState(captureAndUpload)
                        uploadFilePath = os.getcwd() + "/images/%s_frame%d.jpg" % (self.__idCamera, fileNumber)
                        cv2.imwrite(uploadFilePath ,singlePic)
                        print uploadFilePath
                        self.__ftpServer.uploadFile(uploadFilePath)
                        fileNumber += 1
                        print "fileNumber: %d" %(fileNumber)
                        self.__cls.switchLedState(finish)
                        pic = 0
                        print "pic in for loop 2222: %d" %(pic)
                        time.sleep(1)

            #cv2.imshow('Video', frame)

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
        self.__cls.switchLedState(CameraOff)
        self.__video_capture.release()
        cv2.destroyAllWindows()
        self.__ftpServer.disConnect()
        #self.deleteFiles()
        
            



    def finishCaptureAction(self):
        self.__cls.switchLedState(CameraOff)
        self.__video_capture.release()
        cv2.destroyAllWindows()
        self.__ftpServer.disConnect()
        self.deleteFiles()
    


    def uploadImgs(self):
        print "Upload images..."
        self.__ftpServer.connect()
        path = os.getcwd() + "/images/"
        dirs = os.listdir(path)
        for fileName in dirs:
            uploadFilePath = "images/%s" % (fileName)
            #print uploadFilePath
            self.__ftpServer.uploadFile(uploadFilePath)

        print "Upload completed"

            
    def deleteFiles(self):
        directory = os.getcwd()+"/images/"
        
        os.chdir(directory)
        files = glob.glob('*.jpg')
        for filename in files:
            os.unlink(filename)

        print "images from %s was deleted" % (directory)




    def setTimeCamera(self):
        self.__dbServer.connect()
        self.__cameraTime = self.__dbServer.getTimeOpenCam(self.__idCamera)
        self.__dbServer.disConnect()
        #return cameraTime


    def getCameraTime(self):
        return self.__cameraTime
    


    

def parse_reply(reply):
    return reply[reply.find("<p>")+3: reply.find("</p")]


def check_cmd_off():
    r = requests.get("http://facerecoapp.cloudapp.net:8080/get_cmd")
    reply = r.text
    cmd = parse_reply(reply)    
    if cmd == "off":
        print "OFF"
        return 1
    else:
        return 0






    
