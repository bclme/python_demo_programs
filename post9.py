import sys
import os
from PyQt6.QtWidgets import QApplication,  QWidget, QLineEdit, QLabel
from PyQt6 import QtCore, QtGui

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        
 
        
        self.initUI()

    def initUI(self):

        self.line_edit = QLineEdit('Enter Text Here', self)
        self.line_edit.setGeometry(25, 25, 150, 40)

        self.linelabel = QLabel('Entered Text Here', self)
        self.linelabel.setGeometry(25, 35, 180, 120)
        self.linelabel.setWordWrap(True)
        
        self.line_edit.returnPressed.connect(lambda: self.do_action())

        self.setGeometry(25, 45, 350, 150)
        self.setWindowTitle('Post 9')
        self.show()
        
 
    def do_action(self):

        value = self.line_edit.text()
        self.linelabel.setText(value)
       
 
        


def main():

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
