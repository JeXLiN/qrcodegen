#!/usr/bin/env python3

from PySide2.QtWidgets import QApplication, QWidget, QFileDialog, QGraphicsScene
from PySide2.QtCore import QSize
from PySide2.QtGui import QPixmap
from qrcodegen_form import Ui_Form

import qrcode
from PIL.ImageQt import ImageQt
import sys, os


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("QR Code Generator")

        self.ui.graphicsView.setMinimumSize(QSize(284, 284))

        self.ui.openfileBtn.setText("Open File")
        self.ui.qrgenBtn.setText("Generate")
        self.ui.savefileBtn.setText("Save QR Code")
        self.ui.label.setText("Insert text:")

        self.ui.textEdit.textChanged.connect(self.textChanged)
        self.ui.openfileBtn.clicked.connect(self.openTextFile)
        self.ui.qrgenBtn.clicked.connect(self.generate)
        self.ui.savefileBtn.clicked.connect(self.saveQRCode)

        self.data = None
        self.img_file = None

        
    def openTextFile(self):
        filename = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);; All Files (*.*)")

        f = open(filename[0], 'r')
        self.data = f.read().rstrip()
        f.close()
        
    def saveQRCode(self):
        if self.img_file == None:
            return -1
        
        save_path = QFileDialog.getSaveFileName(self, "Save QR Code", "", "PNG Image (*.png)")
        self.img_file.save(save_path[0])


    def textChanged(self):
        self.data = self.ui.textEdit.toPlainText()
    
    def generate(self):
        if self.data == None:
            return -1
        
        scene = QGraphicsScene()
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            border=1
        )
        qr.add_data(self.data)
        qr.make()
        self.img_file = qr.make_image()
        qim = ImageQt(self.img_file)
        pixmap = QPixmap.fromImage(qim).scaled(256, 256)
        scene.addPixmap(pixmap)
        self.ui.graphicsView.setScene(scene)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qrgen = MainWindow()
    qrgen.show()
    sys.exit(app.exec_())
