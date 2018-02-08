import os
import sys
myip = sys.argv[1]
datanode_core=open("/etc/hadoop/mapred-site.xml","r")
contents = datanode_core.readlines()
datanode_core.close()
count = 0
for i in contents:
	count = count + 1
        #print i
	if(i=="<configuration>\n" or i=="<configuration>"):
		break



datanode_core=open("/etc/hadoop/mapred-site.xml","w")

x=0

for i in contents:
	if(x<count):
		datanode_core.write(i)
	if(i=="</configuration>\n"):
		datanode_core.write(i)
	x=x+1
datanode_core = open('/etc/hadoop/mapred-site.xml','r')
contents = datanode_core.readlines()
datanode_core.close()
datanode_core=open("/etc/hadoop/mapred-site.xml","w")	
contents.insert(count, "<property>\n<name>mapred.job.tracker</name>\n<value>hdfs://"+myip+":9002</value>\n</property>\n")
contents = "".join(contents)
datanode_core.write(contents)
datanode_core.close()

os.system("iptables -F")
os.system("hadoop-daemon.sh start jobtracker")
