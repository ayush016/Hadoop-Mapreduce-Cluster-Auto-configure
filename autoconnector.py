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
   #b1 = QPushButton(win)
   #b1.setText("Make Datanode")
   #b1.move(50,20)
   #b1.clicked.connect(b1_clicked)

   #win.setGeometry(100,100,200,100)
   #win.setWindowTitle("Datanode Terminal")
   #win.show()
   b1_clicked()
   sys.exit(app.exec_())

def b1_clicked():
	f = open("iplist.txt","r")
	ip=f.readlines()
	f.close()
	k=[]
	count=-1
	for i in ip:
		cpid=0
		count=count+1
		k.append(i)
		k[count]=k[count].replace('\n','')
		print count
		if(cpid==0):
			os.system("sshpass -p 'ayush' scp -o StrictHostKeyChecking=no autofinder.py root@"+k[count]+":/home/ayush ")
			os.system("sshpass -p 'ayush' ssh root@"+k[count]+" '(python autofinder.py "+k[count]+" )' >> /home/ayush/python/project/pyqt/finder.txt")
			
			#os.system("cd /")
			#os.system("python autologin.py")
			#quit()
		
	#quit()
	g=open("finder.txt","r")
	lines=g.readlines()
	for i in lines:
		if("1-" in i)
			k=i.replace("1-","")
			print k
		if("2-" in i)
			k=i.replace("2-","")
			print k

if __name__ == '__main__':
   window()
