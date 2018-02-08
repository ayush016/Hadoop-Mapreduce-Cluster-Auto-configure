#!/usr/bin/env python
from PyQt4 import QtGui
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import socket
import fcntl
import struct
import os
import time
from subprocess import Popen, PIPE
import threading


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(440, 200, 500, 350)
        self.setWindowTitle("Setting Up")
        self.setWindowIcon(QtGui.QIcon('splash_loading.png'))
	
        extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
	

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        

        self.home()

    def home(self):
        

        extractAction = QtGui.QAction(QtGui.QIcon(), '   *****************************************************************\nPlease be patient\n we are getting things ready for you\nMapping all the networks', self)

        
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(150, 130, 250, 50)

        

        self.show()


    def download(self):
    	time.sleep(1)
        
        #print k
        #print os.system("ps aux|grep 11212")
        self.completed = 0
	k=1
        while self.completed < 100:
            
            while(k==1):
        	k=int(sum(1 for line in open('Ischild.txt')))
            	self.completed += 0.00001
        	self.progress.setValue(self.completed)
        	#print k
            #print k
            self.completed += 0.0001
            self.progress.setValue(self.completed)
        
        self.close()

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)
        


    




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
   layout = QtGui.QVBoxLayout()

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
   #label = QtGui.QLabel("Please wait you will be redirected.........")
   #label.setWordWrap(True)
   #layout.addWidget(label)
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
   
   
   #os.system("python message.py")
   
   layout = QtGui.QVBoxLayout()
   layout.addWidget(label)
   page.setLayout(layout)
   label = QtGui.QLabel("\nPlease wait for few seconds we are setting you up")
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
    label = QtGui.QLabel("Your Selected Datanodes are :\n")
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
    
def nextprint():
    if(wizard.currentPage().title()=="Select Datanodes"):
	os.system("python qlistwidget_selection_modes_job.py")
    	os.system("python qlistwidget_selection_modes.py")
    	
    	pid=os.fork()
    	
    	if(pid==0):
    		
        	os.system("python Startnew.py")
        quit()
        #MakeDatanode()
     
   
    #print wizard.currentPage().title()    	 

def commitprint():
    print("Action: commit Page: " + wizard.currentPage().title())
    label = QtGui.QLabel("\ntestetetet")
    label.setWordWrap(True)
    layout.addWidget(label)


 

	
		
	
ppid=os.fork()
if(ppid==0):
	f=open("Ischild.txt","w")
	
	#x = (str)(os.getpid())
	f.write("1\n")
	f.close()
	#print type(x)
	cpid=os.fork()
	if(cpid==0):
		os.system("python MakeNamenode.py")
	else:
		os.system("python message.py")
	quit()
else:
	#os.system("python message.py")
	
	app = QtGui.QApplication(sys.argv)
	wizard = QtGui.QWizard()
	wizard.addPage(createIntroPage())
	
	wizard.addPage(showdialog())
	wizard.button(QtGui.QWizard.NextButton).clicked.connect(nextprint)
	#wizard.button(QtGui.QWizard.CommitButton).clicked.connect(commitprint)
	#wizard.addPage(qlistwidget_selection_modes.__init__(self))
	wizard.addPage(MakeDatanode())
	GUI = Window()
	GUI.download() 
	#print dir(wizard)
	#print dir(wizard)
	wizard.show()
	#if(wizard.currentPage().title()=="Introduction"): 
	sys.exit(wizard.exec_())
'''
    ex = combodemo()
    ex.show()
    sys.exit(app.exec_())
'''
    
