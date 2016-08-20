
import re
import datetime
import time
import sys
import requests
import thread
from camera import *




cam = Camera(101)
cam.setTimeCamera()


def parse_reply(reply):
    return reply[reply.find("<p>")+3: reply.find("</p")]

def check_on():
    #r = requests.get("http://10.0.0.7:8080/get_cmd")
    r = requests.get("http://facerecoapp.cloudapp.net:8080/get_cmd")
    reply = r.text
    cmd = parse_reply(reply)
    
    if cmd == "NONE":
        return
    
    if cmd == "on":
        print "ON"
        cam.captureAction()
        """
        while 1:
            print "in on"
            
            time.sleep(1)
            
            if check_cmd_off():
                break
            """
        #cam.captureAction()
    """
    if cmd == "off":
        print "OFF"
        cam.finishCaptureAction()
    """
        
    
"""
def check_cmd_off():
    r = requests.get("http://10.0.0.7:8080/get_cmd")
    reply = r.text
    cmd = parse_reply(reply)    
    if cmd == "off":
        print "OFF"
        #cam.finishCaptureAction()
        return 1
"""
    

def loop_connect_to_server():
    print "[*] Running..."
    while 1:
        check_on()
        time.sleep(1)



thread.start_new_thread(loop_connect_to_server, ())
