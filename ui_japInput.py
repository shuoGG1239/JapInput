# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_japInput.ui'
#
# Created: Sun Jan 27 22:43:34 2019
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import listWidget
import lineEdit

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(382, 307)
        self.lineEdit = lineEdit.LineEdit(widget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 321, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget = listWidget.ListWidget(widget)
        self.listWidget.setGeometry(QtCore.QRect(10, 90, 321, 191))
        self.listWidget.setObjectName("listWidget")
        self.btnMin = QtWidgets.QPushButton(widget)
        self.btnMin.setGeometry(QtCore.QRect(280, 10, 31, 23))
        self.btnMin.setObjectName("btnMin")
        self.btnClose = QtWidgets.QPushButton(widget)
        self.btnClose.setGeometry(QtCore.QRect(320, 10, 31, 23))
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.btnMin.setText(_translate("widget", "+"))
        self.btnClose.setText(_translate("widget", "×"))

