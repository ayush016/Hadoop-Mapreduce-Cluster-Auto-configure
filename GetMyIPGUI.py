#!/usr/bin/python2
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import socket
import fcntl
import struct
import os
def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QPushButton(w)
   b.setText("See")

   b.move(120,100)
   b.clicked.connect(showdialog)
   w.setWindowTitle("All connected Ips in the Network")
   w.show()
   sys.exit(app.exec_())
   
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, 
        struct.pack('256s', ifname[:15])
    )[20:24])
	
def showdialog():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Information)
   x=os.system("ip link|grep 'state UP'|cut -d ':' -f 2 > NetworkInterface.txt")
#print x
   f=open("NetworkInterface.txt","r")
   line = f.readlines()
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
   z=get_ip_address(k[0])
   
   msg.setText(z)
   #msg.setText(line[1])
   #msg.setInformativeText("This is additional information")
   #msg.setWindowTitle("MessageBox demo")
   #msg.setDetailedText("The details are as follows:")
   #msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   msg.buttonClicked.connect(msgbtn)
	
   retval = msg.exec_()
   #print "value of pressed message box button:", retval
	
def msgbtn(i):
   print "Button pressed is:",i.text()
	
if __name__ == '__main__': 
   window()
