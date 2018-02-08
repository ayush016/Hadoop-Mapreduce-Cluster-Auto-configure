#!/usr/bin/env python
from PyQt4 import QtGui
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import socket
import fcntl
import struct
import os
from subprocess import Popen, PIPE
def createIntroPage():
    page = QtGui.QWizardPage()
    page.setTitle("Introduction")

    label = QtGui.QLabel("Welcome to Hadoop Autmation software")
    label.setWordWrap(True)

    layout = QtGui.QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)

    return page


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, 
        struct.pack('256s', ifname[:15])
    )[20:24])
	
def showdialog():
   page = QtGui.QWizardPage()
   page.setTitle("This is your Ip :")
   

   #msg = QMessageBox()
   #msg.setIcon(QMessageBox.Information)
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
   #z=get_ip_address(k[0])
   #print k
   #msg.setText(z)
   #msg.setText(line[1])
   #msg.setInformativeText("This is additional information")
   #msg.setWindowTitle("MessageBox demo")
   #msg.setDetailedText("The details are as follows:")
   #msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   #msg.buttonClicked.connect(msgbtn)
	
   #retval = msg.exec_()
   #print "value of pressed message box button:", retval
   label = QtGui.QLabel(get_ip_address(k[0]))
   h = open("YourIp.txt","w")
   h.write(get_ip_address(k[0]))
   label.setWordWrap(True)

   layout = QtGui.QVBoxLayout()
   layout.addWidget(label)
   page.setLayout(layout)
   label = QtGui.QLabel("\nYou are all set Click next to select datanodes")
   label.setWordWrap(True)
   layout.addWidget(label)
   return page
   
def msgbtn(i):
   print "Button pressed is:",i.text()
   #return page

def MakeDatanode():
    page = QtGui.QWizardPage()
    page.setTitle("Select Datanodes")
    layout = QtGui.QVBoxLayout()
    x=open("datanodes.txt","r")
    line=x.readlines()
    
    index=0
    label = QtGui.QLabel("Your Selected Datanodes are :")
    label.setWordWrap(True)
    layout.addWidget(label)
    for i in line:
	    label = QtGui.QLabel(i)
	    label.setWordWrap(True)
	    layout.addWidget(label)
	    #print index
	    index=index+1
        
    page.setLayout(layout)
    
    #application = QtGui.QApplication(sys.argv)
    wizard.setWindowTitle("Automation")
    return page
    
def ConfigDatanode():
    page = QtGui.QWizardPage()
    page.setTitle("Configuration")

    label = QtGui.QLabel("Configuration in progress please wait")
    label.setWordWrap(True)

    layout = QtGui.QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)

    return page


def nextprint():
    if(wizard.currentPage().title()=="Select Datanodes"):
	os.system("python qlistwidget_selection_modes_job.py")
    	os.system("python qlistwidget_selection_modes.py")
    	pid=os.fork()
    	if(pid==0):
    		
        	os.system("python Startnew.py")
        quit()
        #MakeDatanode()
    if(wizard.currentPage().title()=="Configuration"): 
    	os.system("python SShconnecting.py")



app = QtGui.QApplication(sys.argv)

wizard = QtGui.QWizard()
wizard.addPage(createIntroPage())
wizard.addPage(showdialog())
wizard.button(QtGui.QWizard.NextButton).clicked.connect(nextprint)

    #wizard.addPage(qlistwidget_selection_modes.__init__(self))
wizard.addPage(MakeDatanode())
wizard.addPage(ConfigDatanode())
    
   
wizard.show()
wizard.next()
wizard.next()
    
    
sys.exit(wizard.exec_())
'''
    ex = combodemo()
    ex.show()
    sys.exit(app.exec_())
'''
    
