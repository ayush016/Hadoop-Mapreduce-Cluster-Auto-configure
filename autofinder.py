import os
import subprocess
import sys
output = subprocess.check_output("jps", shell=True)

if("namenode" in output or "Namenode" in output):
	print "1-",sys.argv[1]
elif("datanode" in output or "Datanode" in output):
	print "2-",sys.argv[1]
else:
	print "0-",sys.argv[1]
	
