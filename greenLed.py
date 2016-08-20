
from led import *
import RPi.GPIO as GPIO


class GreenLed(Led):

    def __init__(self, pinNumber):
        Led.__init__(self, pinNumber)



