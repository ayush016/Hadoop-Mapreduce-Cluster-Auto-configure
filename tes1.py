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
   b1.setText("Push")
   b1.move(50,20)
   b2= QPushButton(win)
   b2.setText("next")
   b2.move(50,60)
   b1.clicked.connect(b1_clicked)
   b2.clicked.connect(forward)

   win.setGeometry(100,100,200,100)
   win.setWindowTitle("Make Selected Ips datanode")
   win.show()
   sys.exit(app.exec_())

def b1_clicked():
	f = open('ex.txt','r')
	contents = f.readlines()
	f.close()
	#print contents
	#print type(contents)
	count = 0
	for i in contents:
		count = count + 1
		if(i=="<configuration>\n" or i=="<configuration>"):
			break
	#print count

	contents.insert(count+1, "<property>\n<name>dfs.data.dir</name>\n<value>/data</value>\n</property>\n")

	f = open('ex.txt','w')
	contents = "".join(contents)
	f.write(contents)
	f.close()
	
def forward():
	os.system("./message.py")
if __name__ == '__main__':
   window()
