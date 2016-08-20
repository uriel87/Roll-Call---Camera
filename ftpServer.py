
import ftplib
from ftplib import FTP
from server import *
from defineFile import *

import time


class FtpServer(Server):

    def __init__(self, host, port, username, password, localPath):
        Server.__init__(self, host, port, username, password)
        self.__ftp = None
        self.__localPath = localPath
        self.__uploadPath = uploadPathFtp
        #self.__fileNumber = 0


    def connect(self):
        try:
            self.__ftp = FTP()
            self.__ftp.connect(self.host, port = self.port)
            self.__ftp.login(self.username, self.password)
            self.__ftp.cwd(self.__uploadPath)
            self.__ftp.set_pasv(False)
            print "connected to ftp server"
            
        except ftplib.all_errors:
            print "Error: problem to connect ftp server"
        



    def disConnect(self):
        try:
            #self.__fileNumber = 0
            self.__ftp.quit()
            print "Disconnected from ftp server"
            
        except ftplib.all_errors:
            print "Error: problem to disconnect from ftp server"

    
    
    def getFtp(self):
        return self.__ftp

        
    
    def getLocalPath(self):
        return self.__localPath


    
    def getUploadPath(self):
        return self.__uploadPath


    """
    def incFileNumber(self):
        self.__fileNumber += 1
    """



    def uploadFile(self, uploadFilePath):
        try:
            fileName = open(uploadFilePath,"rb")
            pathSplit = uploadFilePath.split("/")
            #self.__ftp.set_pasv(False)
            #print uploadFilePath
            finalFileName = pathSplit[len(pathSplit)-1]
            self.__ftp.storbinary("STOR " + finalFileName, fileName)
            print "upload done"
            
        except IOError:
            print "Error: can't find file or data"
            self.disConnect()
            


        



"""
ftp = FtpServer("host11", "port11", "username11", "password11", "localPath11", "uploadPath11")
print ftp.port
print ftp.getLocalPath()
print ftp.getuploadPath()
print ftp.getFtp()

while 1:
    
    print ftp.uploadFile()
    time.sleep(1)
    
"""





#print "connect to server"
#print "uploading..."
#filename = "frame000.jpg"
#ftp = FTP()
#ftp.connect("facerecoapp.cloudapp.net",port=21)
#ftp.login("UserUpload","Sd299ed9r")

#ftp.cwd("/uploadFile/camera")
#uploadFilePath = "frame%d.jpg" % (fileNumber)
#ftp.set_pasv(False)
#myfile = open(uploadFilePath,"rb")
#pathSplit = uploadFilePath.split("/")
#finalFileName = pathSplit[len(pathSplit)-1]
#ftp.storbinary("STOR " + finalFileName, myfile)
#print "Upload completed"
#ftp.quit()

        
        
