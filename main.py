
import re
import datetime
import time
import sys
import requests
from camera import *



if __name__ == "__main__":
    
    cam = Camera(101)
    #CameraTime = cam.getTimeCamera()
    cam.setTimeCamera()
        
    """
    camTime = []
    camTime.append((6, "06:41:00"))
    print "camTime[0]"
    print camTime[0]
    """
    #time.sleep(2)
    #cam.captureAction()

    """
    i=0
    for i in range(4):
        dayNumber = int(time.strftime('%w'));
        hour = str(time.strftime('%X'));
        currentTime = (dayNumber, hour)
        print currentTime
        time.sleep(1)
        i += 1
    """

        
    cam.captureAction()
    
    """
    while 1:
        #cam.
        dayNumber = int(time.strftime('%w'));
        hour = str(time.strftime('%X'));
        currentTime = (dayNumber, hour)
        print currentTime
        #print cam.getCameraTime()
    
        if currentTime in cam.getCameraTime():
           cam.captureAction()
           cam.setTimeCamera()
        time.sleep(1)
    """

    
    
        
        
        
