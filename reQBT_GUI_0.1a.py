# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reQBT_GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(930, 570)

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        MainWindow.setFont(font)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.titleLabel = QtGui.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(370, 20, 181, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.titleLabel.setFont(font)
        self.titleLabel.setAcceptDrops(False)
        self.titleLabel.setAutoFillBackground(False)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))

        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 72, 337, 207))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))

        self.topLeftVerticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.topLeftVerticalLayout.setSpacing(15)
        self.topLeftVerticalLayout.setObjectName(_fromUtf8("topLeftVerticalLayout"))

        self.CaseLayout = QtGui.QHBoxLayout()
        self.CaseLayout.setObjectName(_fromUtf8("CaseLayout"))

        self.case_label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.case_label.setFont(font)
        self.case_label.setObjectName(_fromUtf8("case_label"))
        self.CaseLayout.addWidget(self.case_label)

        self.caseLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.caseLineEdit.setFont(font)
        self.caseLineEdit.setObjectName(_fromUtf8("caseLineEdit"))
        self.CaseLayout.addWidget(self.caseLineEdit)

        self.caseClearButton = QtGui.QPushButton(self.layoutWidget)
        self.caseClearButton.setFont(font)
        self.caseClearButton.setObjectName(_fromUtf8("caseClearButton"))
        self.CaseLayout.addWidget(self.caseClearButton)

        self.topLeftVerticalLayout.addLayout(self.CaseLayout)

        self.contributorsLayout = QtGui.QHBoxLayout()
        self.contributorsLayout.setContentsMargins(-1, -1, 82, -1)
        self.contributorsLayout.setSpacing(50)
        self.contributorsLayout.setObjectName(_fromUtf8("contributorsLayout"))

        self.contributors_label = QtGui.QLabel(self.layoutWidget)
        self.contributors_label.setFont(font)
        self.contributors_label.setObjectName(_fromUtf8("contributors_label"))
        self.contributorsLayout.addWidget(self.contributors_label)

        self.contributorSpinBox = QtGui.QSpinBox(self.layoutWidget)
        self.contributorSpinBox.setFont(font)
        self.contributorSpinBox.setMinimum(1)
        self.contributorSpinBox.setMaximum(3)
        self.contributorSpinBox.setObjectName(_fromUtf8("contributorSpinBox"))
        self.contributorsLayout.addWidget(self.contributorSpinBox)

        self.topLeftVerticalLayout.addLayout(self.contributorsLayout)

        self.deducibleLayout = QtGui.QHBoxLayout()
        self.deducibleLayout.setContentsMargins(-1, -1, 100, -1)
        self.deducibleLayout.setObjectName(_fromUtf8("deducibleLayout"))
        self.deducibleButton = QtGui.QRadioButton(self.layoutWidget)
        self.deducibleButton.setFont(font)
        self.deducibleButton.setCheckable(True)
        self.deducibleButton.setChecked(False)
        self.deducibleButton.setObjectName(_fromUtf8("deducibleButton"))
        self.deducibleLayout.addWidget(self.deducibleButton)

        self.nondeducibleButton = QtGui.QRadioButton(self.layoutWidget)
        self.nondeducibleButton.setFont(font)
        self.nondeducibleButton.setObjectName(_fromUtf8("nondeducibleButton"))
        self.deducibleLayout.addWidget(self.nondeducibleButton)

        self.topLeftVerticalLayout.addLayout(self.deducibleLayout)

        self.quantLayout = QtGui.QHBoxLayout()
        self.quantLayout.setContentsMargins(0, -1, 80, -1)
        self.quantLayout.setSpacing(6)
        self.quantLayout.setObjectName(_fromUtf8("quantLayout"))

        self.quantLabel = QtGui.QLabel(self.layoutWidget)
        self.quantLabel.setFont(font)
        self.quantLabel.setObjectName(_fromUtf8("quantLabel"))
        self.quantLayout.addWidget(self.quantLabel)

        self.quantLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.quantLineEdit.setFont(font)
        self.quantLineEdit.setObjectName(_fromUtf8("quantLineEdit"))
        self.quantLayout.addWidget(self.quantLineEdit)

        self.pmLabel = QtGui.QLabel(self.layoutWidget)
        self.pmLabel.setFont(font)
        self.pmLabel.setObjectName(_fromUtf8("pmLabel"))
        self.quantLayout.addWidget(self.pmLabel)

        self.quantClearButton = QtGui.QPushButton(self.layoutWidget)
        self.quantClearButton.setFont(font)
        self.quantClearButton.setObjectName(_fromUtf8("quantClearButton"))
        self.quantLayout.addWidget(self.quantClearButton)

        self.topLeftVerticalLayout.addLayout(self.quantLayout)

        self.PnLayout = QtGui.QHBoxLayout()
        self.PnLayout.setContentsMargins(-1, -1, 80, 7)
        self.PnLayout.setSpacing(50)
        self.PnLayout.setObjectName(_fromUtf8("PnLayout"))

        self.PnLabel = QtGui.QLabel(self.layoutWidget)
        self.PnLabel.setFont(font)
        self.PnLabel.setObjectName(_fromUtf8("PnLabel"))
        self.PnLayout.addWidget(self.PnLabel)

        self.PnSpinBox = QtGui.QSpinBox(self.layoutWidget)
        self.PnSpinBox.setFont(font)
        self.PnSpinBox.setMinimum(0)
        self.PnSpinBox.setMaximum(3)
        self.PnSpinBox.setObjectName(_fromUtf8("PnSpinBox"))
        self.PnLayout.addWidget(self.PnSpinBox)

        self.topLeftVerticalLayout.addLayout(self.PnLayout)

        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(440, 70, 400, 31))
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))

        self.REP_Layout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.REP_Layout.setMargin(5)
        self.REP_Layout.setSpacing(50)
        self.REP_Layout.setObjectName(_fromUtf8("REP_Layout"))

        self.REP1_Label = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.REP1_Label.setFont(font)
        self.REP1_Label.setObjectName(_fromUtf8("REP1_Label"))
        self.REP_Layout.addWidget(self.REP1_Label)

        self.REP2_Label = QtGui.QLabel(self.layoutWidget1)
        self.REP2_Label.setFont(font)
        self.REP2_Label.setObjectName(_fromUtf8("REP2_Label"))
        self.REP_Layout.addWidget(self.REP2_Label)

        self.REP3_Label = QtGui.QLabel(self.layoutWidget1)
        self.REP3_Label.setFont(font)
        self.REP3_Label.setObjectName(_fromUtf8("REP3_Label"))
        self.REP_Layout.addWidget(self.REP3_Label)

        self.Pn1_Label = QtGui.QLabel(self.layoutWidget1)
        self.Pn1_Label.setEnabled(True)
        self.Pn1_Label.setFont(font)
        self.Pn1_Label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Pn1_Label.setObjectName(_fromUtf8("Pn1_Label"))
        self.REP_Layout.addWidget(self.Pn1_Label)

        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(50, 450, 191, 71))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.buttonsLayout = QtGui.QVBoxLayout(self.layoutWidget2)
        self.buttonsLayout.setSpacing(15)
        self.buttonsLayout.setObjectName(_fromUtf8("buttonsLayout"))

        self.saveExcelButton = QtGui.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.saveExcelButton.setFont(font)
        self.saveExcelButton.setObjectName(_fromUtf8("saveExcelButton"))
        self.buttonsLayout.addWidget(self.saveExcelButton)

        self.LRButton = QtGui.QPushButton(self.layoutWidget2)
        self.LRButton.setFont(font)
        self.LRButton.setObjectName(_fromUtf8("LRButton"))
        self.buttonsLayout.addWidget(self.LRButton)

        self.TPOXREP1_ComboBox = QtGui.QComboBox(self.centralwidget)
        self.TPOXREP1_ComboBox.setGeometry(QtCore.QRect(440, 397, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TPOXREP1_ComboBox.setFont(font)
        self.TPOXREP1_ComboBox.setObjectName(_fromUtf8("TPOXREP1_ComboBox"))
        self.TPOXREP1_ComboBox.addItem(_fromUtf8(""))
        self.TPOXREP1_ComboBox.addItem(_fromUtf8(""))
        self.TPOXREP1_ComboBox.addItem(_fromUtf8(""))
        self.TPOXREP1_ComboBox.addItem(_fromUtf8(""))
        self.TPOXREP1_ComboBox.addItem(_fromUtf8(""))
        self.TPOXREP1_ComboBox.addItem(_fromUtf8(""))
        self.TPOXREP1_ComboBox.addItem(_fromUtf8(""))
        self.TPOXREP1_ComboBox.addItem(_fromUtf8(""))

        self.locusLabel = QtGui.QLabel(self.centralwidget)
        self.locusLabel.setGeometry(QtCore.QRect(365, 75, 48, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.locusLabel.setFont(font)
        self.locusLabel.setObjectName(_fromUtf8("locusLabel"))

        self.D7Label = QtGui.QLabel(self.centralwidget)
        self.D7Label.setGeometry(QtCore.QRect(365, 108, 23, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.D7Label.setFont(font)
        self.D7Label.setObjectName(_fromUtf8("D7Label"))

        self.CSFLabel = QtGui.QLabel(self.centralwidget)
        self.CSFLabel.setGeometry(QtCore.QRect(365, 139, 35, 19))
        self.CSFLabel.setFont(font)
        self.CSFLabel.setObjectName(_fromUtf8("CSFLabel"))

        self.D3Label = QtGui.QLabel(self.centralwidget)
        self.D3Label.setGeometry(QtCore.QRect(365, 170, 23, 19))
        self.D3Label.setFont(font)
        self.D3Label.setObjectName(_fromUtf8("D3Label"))

        self.THO1Label = QtGui.QLabel(self.centralwidget)
        self.THO1Label.setGeometry(QtCore.QRect(365, 201, 46, 19))
        self.THO1Label.setFont(font)
        self.THO1Label.setObjectName(_fromUtf8("THO1Label"))

        self.D13Label = QtGui.QLabel(self.centralwidget)
        self.D13Label.setGeometry(QtCore.QRect(365, 232, 31, 19))
        self.D13Label.setFont(font)
        self.D13Label.setObjectName(_fromUtf8("D13Label"))

        self.D16Label = QtGui.QLabel(self.centralwidget)
        self.D16Label.setGeometry(QtCore.QRect(365, 263, 28, 19))
        self.D16Label.setFont(font)
        self.D16Label.setObjectName(_fromUtf8("D16Label"))

        self.D2Label = QtGui.QLabel(self.centralwidget)
        self.D2Label.setGeometry(QtCore.QRect(365, 294, 23, 19))
        self.D2Label.setFont(font)
        self.D2Label.setObjectName(_fromUtf8("D2Label"))

        self.D19Label = QtGui.QLabel(self.centralwidget)
        self.D19Label.setGeometry(QtCore.QRect(365, 325, 31, 19))
        self.D19Label.setFont(font)
        self.D19Label.setObjectName(_fromUtf8("D19Label"))

        self.vWALabel = QtGui.QLabel(self.centralwidget)
        self.vWALabel.setGeometry(QtCore.QRect(365, 356, 36, 19))
        self.vWALabel.setFont(font)
        self.vWALabel.setObjectName(_fromUtf8("vWALabel"))

        self.TPOXLabel = QtGui.QLabel(self.centralwidget)
        self.TPOXLabel.setGeometry(QtCore.QRect(365, 387, 48, 19))
        self.TPOXLabel.setFont(font)
        self.TPOXLabel.setObjectName(_fromUtf8("TPOXLabel"))

        self.D18Label = QtGui.QLabel(self.centralwidget)
        self.D18Label.setGeometry(QtCore.QRect(365, 418, 31, 19))
        self.D18Label.setFont(font)
        self.D18Label.setObjectName(_fromUtf8("D18Label"))

        self.D5Label = QtGui.QLabel(self.centralwidget)
        self.D5Label.setGeometry(QtCore.QRect(365, 449, 23, 19))
        self.D5Label.setFont(font)
        self.D5Label.setObjectName(_fromUtf8("D5Label"))

        self.FGALabel = QtGui.QLabel(self.centralwidget)
        self.FGALabel.setGeometry(QtCore.QRect(365, 480, 37, 19))
        self.FGALabel.setFont(font)
        self.FGALabel.setObjectName(_fromUtf8("FGALabel"))

        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.titleLabel.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.TPOXREP1_ComboBox.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.menuFile = QtGui.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))

        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))

        self.menuRun = QtGui.QMenu(self.menubar)
        self.menuRun.setObjectName(_fromUtf8("menuRun"))

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))

        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))

        self.actionSave_Run_File = QtGui.QAction(MainWindow)
        self.actionSave_Run_File.setObjectName(_fromUtf8("actionSave_Run_File"))

        self.actionCheck_for_Errors = QtGui.QAction(MainWindow)
        self.actionCheck_for_Errors.setObjectName(_fromUtf8("actionCheck_for_Errors"))

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.menuRun.addAction(self.actionSave_Run_File)
        self.menuRun.addAction(self.actionCheck_for_Errors)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.quantClearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.quantLineEdit.clear)
        QtCore.QObject.connect(self.caseClearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.caseLineEdit.clear)
        QtCore.QObject.connect(self.PnSpinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Pn1_Label.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "reQBT", None))
        self.titleLabel.setText(_translate("MainWindow", "reQBT v2.0", None))
        self.case_label.setText(_translate("MainWindow", "Case: ", None))
        self.caseClearButton.setText(_translate("MainWindow", "Clear", None))
        self.contributors_label.setText(_translate("MainWindow", "Contributors:", None))
        self.deducibleButton.setText(_translate("MainWindow", "Deducible", None))
        self.nondeducibleButton.setText(_translate("MainWindow", "Non-Deducible", None))
        self.quantLabel.setText(_translate("MainWindow", "Quant:", None))
        self.pmLabel.setText(_translate("MainWindow", "pm", None))
        self.quantClearButton.setText(_translate("MainWindow", "Clear", None))
        self.PnLabel.setText(_translate("MainWindow", "Known Pn:", None))
        self.REP1_Label.setText(_translate("MainWindow", "REP 1", None))
        self.REP2_Label.setText(_translate("MainWindow", "REP 2", None))
        self.REP3_Label.setText(_translate("MainWindow", "REP 3", None))
        self.Pn1_Label.setText(_translate("MainWindow", "Pn1", None))
        self.saveExcelButton.setText(_translate("MainWindow", "Save as Excel File", None))
        self.LRButton.setText(_translate("MainWindow", "Calculate LR", None))

        self.TPOXREP1_ComboBox.setItemText(0, _translate("MainWindow", "6", None))
        self.TPOXREP1_ComboBox.setItemText(1, _translate("MainWindow", "7", None))
        self.TPOXREP1_ComboBox.setItemText(2, _translate("MainWindow", "8", None))
        self.TPOXREP1_ComboBox.setItemText(3, _translate("MainWindow", "9", None))
        self.TPOXREP1_ComboBox.setItemText(4, _translate("MainWindow", "10", None))
        self.TPOXREP1_ComboBox.setItemText(5, _translate("MainWindow", "11", None))
        self.TPOXREP1_ComboBox.setItemText(6, _translate("MainWindow", "12", None))
        self.TPOXREP1_ComboBox.setItemText(7, _translate("MainWindow", "13", None))

        self.locusLabel.setText(_translate("MainWindow", "Locus", None))
        self.D7Label.setText(_translate("MainWindow", "D7:", None))
        self.CSFLabel.setText(_translate("MainWindow", "CSF:", None))
        self.D3Label.setText(_translate("MainWindow", "D3:", None))
        self.THO1Label.setText(_translate("MainWindow", "THO1:", None))
        self.D13Label.setText(_translate("MainWindow", "D13:", None))
        self.D16Label.setText(_translate("MainWindow", "D16", None))
        self.D2Label.setText(_translate("MainWindow", "D2:", None))
        self.D19Label.setText(_translate("MainWindow", "D19:", None))
        self.vWALabel.setText(_translate("MainWindow", "vWA:", None))
        self.TPOXLabel.setText(_translate("MainWindow", "TPOX:", None))
        self.D18Label.setText(_translate("MainWindow", "D18:", None))
        self.D5Label.setText(_translate("MainWindow", "D5:", None))
        self.FGALabel.setText(_translate("MainWindow", "FGA:", None))

        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuRun.setTitle(_translate("MainWindow", "Run", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionSave_Run_File.setText(_translate("MainWindow", "Run File", None))
        self.actionCheck_for_Errors.setText(_translate("MainWindow", "Check for Errors", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

