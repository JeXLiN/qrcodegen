# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qrcodegen_form.ui',
# licensing of 'qrcodegen_form.ui' applies.
#
# Created: Sat Nov  2 00:35:40 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.openfileBtn = QtWidgets.QPushButton(Form)
        self.openfileBtn.setObjectName("openfileBtn")
        self.horizontalLayout_5.addWidget(self.openfileBtn)
        self.qrgenBtn = QtWidgets.QPushButton(Form)
        self.qrgenBtn.setObjectName("qrgenBtn")
        self.horizontalLayout_5.addWidget(self.qrgenBtn)
        self.savefileBtn = QtWidgets.QPushButton(Form)
        self.savefileBtn.setObjectName("savefileBtn")
        self.horizontalLayout_5.addWidget(self.savefileBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "TextLabel", None, -1))
        self.openfileBtn.setText(QtWidgets.QApplication.translate("Form", "PushButton", None, -1))
        self.qrgenBtn.setText(QtWidgets.QApplication.translate("Form", "PushButton", None, -1))
        self.savefileBtn.setText(QtWidgets.QApplication.translate("Form", "PushButton", None, -1))

