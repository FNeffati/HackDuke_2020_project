# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hackduke2020qtdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.questionbox = QtWidgets.QTextEdit(self.centralwidget)
        self.questionbox.setGeometry(QtCore.QRect(400, 140, 104, 31))
        self.questionbox.setObjectName("questionbox")
        self.question = QtWidgets.QLabel(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(280, 120, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.question.setFont(font)
        self.question.setObjectName("question")
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(300, 210, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.answer.setFont(font)
        self.answer.setObjectName("answer")
        self.answerbox = QtWidgets.QTextEdit(self.centralwidget)
        self.answerbox.setGeometry(QtCore.QRect(400, 230, 104, 31))
        self.answerbox.setObjectName("answerbox")
        self.Done = QtWidgets.QPushButton(self.centralwidget)
        self.Done.setGeometry(QtCore.QRect(300, 310, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Done.setFont(font)
        self.Done.setObjectName("Done")
        self.question_2 = QtWidgets.QLabel(self.centralwidget)
        self.question_2.setGeometry(QtCore.QRect(180, 30, 491, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.question_2.setFont(font)
        self.question_2.setObjectName("question_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.question.setText(_translate("MainWindow", "Question:"))
        self.answer.setText(_translate("MainWindow", "Answer: "))
        self.Done.setText(_translate("MainWindow", "Done!"))
        self.question_2.setText(_translate("MainWindow", "COVID-19 Adverse Event Reporting Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

