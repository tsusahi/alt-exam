# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'information.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DInfo(object):
    def setupUi(self, DInfo):
        DInfo.setObjectName("DInfo")
        DInfo.resize(500, 300)
        DInfo.setMinimumSize(QtCore.QSize(500, 300))
        DInfo.setMaximumSize(QtCore.QSize(500, 300))
        DInfo.setStyleSheet("background-color: #fcfeff")
        self.textBrowser = QtWidgets.QTextBrowser(DInfo)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 480, 210))
        self.textBrowser.setStyleSheet("background-color: #fcfeff")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(DInfo)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 240, 160, 40))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(DInfo)
        QtCore.QMetaObject.connectSlotsByName(DInfo)

    def retranslateUi(self, DInfo):
        _translate = QtCore.QCoreApplication.translate
        DInfo.setWindowTitle(_translate("DInfo", "Information"))
        self.textBrowser.setHtml(_translate("DInfo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Студенты Санкт-Петербургского государственного электротехнического университета &quot;ЛЭТИ&quot; им. В.И. Ульянова (Ленина)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Банит Максим Сергеевич (ФКТИ, гр. 1305)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Смирнов Кирилл Владимирович (ФКТИ, гр. 1305)</p></body></html>"))
        self.pushButton_2.setText(_translate("DInfo", "OK"))
