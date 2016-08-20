

from ledState import * 


class NoRecognizeState(LedState):

    def __init__(self):
        #print "NoRecognizeState"
        LedState.__init__(self)
        self._getLeds().getRedLed().turnOn()
        self._getLeds().getOrangeLed().turnoff()
        self._getLeds().getGreenLed().turnoff()
        self._getLeds().getBlueLed().turnOn()



