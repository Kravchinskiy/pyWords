# import pickle

#from PyQt5.QtCore import QFile, QIODevice, Qt, QTextStream
from PyQt5 import Qt
#from PyQt5 import QtGui
#from PyQt5.QtWidgets import (QDialog, QFileDialog, QGridLayout, QHBoxLayout,
#        QLabel, QLineEdit, QMessageBox, QPushButton, QTextEdit, QVBoxLayout,
#        QWidget)
from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QMessageBox, QWidget

from pyWords import ClWords

class QtDictionary(QWidget):

    def __init__(self, parent=None):
        super(QtDictionary, self).__init__(parent)

        self.__words = ClWords()
        self.__word, self.__answers = self.__words.getSet()
        # Output English Word
        self.lblWord = QLabel(self.__word)
        # define Translate buttons
        self.btnTrans1 = QPushButton(self.__answers[0])
        self.btnTrans1.setGeometry(300, 120, 320, 20)
        self.btnTrans1.show()
        self.btnTrans2 = QPushButton(self.__answers[1])
        self.btnTrans2.setGeometry(300, 120, 320, 20)
        self.btnTrans2.show()
        self.btnTrans3 = QPushButton(self.__answers[2])
        self.btnTrans3.setGeometry(300, 120, 320, 20)
        self.btnTrans3.show()
        self.btnTrans4 = QPushButton(self.__answers[3])
        self.btnTrans4.setGeometry(300, 120, 320, 20)
        self.btnTrans4.show()
        self.btnTrans5 = QPushButton(self.__answers[4])
        self.btnTrans5.setGeometry(300, 120, 320, 20)
        self.btnTrans5.show()
        self.btnTrans6 = QPushButton(self.__answers[5])
        self.btnTrans6.setGeometry(300, 120, 320, 20)
        self.btnTrans6.show()
        # Define Control buttons
        self.lblSpace = QLabel("")
        self.btnClose = QPushButton("&Закрыть")
        self.btnClose.setGeometry(300, 120, 320, 20)
        self.btnClose.show()
        self.btnNext = QPushButton("&Следующее")
        self.btnNext.setGeometry(300, 120, 320, 20)
        self.btnNext.show()
        # Connect event handle
        self.btnTrans1.clicked.connect(self.press_1)
        self.btnTrans2.clicked.connect(self.press_2)
        self.btnTrans3.clicked.connect(self.press_3)
        self.btnTrans4.clicked.connect(self.press_4)
        self.btnTrans5.clicked.connect(self.press_5)
        self.btnTrans6.clicked.connect(self.press_6)
        
        self.btnNext.clicked.connect(self.nextWord)
        self.btnClose.clicked.connect(self.closeApp)
        # contain to VBox
        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(self.btnTrans1)
        buttonLayout1.addWidget(self.btnTrans2)
        buttonLayout1.addWidget(self.btnTrans3)
        buttonLayout1.addWidget(self.btnTrans4)
        buttonLayout1.addWidget(self.btnTrans5)
        buttonLayout1.addWidget(self.btnTrans6)
        
        # contain to HBox
        buttonLayout2 = QHBoxLayout()
        buttonLayout2.addWidget(self.btnClose)
        buttonLayout2.addWidget(self.btnNext)
        # contain to Grid        
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.lblWord, 0, 0)
        mainLayout.addLayout(buttonLayout1, 1, 0)
        mainLayout.addWidget(self.lblSpace, 2, 0)
        mainLayout.addLayout(buttonLayout2, 3, 0)
        # Main Layout
        self.setLayout(mainLayout)
        self.setWindowTitle("Словарь 2019")
        self.resize(640, 800)

#-----------------------------------------------------------------------        
#   Show Message
#-----------------------------------------------------------------------        
    def showMsg(self, nBtn):
        # rule = self.__wordCount % 6
        idx = nBtn - 1
        if self.__words.checkTrans(self.__answers[idx]):
            self.__words.incCount()
            title = "Правильно"
            msg   = "Следующее слово."
        else:
            self.__words.decCount()
            title = "Неправильно"
            msg   = "Выбирете заново"
        QMessageBox.information(self, title, msg)
        return

