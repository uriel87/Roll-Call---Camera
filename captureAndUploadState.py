
from ledState import * 


class CaptureAndUploadState(LedState):

    def __init__(self):
        #print "CaptureAndUploadState"
        LedState.__init__(self)
        self._getLeds().getRedLed().turnOn()
        self._getLeds().getOrangeLed().turnOn()
        self._getLeds().getGreenLed().turnoff()
        self._getLeds().getBlueLed().turnOn()
