import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from time import time, sleep

Ui_MainWindow, QtBaseClass = uic.loadUiType("test1.ui")

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #define widgets
        self.pb_st = self.findChild(QPushButton, 'pushButton_st')
        self.pb_quit = self.findChild(QPushButton, 'pushButton_quit')
        
        self.pb_st.clicked.connect(self.show_text)
        self.pb_quit.clicked.connect(self.ui_quit)

    def show_text(self):
        print("Hello world.")
        sleep(3)
        print("Hello Stampy.")
        
        
    def ui_quit(self):
        self.close()
        
    
    
if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()