#!/usr/bin/python2
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
import time
def window():
   app = QApplication(sys.argv)
   w = QWidget()
   #b = QPushButton(w)
   #b.setText("See")
   
   #b.move(120,100)
   #b.clicked.connect(showdialog)
   w.setWindowTitle("All connected Ips in the Network")
   #w.show()
   showdialog()
   sys.exit(app.exec_())
	
def showdialog():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Information)
 
   z="hi"
   msg.setText(z)
   #print dir(msg)
   showdialog2()
   #msg.buttonClicked.connect(msgbtn)
	
   msg.exec_()
   #print "value of pressed message box button:", retval
def showdialog2():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Information)
 
   z="hi2"
   msg.setText(z)
   #print dir(msg)
   #msg.buttonClicked.connect(msgbtn)=	
   retval = msg.exec_()
   
   
   #print "value of pressed message box button:", retval	
def msgbtn(i):
   print "Button pressed is:",i.text()
	
if __name__ == '__main__': 
   window()
   
