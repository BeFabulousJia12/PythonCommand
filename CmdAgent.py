import socket
import threading
import os

from urllib import unquote_plus

CMD_TCP_PORT = 9099

class CmdThread(threading.Thread):
    
    channel = None
    
    def __init__(self, chnl):
        threading.Thread.__init__ (self)
        self.channel = chnl
        
    def run(self):
        line = self.channel.makefile().readline().rstrip('\n\r');
        if line <> '' :
            self.process(line)
        else:
            self.channel.send("ERROR - Incorrect command syntax")
            self.channel.close()

    def process(self, cmdline):
        inp = cmdline.split()
        self.processCommand(inp[0], inp[1:])
        
    def processCommand(self, cmd, params):
        ucmd = unquote_plus(cmd).lower()
        uparams = [unquote_plus(prm) for prm in params]
        
        if ucmd == 'system':
            self.doSystem(uparams)
        else:
	    if ucmd == 'system_no_wait':
		self.doSystemNoWait(uparams)
	    else:
                print 'ERROR - Unknown command: ' + cmd
                self.channel.send('ERROR - Unknown command: ' + cmd)
        
    def doSystem(self, params):
        if (params != None and len(params) > 0):
            dparam = " ".join(params)
            print 'SYSTEM command: ' + dparam
            try :
                retVal = os.system(dparam)
                self.channel.send('OK - Return code %d' % retVal)
            except:
                self.channel.send('ERROR - Exception during execution:' + sys.exc_info()[0])
                print "Error running command SYSTEM:", sys.exc_info()[0]
        else:
            print "ERROR - SYSTEM command - No parameters"
            self.channel.send("ERROR - SYSTEM command - No parameters")
	self.channel.close()

    def doSystemNoWait(self, params):
        if (params != None and len(params) > 0):
            dparam = " ".join(params)
	    self.channel.close()
            print 'SYSTEM_NO_WAIT command: ' + dparam
            try :
                os.system(dparam)                
            except:               
                print "Error running command SYSTEM_NO_WAIT:", sys.exc_info()[0]
        else:
            print "ERROR - SYSTEM_NO_WAIT command - No parameters"
            self.channel.send("ERROR - SYSTEM_NO_WAIT command - No parameters")
    

cmdSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cmdSocket.bind(('', CMD_TCP_PORT))
cmdSocket.listen(5)

runFlag = True
while runFlag :
        print "Waiting for connection ..."
        channel, address = cmdSocket.accept()
        print "... Connection accepted"
        sockThread = CmdThread(channel)
        sockThread.start()
