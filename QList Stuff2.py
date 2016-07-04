from PyQt4 import QtGui, QtCore, uic
import sys


class reQBTListModel(QtCore.QAbstractListModel):

    def __init__(self, alleles = [], parent = None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.__alleles = alleles



    def headerData(self, section, orientation, role):

        if role == QtCore.Qt.DisplayRole:

            if orientation == QtCore.Qt.Horizontal:
                return "Palette"
            else:
                return "Color " + str(section + 1)


    def rowCount(self, parent):
        return len(self.__alleles)


    def data(self, index, role):


        if role == QtCore.Qt.EditRole:
            return self.__alleles[index.row()].name()


        if role == QtCore.Qt.ToolTipRole:
            return "Hex code: " + self.__alleles[index.row()].name()



        if role == QtCore.Qt.DisplayRole:

            row = index.row()
            value = self.__alleles[row]

            return value.name()



    def flags(self, index):
        return QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled



    def setData(self, index, value, role = QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:

            row = index.row()
            color = QtGui.QColor(value)

            if color.isValid():
                self.__alleles[row] = color
                self.dataChanged.emit(index, index)
                return True
        return False


    #=====================================================#
    #INSERTING & REMOVING
    #=====================================================#
    def insertRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginInsertRows(parent, position, position + rows - 1)

        for i in range(rows):
            self.__alleles.insert(position, QtGui.QColor("#000000"))

        self.endInsertRows()

        return True



    def removeRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginRemoveRows(parent, position, position + rows - 1)

        for i in range(rows):
            value = self.__alleles[position]
            self.__alleles.remove(value)

        self.endRemoveRows()
        return True






if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    app.setStyle("plastique")



    comboBox = QtGui.QComboBox()
    comboBox.show()



    red   = QtGui.QColor(255,0,0)
    green = QtGui.QColor(0,255,0)
    blue  = QtGui.QColor(0,0,255)



    rowCount = 4
    columnCount = 6



    model = reQBTListModel([red, green, blue])
    model.insertRows(0, 5)


    comboBox.setModel(model)



    sys.exit(app.exec_())