import socket #Socket package
import subprocess #Processes package
import sys #System package
from datetime import datetime #Time & Date

#clear your screen
subprocess.call( 'clear', shell=True )

#ask for a host
remoteServer = raw_input("Enter a remote host to scan:")
remoteServerIP = socket.gethostbyname( remoteServer )
portRange = input( "Enter the maximum port number to scan:")

#print the banner
print "-" * 60
print "Please wait, scanning remote host:", remoteServerIP
print "-" * 60

#check what time the scan started.
starttime = datetime.now()

#scan ports within the range, will also do some error handling

try:
    for port in range( 1, int( portRange)+1 ):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: \t Open".format(port)
        sock.close()
        
except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()
    
except socket.gaierror:
    print "Hostname could not be resolved, Exiting"
    sys.exit()
   
except socket.error:
    print "Couldn't connect to server"
    sys.exit()
    
# grab end time
endtime = datetime.now()

#find the total scan time
scantime = endtime-starttime
print 'Scanning completed in: ', scantime
