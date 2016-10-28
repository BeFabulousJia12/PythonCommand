import socket
import sys
import time

def calcConnectionParams(str):
    pos = str.find(':')
    if (pos < 0):
        return str, DEFAULT_CMD_TCP_PORT
    else:
        return str[:pos], int(str[(pos + 1):])
    
if (len(sys.argv) < 3):
    print("CmdClient parameters syntax error.")
    print(" Proper usage: ")
    print("    CmdClient.py <agent-ip>[:<agent-port>] <param-1> ... <param-N>")
else:
    DEFAULT_CMD_TCP_PORT = 9099
    
    if(sys.argv[1].lower() == "sleep"):
	print("sleep "+sys.argv[2]+" seconds.")
        sec = int(sys.argv[2])
	time.sleep(sec)
	sys.exit(0)
   
    #socket connection
    agentAddr, agentPort = calcConnectionParams(sys.argv[1])    
    channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    channel.connect(calcConnectionParams(sys.argv[1]))

    #system command, wait for finish
    if (len(sys.argv) == 3):
	print("The script is going to halt until the BAT command is completed")	
	channel.send('SYSTEM ' + (' '.join(sys.argv[2:3])) + '\n')
	sys.exit(0)
    #system command, return immediately
    if (len(sys.argv) == 4):
	print("The script is goingt to return immediately when the command is sent")
	channel.send('SYSTEM_NO_WAIT ' + (' '.join(sys.argv[2:3])) + '\n')
    chFile = channel.makefile()
    
    for line in chFile:
        print line


