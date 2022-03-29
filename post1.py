import sys
import os
from PyQt6.QtWidgets import QApplication,  QWidget, QPushButton

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.initUI()

    def initUI(self):

        pb1 = QPushButton('Exit', self)
        pb1.setGeometry(50, 20, 250, 30)
        pb1.setStyleSheet('QPushButton {background-color: #2F569B; color: #d4d4d4;}')
        pb1.clicked.connect(onClick_pb1)
        
        pb2 = QPushButton('Click Me!', self)
        pb2.setGeometry(50, 60, 250, 30)
        pb2.setStyleSheet('QPushButton {background-color: #2F569B; color: #d4d4d4;}')
        pb2.clicked.connect(self.onClick_pb2)
        
        pb3 = QPushButton('Open Notepad', self)
        pb3.setGeometry(50, 100, 250, 30)
        pb3.setStyleSheet('QPushButton {background-color: #2F569B; color: #d4d4d4;}')
        pb3.clicked.connect(onClick_pb3)

        self.setGeometry(25, 45, 350, 150)
        self.setWindowTitle('Post 1')
        self.show()
        
 
    def onClick_pb2(self):
 
       print("clicked")
       
 
        
def onClick_pb3():
    os.popen(r"C:\WINDOWS\system32\notepad.exe")


    
def onClick_pb1():
    exit()

def main():

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
