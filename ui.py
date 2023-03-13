# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtTest
from random import randint

# QtTest.QTest.qWait(msecs)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(448, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 50, 331, 171))
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 260, 89, 25)) # Values 170, 260, 89, 25
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.text = lambda: f"Hi I'm Qasatak. I am telling you the story of a red bottle. The red bottle's name was adventy" # The text that will be displayed on the white space on the UI. Basically the story
        self.pushButton.clicked.connect(lambda: self.wait_set_text(self.textEdit, self.text()))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", ""
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html>"
            "<head>"
            "<meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style>"
            "</head>"
            "<body style=\" font-family:\'Ubuntu\'; "
            "font-size:11pt; "
            "font-weight:400; "
            "font-style:normal;\">\n"
            "<p style=\"-qt-paragraph-type:empty; "
            "margin-top:0px; "
            "margin-bottom:0px; "
            "margin-left:0px; "
            "margin-right:0px; "
            "-qt-block-indent:0; "
            "text-indent:0px;\"><br /></p>"
            "</body>"
            "</html>"))
        self.pushButton.setText(_translate("MainWindow", "Start Story"))

        new_btn_len = (len(self.pushButton.text())*7)+10
        self.pushButton.setGeometry(QtCore.QRect(170-(new_btn_len-89)//2, 260, new_btn_len, 25))

    def wait_set_text(self, container, text):
        self.pushButton.setEnabled(False)
        x = ""
        for i in text:
            x += i
            container.setText(x)
            QtTest.QTest.qWait(randint(1000, 3000)//randint(20,70))
        self.pushButton.setEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
