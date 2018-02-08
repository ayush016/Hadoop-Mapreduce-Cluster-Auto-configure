import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
class combodemo(QWidget):
   def __init__(self, parent = None):
      super(combodemo, self).__init__(parent)
      
      layout = QHBoxLayout()
      self.cb = QComboBox()
      f=open("iplist.txt","r")
      os.system("rm -f datanodes.txt")
      os.system("touch datanodes.txt")
      line=f.readlines()
      for i in line:
      	self.cb.addItem(i)
      self.cb.currentIndexChanged.connect(self.selectionchange)
      
      
      layout.addWidget(self.cb)
      self.setLayout(layout)
      self.setWindowTitle("Select Nodes")

   def selectionchange(self,i):
      #print self.cb.currentText()
      g=open("datanodes.txt","a")
      g.write(self.cb.currentText())
      
      
     
      
	   	
def main():
   app = QApplication(sys.argv)
   ex = combodemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
