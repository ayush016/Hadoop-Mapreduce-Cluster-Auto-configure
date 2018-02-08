import socket
import fcntl
import struct
import os
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, 
        struct.pack('256s', ifname[:15])
    )[20:24])

x=os.system("ip link|grep 'state UP'|cut -d ':' -f 2 > NetworkInterface.txt")
#print x
f=open("NetworkInterface.txt","r")
line = f.readlines()
f.close()
k=[]
count=0
for i in line:
	k.append(i)
	k[count]=k[count].replace('\n','')
	k[count]=k[count].replace(' ','')
	count = count +1
g = open("NetworkInterface.txt","w")
count_new = 0
for i in line:
	g.write(k[count_new])
	count_new = count_new + 1
g.close()
#print k[0]
myip=get_ip_address(k[0])

namenode=open("/etc/hadoop/hdfs-site.xml","r")
contents = namenode.readlines()
namenode.close()
count = 0
for i in contents:
	count = count + 1
	#print i
	if(i=="<configuration>\n" or i=="<configuration>"):
		break

os.system("rm -rf /master")


namenode=open("/etc/hadoop/hdfs-site.xml","w")
x=0

for i in contents:
	if(x<count):
		namenode.write(i)
	if(i=="</configuration>\n"):
		namenode.write(i)
	x=x+1

namenode=open("/etc/hadoop/hdfs-site.xml","r")
contents = namenode.readlines()
namenode.close()
namenode=open("/etc/hadoop/hdfs-site.xml","w")
count = 0
for i in contents:
	count = count + 1
	#print i
	if(i=="<configuration>\n" or i=="<configuration>"):
		break

contents.insert(count, "<property>\n<name>dfs.name.dir</name>\n<value>/master</value>\n</property>\n")
contents = "".join(contents)
namenode.write(contents)

namenode.close()

namenode_core=open("/etc/hadoop/core-site.xml","r")
contents = namenode_core.readlines()
namenode_core.close()
count = 0
for i in contents:
	count = count + 1
	print i
	if(i=="<configuration>\n" or i=="<configuration>"):
		break
namenode_core=open("/etc/hadoop/core-site.xml","w")	


namenode_core=open("/etc/hadoop/core-site.xml","w")
x=0

for i in contents:
	if(x<count):
		namenode_core.write(i)
	if(i=="</configuration>\n"):
		namenode_core.write(i)
	x=x+1
namenode_core=open("/etc/hadoop/core-site.xml","r")
contents = namenode_core.readlines()
namenode_core.close()
namenode_core=open("/etc/hadoop/core-site.xml","w")
contents.insert(count, "<property>\n<name>fs.default.name</name>\n<value>hdfs://"+myip+":9001</value>\n</property>\n")
contents = "".join(contents)
namenode_core.write(contents)
namenode_core.close()
os.system("iptables -F")
os.system("hadoop namenode -format -force")
os.system("hadoop-daemon.sh start namenode")

