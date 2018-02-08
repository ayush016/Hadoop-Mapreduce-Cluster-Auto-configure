import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os

class Form(QDialog):
   def __init__(self, parent=None):
      super(Form, self).__init__(parent)
      self.setGeometry(440, 200, 500, 350)	
      layout = QVBoxLayout()
      self.b1 = QPushButton("Select NameNode")
      self.b1.setCheckable(True)
      self.b1.toggle()
     
      #self.b1.clicked.connect(lambda:self.whichbtn(self.b1))
      self.b1.clicked.connect(self.btnstate)
      layout.addWidget(self.b1)
		
      self.setLayout(layout)
   
      self.b4 = QPushButton("Automatic Selection (Beta)")
      self.b4.setDefault(True)
      #self.b4.clicked.connect(lambda:self.whichbtn(self.b4))
      self.b4.clicked.connect(self.btnstate1)
      layout.addWidget(self.b4)
      
      self.setWindowTitle("Welcome to Client Gateway")

   def btnstate(self):
      os.system("python qlist_client.py")
      os.system("python qlist_client_job.py")
      
   def btnstate1(self):
      os.system("python autoconnector.py")
			
   def whichbtn(self,b):
      print "clicked button is "+b.text()

def main():
   app = QApplication(sys.argv)
   ex = Form()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
