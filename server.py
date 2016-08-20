

class Server():

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        print "connect to server"


    def disConnect(self):
        print "disconnect to server"
        
