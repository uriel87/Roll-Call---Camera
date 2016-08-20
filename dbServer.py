
from server import *
import MySQLdb
#import paramiko
import re


from defineFile import *
#import time


class DbServer(Server):

    def __init__(self, host, port, username, password, dbName):
        Server.__init__(self, host, port, username, password)
        self.__dbName = dbName
        self.__db = None
        self.__cursor = None
        self.__timeBeforeOpenCamera = 10


    def connect(self):
        try:
            self.__db = MySQLdb.connect(host = self.host, port = self.port, user = self.username, passwd = self.password, db = self.__dbName)
            self.__cursor = self.__db.cursor()
            self.__cursor.execute("SELECT VERSION()")
            self.__cursor.fetchone()
            #print "Database version: %s " % self.__cursor.fetchone()
            print "connected to MySQLdb server"
            #return self.__db
            
        except MySQLdb.Error as e:
            print "Error: problem to connect MySQLdb server"
        



    def disConnect(self):
        try:
            self.__db.close
            print "Disconnected from MySQLdb server"
            
        except MySQLdb.Error as e:
            print "Error: problem to disconnect from MySQLdb server"



    def getTimeOpenCam(self, cameraId):

        try:
            query= "SELECT day_of_week, open_time FROM cameras WHERE camera = %d" %(cameraId)
            timeArr = []
            self.__cursor.execute(query)
            results = self.__cursor.fetchall()
            for row in results:
                    day = int(row[0])
                    hour = str(row[1])
                    timeArr.append((day,self.changeTime(hour)))
            return timeArr
        
        except MySQLdb.Error as e:
            print "Error: can't get camera data"
            self.disConnect()




    def changeTime(self, hour):
        h, m, s = re.split(':', hour)
        hour = int(h)
        second = int(s)
        minutes = int(m) - self.__timeBeforeOpenCamera
        if minutes < 0:
            minutes = minutes + 60
            hour -= 1
        newTime = "%d:%d:%d" %( hour, minutes, second )
        return newTime
            









        
        