#-----------------------------------------------------------------------        
#   Press Button 1
#-----------------------------------------------------------------------        
    def press_1(self):
        # self.showMsg(1)
        if self.__words.checkTrans(self.__answers[0]):
            self.nextWord()
        else:
            self.btnTrans1.setStyleSheet('color: #ff0000')
            font = Qt.QFont()
            font.setBold(True)
            self.btnTrans1.setFont(font)
        return

#-----------------------------------------------------------------------        
#   Press Button 2
#-----------------------------------------------------------------------        
    def press_2(self):
        # self.showMsg(2)
        if self.__words.checkTrans(self.__answers[1]):
            self.nextWord()
        else:
            self.btnTrans2.setStyleSheet('color: #ff0000')
            font = Qt.QFont()
            font.setBold(True)
            self.btnTrans2.setFont(font)
        return

#-----------------------------------------------------------------------        
#   Press Button 3
#-----------------------------------------------------------------------        
    def press_3(self):
        # self.showMsg(3)
        if self.__words.checkTrans(self.__answers[2]):
            self.nextWord()
        else:
            self.btnTrans3.setStyleSheet('color: #ff0000')
            font = Qt.QFont()
            font.setBold(True)
            self.btnTrans3.setFont(font)
        return

#-----------------------------------------------------------------------        
#   Press Button 4
#-----------------------------------------------------------------------        
    def press_4(self):
        # self.showMsg(4)
        if self.__words.checkTrans(self.__answers[3]):
            self.nextWord()
        else:
            self.btnTrans4.setStyleSheet('color: #ff0000')
            font = Qt.QFont()
            font.setBold(True)
            self.btnTrans4.setFont(font)
        return

#-----------------------------------------------------------------------        
#   Press Button 5
#-----------------------------------------------------------------------        
    def press_5(self):
        # self.showMsg(5)
        if self.__words.checkTrans(self.__answers[4]):
            self.nextWord()
        else:
            self.btnTrans5.setStyleSheet('color: #ff0000')
            font = Qt.QFont()
            font.setBold(True)
            self.btnTrans5.setFont(font)
        return

#-----------------------------------------------------------------------        
#   Press Button 6
#-----------------------------------------------------------------------        
    def press_6(self):
        #self.showMsg(6)
        if self.__words.checkTrans(self.__answers[5]):
            self.nextWord()
        else:
            self.btnTrans6.setStyleSheet('color: #ff0000')
            font = Qt.QFont()
            font.setBold(True)
            self.btnTrans6.setFont(font)
        return

#-----------------------------------------------------------------------        
#   Press Button Next
#-----------------------------------------------------------------------        
    def nextWord(self):
        # engWord = "Следующее слово " + str(self.incWordCount())
        self.__word, self.__answers = self.__words.getSet()
        font = Qt.QFont()
        font.setBold(False)
        self.lblWord.setText(self.__word)
        self.btnTrans1.setText(self.__answers[0])
        self.btnTrans1.setStyleSheet('color: #000000')
        self.btnTrans1.setFont(font)
        self.btnTrans2.setText(self.__answers[1])
        self.btnTrans2.setStyleSheet('color: #000000')
        self.btnTrans2.setFont(font)
        self.btnTrans3.setText(self.__answers[2])
        self.btnTrans3.setStyleSheet('color: #000000')
        self.btnTrans3.setFont(font)
        self.btnTrans4.setText(self.__answers[3])
        self.btnTrans4.setStyleSheet('color: #000000')
        self.btnTrans4.setFont(font)
        self.btnTrans5.setText(self.__answers[4])
        self.btnTrans5.setStyleSheet('color: #000000')
        self.btnTrans5.setFont(font)
        self.btnTrans6.setText(self.__answers[5])
        self.btnTrans6.setStyleSheet('color: #000000')
        self.btnTrans6.setFont(font)
        return

#-----------------------------------------------------------------------        
#   Press Button Close
#-----------------------------------------------------------------------        
    def closeApp(self):
        sys.exit(0)


#-----------------------------------------------------------------------        
#   Main Progaram (Starting Point)
#-----------------------------------------------------------------------        
if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    qtDictionary = QtDictionary()
    qtDictionary.show()

    sys.exit(app.exec_())
