# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets as qtw
import sys

class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = qtw.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = qtw.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 501, 481))
        self.groupBox.setObjectName("groupBox")
        self.dateEdit = qtw.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(139, 50, 341, 26))
        self.dateEdit.setObjectName("dateEdit")
        self.label_date = qtw.QLabel(self.groupBox)
        self.label_date.setGeometry(QtCore.QRect(40, 60, 67, 17))
        self.label_date.setObjectName("label_date")
        self.label_time = qtw.QLabel(self.groupBox)
        self.label_time.setGeometry(QtCore.QRect(40, 120, 67, 17))
        self.label_time.setObjectName("label_time")
        self.label_location = qtw.QLabel(self.groupBox)
        self.label_location.setGeometry(QtCore.QRect(40, 170, 67, 17))
        self.label_location.setObjectName("label_location")
        self.timeEdit = qtw.QTimeEdit(self.groupBox)
        self.timeEdit.setGeometry(QtCore.QRect(137, 120, 341, 26))
        self.timeEdit.setObjectName("timeEdit")
        self.lineEdit = qtw.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(142, 170, 331, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = qtw.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(43, 240, 431, 211))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = qtw.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = qtw.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_date.setText(_translate("MainWindow", "Date"))
        self.label_time.setText(_translate("MainWindow", "Time"))
        self.label_location.setText(_translate("MainWindow", "Location"))



class Main(qtw.QWidget, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		# add as any properties here...
		self.setWindowTitle('The title of main window')

if __name__ == "__main__":
  app = qtw.QApplication(sys.argv)

  main = Main()
  main.show()

  sys.exit(app.exec())