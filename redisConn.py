import os, socket 
''' 
   Lightweight connection to Redis
   @todo needs timeout handling
   @todo needs to ping redis to get a pong. if not pong, then fail
'''
class redisConn:
    
    def __init__(self, host='', port=''):
        '''
           Set up the connection
           If not set, the port is the default 6379
           If not set, the host is localhost
        '''
        if not port:
            self.port = 6379
        else:
            self.port = port
            
        if not host:
            self.host = '127.0.0.1'
        else:
            self.host = host
    
    def command (self, command, rediskey='', data=''):
        '''
           Light weight connection call to server
           Takes the connection command
        '''
        data is None
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host, self.port))
            s.send(command + ' '+rediskey)
            data = s.recv(1024)
            s.close()
            print 'Received', repr(data)
        except socket.error, msg:
            s.close()
            print msg
        return data