

from ledState import * 


class CameraOffState(LedState):

    def __init__(self):
        #print "BlinkState"
        LedState.__init__(self)
        self._getLeds().getRedLed().turnoff()
        self._getLeds().getOrangeLed().turnoff()
        self._getLeds().getGreenLed().turnoff()
        self._getLeds().getBlueLed().turnoff()

