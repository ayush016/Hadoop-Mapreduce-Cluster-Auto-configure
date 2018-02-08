# coding=utf-8

# imports the sys module
import sys  # provides interaction with the Python interpreter

# imports the necessary Qt modules
from PyQt4 import QtGui  # provides the graphic elements
from PyQt4.QtCore import pyqtSlot  # provides the 'pyqtSlot()' decorator


# the 'Window' class inherits from the 'QWidget' class
class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # button names
        button_names = [
            u'Button A',
            u'Button B',
            u'Button C',
            u'Button D',
            u'Button E',
            u'Button F'
        ]

        # creates the buttons
        self.buttons = {}
        for name in button_names:
            button = QtGui.QPushButton(name)
            button.clicked.connect(self.button_clicked)  # connects the 'clicked()' signal with the 'button_clicked()' slot
            self.buttons[name] = button

        # creates a vertical box layout for the window
        vlayout = QtGui.QVBoxLayout()

        # adds each button to the layout
        for button in button_names:
            vlayout.addWidget(self.buttons[button])

        self.setLayout(vlayout)  # sets the window layout

    # 'button_clicked()' slot
    @pyqtSlot()
    def button_clicked(self):
        """ Prints the text of the button clicked """

        # the 'sender()' method returns the object that emits the signal
        if self.sender() is self.buttons[u'Button A']:
            print u'button A clicked'
        elif self.sender() is self.buttons[u'Button B']:
            print u'button B clicked'
        elif self.sender() is self.buttons[u'Button C']:
            print u'button C clicked'
        elif self.sender() is self.buttons[u'Button D']:
            print u'button D clicked'
        elif self.sender() is self.buttons[u'Button E']:
            print u'button E clicked'
        elif self.sender() is self.buttons[u'Button F']:
            print u'button F clicked'
        else:
            print u'other button clicked'


# creates the application and takes arguments from the command line
application = QtGui.QApplication(sys.argv)

# creates the window and sets its properties
window = Window()
window.setWindowTitle(u'Multiple buttons')  # title
window.resize(300, 200)  # size
window.show()  # shows the window

# runs the application and waits for its return value at the end
sys.exit(application.exec_())
