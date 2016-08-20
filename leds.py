

import RPi.GPIO as GPIO
from orangeLed import *
from redLed import *
from greenLed import *
from blueLed import *


class Leds(object):
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(Leds, self).__new__(self)
        return self._instance

    def __init__(self):
        
        GPIO.setmode(GPIO.BCM)
        self.__redLed = RedLed(27)
        self.__orangeLed = OrangeLed(17)
        self.__greenLed = GreenLed(3)
        self.__blueLed = BlueLed(18)



    def getRedLed(self):
        return self.__redLed


    def getOrangeLed(self):
        return self.__orangeLed
    

    def getGreenLed(self):
        return self.__greenLed

    
    def getBlueLed(self):
        return self.__blueLed
    


"""
leds = Leds()
leds.getBlueLed().blink()
leds.getRedLed().blink()
leds.getOrangeLed().blink()
leds.getGreenLed().blink()
"""






        
        
    
