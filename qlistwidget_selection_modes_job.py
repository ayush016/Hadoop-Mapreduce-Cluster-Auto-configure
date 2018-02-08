import sys
import os
from PyQt4 import QtGui
from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QAbstractItemView  
import time
base, form = uic.loadUiType('tester.ui') 


class Window(base, form):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)  

     
        self.group_modes = QtGui.QButtonGroup()

        # adds the QRadioButton widgets to the QButtonGroup container, and
        # sets a selection mode constant to each widget id
        self.group_modes.addButton(self.rb_single_selection,QAbstractItemView.SingleSelection)
        #self.group_modes.addButton(self.test)
        #self.group_modes.addButton(self.rb_extended_selection,QAbstractItemView.ExtendedSelection)
        #self.group_modes.addButton(self.rb_multi_selection,QAbstractItemView.MultiSelection)
        #self.group_modes.addButton(self.rb_no_selection,QAbstractItemView.NoSelection)

        # 'buttonClicked()' signal
        self.listwidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.group_modes.buttonClicked['int'].connect(self.test)
	

        f=open("iplist.txt","r")
        os.system("rm -f datanodes.txt")
        os.system("touch datanodes.txt")
        g=open("datanodes.txt","w")
        line=f.readlines()
        strlist = [format(i) for i in line]
        self.listwidget.addItems(strlist)
        #g.write(format(i))
        #self.QListWidget.currentRow(print_info())
        #[x.row() for x in self.listwidget.selectedIndexes()]
        #time.sleep(5)
        #y = self.listwidget.selectedIndexes()
        #print y
        #print dir(strlist)
	

    @pyqtSlot(int)
    def button_clicked(self, id_):

        self.listwidget.setSelectionMode(QAbstractItemView.MultiSelection)
    def print_info():
    	print myListWidget.currentRow()
    def test(self):
    	 y = [x.row() for x in self.listwidget.selectedIndexes()]
         print y
         p=open("iplist.txt","r")
         o=open("datanodes.txt","w")
         line=p.readlines()
         for k in y:
         	o.write(line[k])

application = QtGui.QApplication(sys.argv)


window = Window()
window.show() 

sys.exit(application.exec_())
