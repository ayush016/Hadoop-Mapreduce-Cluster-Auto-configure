import sys

from PyQt4 import QtGui
from PyQt4 import uic
from PyQt4.QtCore import pyqtSlot

base, form = uic.loadUiType('qlistwidget_selected_items.ui')  # loads the user interface


class Window(base, form):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)  # initializes the user interface

        # sets the selection mode
        self.listwidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

        # 'itemSelectionChanged()' signal
        self.listwidget.itemSelectionChanged.connect(self.selection_changed)

        # adds multiple items using a list comprehension
        strlist = ['Item {}'.format(i) for i in xrange(1, 11)]
        self.listwidget.addItems(strlist)

    # 'selection_changed()' slot
    @pyqtSlot()
    def selection_changed(self):
        # clears the output text
        self.edt_output.clear()

        # prints the text of the selected items on the QPlainTextEdit
        for item in self.listwidget.selectedItems():
            self.edt_output.appendPlainText(item.text())


# creates the application
application = QtGui.QApplication(sys.argv)

# creates the window
window = Window()
window.show()  # shows the window

# runs the application
sys.exit(application.exec_())
