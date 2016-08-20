

from noRecognizeState import *
from captureAndUploadState import *
from finishState import *
from cameraStartState import *
from defineFile import *
from cameraOffState import *

class ContextLedState():
    
    def __init__(self):
        print "__init__ ContextState"
        self.__currentLedState = NoRecognizeState()

        
    
    def switchLedState(self, stateSelected):
        
        state = {
                noRecognize : NoRecognizeState,
                captureAndUpload : CaptureAndUploadState,
                finish : FinishState,
                cameraStart : CameraStartState,
                CameraOff: CameraOffState
            }
        
        self.__currentLedState = state[stateSelected]()







        
