#!/usr/bin/python2
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import socket
import fcntl
import struct
import os
def window():
   app = QApplication(sys.argv)
   win = QDialog()
   b1 = QPushButton(win)
   b1.setText("Make Datanode")
   b1.move(50,20)
   b1.clicked.connect(b1_clicked)

   win.setGeometry(100,100,200,100)
   win.setWindowTitle("Datanode Terminal")
   win.show()
   sys.exit(app.exec_())

def b1_clicked():
	f = open("datanodes.txt","r")
	mip=open("YourIp.txt","r")
	mipp=mip.readlines()
	myiip=mipp[0]
	ip=f.readlines()
	k=[]
	count=0
	for i in ip:
		k.append(i)
		k[count]=k[count].replace('\n','')
		
	#print k
		if(count==0):
			os.system("sshpass -p 'ayush' scp -o StrictHostKeyChecking=no autologinjob.py root@"+k[count]+":/root/ ")
			os.system("sshpass -p 'ayush' ssh root@"+k[count]+" python autologinjob.py "+k[count])
			
		else:

			os.system("sshpass -p 'ayush' scp -o StrictHostKeyChecking=no autologin.py root@"+k[count]+":/root/ ")
			os.system("sshpass -p 'ayush' ssh root@"+k[count]+" python autologin.py "+myiip+" "+k[0])
		count=count+1
		#os.system("cd /")
		#os.system("python autologin.py")

if __name__ == '__main__':
   window()
