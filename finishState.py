

from ledState import * 


class FinishState(LedState):

    def __init__(self):
        #print "FinishState"
        LedState.__init__(self)
        self._getLeds().getRedLed().turnoff()
        self._getLeds().getOrangeLed().turnoff()
        self._getLeds().getGreenLed().turnOn()
        self._getLeds().getBlueLed().turnOn()

