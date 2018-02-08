#!/usr/bin/python2
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
def window():
   app = QApplication(sys.argv)
   w = QWidget()
   #b = QPushButton(w)
   #b.setText("See")
   
   #b.move(120,100)
   #b.clicked.connect(showdialog)
   #w.setWindowTitle("Software is setting up please wait")
   #w.show()
   showdialog()
   sys.exit(app.exec_())
	
def showdialog():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Information)
   f=open("YourIp.txt","r")
   l=f.readlines()
   ipcount = []
   ic=0
   ipadd=""
   for o in l:
   	for w in o:
   		if(ic==3):
   			break
   		if(w=="."):
   			ic=ic+1	
   		ipadd = ipadd+w
   #print ipadd
   
   os.system("nmap -sP "+ipadd+"* -n  |grep "+ipadd+" > list.txt")
   p=open("Ischild.txt","a")
   p.write("2")
   f=open("list.txt","r")
   line = f.readlines()
   k=[]
   z=""
   count=0
   for i in line:
   	k.append(i)
   	k[count]=k[count].replace('Nmap scan report for ','')
   	count=count+1
   j = open("iplist.txt","w")
   count_new = 0
   for i in line:
   	j.write(k[count_new])
   	count_new = count_new + 1
   j.close()
   for i in k:
   	z=z+i
   
   #msg.setText(z)
   #msg.setText(line[1])
   #msg.setInformativeText("This is additional information")
   #msg.setWindowTitle("MessageBox demo")
   #msg.setDetailedText("The details are as follows:")
   #msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   #msg.buttonClicked.connect(msgbtn)
	
   #retval = msg.exec_()
   #print "value of pressed message box button:", retval
	
def msgbtn(i):
   print "Button pressed is:",i.text()
	
if __name__ == '__main__': 
   window()
   
