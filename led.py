
import time
import RPi.GPIO as GPIO


class Led():

    def __init__(self, pinNumber):
        GPIO.setmode(GPIO.BCM)
        self.__pinNumber = pinNumber
        GPIO.setup(self.__pinNumber, GPIO.OUT)


    def turnOn(self):
        GPIO.output(self.__pinNumber, True)
        

    def turnoff(self):
        GPIO.output(self.__pinNumber, False)


    def blink(self):
        while 1:
            GPIO.output(self.__pinNumber, True)
            time.sleep(1)
            GPIO.output(self.__pinNumber, False)
            time.sleep(1)





    


        
        
    
