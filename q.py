#!/usr/bin/python2
import os
import sys
x=0
while(x!=4):
	print "\t\t\t\tWelcome to the menu"
	print '''
	press 1 for date
	press 2 for calendar
	press 3 for ipconfigration
	press 4 for exit
	'''

	x=raw_input("Enter your choice\t")
	x = int(x)
	if x==1:
		y=os.system("date")
	elif x==2:
		y=os.system("cal")
	elif x==3:
		y=os.system("ifconfig")
	elif x!=4:
		print "Invalid input"
	x=raw_input("Enter to continue")
	x = int(x)
	z=os.system("clear")

