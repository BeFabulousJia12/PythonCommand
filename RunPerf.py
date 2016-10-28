import os
import sys
import time

print("Start Master Jmeter")
#Change the path string as yours -- where the RunJmeterPerftest.bat is
Path ="F:\\Jmeter\\jmeter\\bin\\"
batMaster = 'RunJmeterPerftest.bat'
os.system('start '+ Path + batMaster)
#SVT
#Local file
##batMaster_SVTinfo = 'RunSVTInfoPerftest.bat'
##os.system('start '+ Path + batMaster_SVTinfo)
#Remote file
cmdclient ="CmdClient.py"
remoteip="10.1.64.237"
commandsvt = "\"start C:\\jmeter\\bin\\RunSVTInfoPerftest.bat\""
print(Path + cmdclient + " " + remoteip +" " + commandsvt)
#os.system(Path + cmdclient + " " + remoteip +" " + commandsvt)

print("waiting for starting remote Jmeter clients")
time.sleep(3600)

print("===Remote Jmeter Client01===")
cmdclient ="CmdClient.py"
remoteip="10.1.64.239"
command = "\"start C:\\jmeter\\bin\\RunJmeterPerftest.bat\""
print(Path + cmdclient + " " + remoteip +" " + command)
os.system(Path + cmdclient + " " + remoteip +" " + command)

time.sleep(3600)

print("===Remote Jmeter Client02===")
cmdclient ="CmdClient.py"
remoteip="10.1.32.76"
command = "\"start C:\\jmeter\\bin\\RunJmeterPerftest.bat\""
print(Path + cmdclient + " " + remoteip +" " + command)
os.system(Path + cmdclient + " " + remoteip +" " + command)


time.sleep(1800)
print("===Remote Jmeter Client03===")
cmdclient ="CmdClient.py"
remoteip="10.1.32.75"
command = "\"start C:\\jmeter\\bin\\RunJmeterPerftest.bat\""
print(Path + cmdclient + " " + remoteip +" " + command)
os.system(Path + cmdclient + " " + remoteip +" " + command)

time.sleep(1800)
print("===Remote Jmeter Client04===")
cmdclient ="CmdClient.py"
remoteip="10.1.32.74"
command = "\"start C:\\jmeter\\bin\\RunJmeterPerftest.bat\""
print(Path + cmdclient + " " + remoteip +" " + command)
os.system(Path + cmdclient + " " + remoteip +" " + command)

time.sleep(1800)

print("===Remote Jmeter Client05===")
cmdclient ="CmdClient.py"
remoteip="10.1.32.73"
command = "\"start C:\\jmeter\\bin\\RunJmeterPerftest.bat\""
print(Path + cmdclient + " " + remoteip +" " + command)
os.system(Path + cmdclient + " " + remoteip +" " + command)

print("===== All Jmeters Running Done =====")
