
import os


"""===================

leds state names

===================="""

noRecognize = "noRecognize"

captureAndUpload = "captureAndUpload"

finish = "finish"

cameraStart = "cameraStart"

CameraOff = "CameraOff"





"""===================

ftpServer.py

===================="""

hostFtp = "facerecoapp.cloudapp.net"
portFtp = 21
usernameFtp = "UserUpload"
passwordFtp = "Sd299ed9r"
uploadPathFtp = "/uploadFile/camera"
localPathFtp = os.getcwd() + "/images/"





"""===================

dbServer.py

===================="""

hostDb = "104.131.0.21"
portDb = 3306
usernameDb = "db_uriel"
passwordDb = "db_uriel1234"
dbNameDb = "rollcall"






"""===================

dbServer.py

===================="""

cascPathFace = os.getcwd()+"/haarcascade_frontalface_default.xml"
cascPathEyes = os.getcwd()+"/haarcascade_eye.xml"
