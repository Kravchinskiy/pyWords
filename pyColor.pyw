# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.Qt import QFont

import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Different Color")
window.resize(640, 400)
lblText = QtWidgets.QLabel("Name of text")
lblText.setStyleSheet('color: #ff0000')
font = QFont()
font.setBold(True)
lblText.setFont(font)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(lblText)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
