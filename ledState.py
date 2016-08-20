
from leds import * 


class LedState(object):
    #leds = Leds()
    
    def __init__(self):
        self._leds = Leds()
    

    def _getLeds(self):
        return self._leds
