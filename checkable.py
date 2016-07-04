__author__ = 'Daniel'
from PyQt4 import QtGui, QtCore
import sys, os

class CheckableComboBox(QtGui.QComboBox):
    def __init__(self, parent = None):
        super(CheckableComboBox, self).__init__()
        self.view().pressed.connect(self.handleItemPressed)
        self.setModel(QtGui.QStandardItemModel(self))

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
            self.showPopup()

        else:
            item.setCheckState(QtCore.Qt.Checked)
            self.showPopup()