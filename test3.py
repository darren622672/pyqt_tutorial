from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from time import time, sleep

# thread 
class MyThread(QThread):
    def __init__(self):
        QThread.__init__(self)
        # define your variables
        self.run_type = 0
        self.number = 0
    def run(self):
        for i in range(self.number):
            print('i:',i)
    
        

Ui_MainWindow, QtBaseClass = uic.loadUiType("test3.ui")

# window
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #define widgets
        self.mythread = MyThread()
        self.pb_st = self.findChild(QPushButton, 'pushButton_st')
        self.pb_quit = self.findChild(QPushButton, 'pushButton_quit')
        self.le_num = self.findChild(QLineEdit, 'lineEdit_num')
        self.mythread.number = int(self.le_num.text())
        
        
        self.pb_st.clicked.connect(self.show_text)
        self.pb_quit.clicked.connect(self.ui_quit)
        self.le_num.textChanged.connect(self.number_change)

    def show_text(self):
#        print("Hello world.")
#        sleep(5)
#        print("Hello Stampy")
        self.mythread.start()
    def number_change(self):
        number = int(self.le_num.text())
        self.mythread.number = number
        
    def ui_quit(self):
        self.mythread.terminate()
        self.close()
        
    
    
if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()   