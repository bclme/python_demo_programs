import sys
from PyQt6.QtWidgets import QApplication,  QWidget,  QLabel
from PyQt6.QtGui import   QFont
from PyQt6.QtCore import Qt

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.initUI()

    def initUI(self):

        lbl1a =  QLabel('RECS', self)
        lbl1a.setGeometry(25, 10, 50, 35)
        lbl1a.setStyleSheet('QLabel {background-color: #0E95A6; color: #d4d4d4;}')
        lbl1a.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        lbl17 =  QLabel('24Hr Air Quality', self)
        lbl17.setGeometry(25, 55, 150, 35)
        
        lbl19 =  QLabel('Air Quality Analysis Dash Board', self)
        lbl19.setFont(QFont("Arial", 18))
        lbl19.setGeometry(25, 100, 350, 40)

        self.setGeometry(25, 45, 380, 150)
        self.setWindowTitle('Post 2')
        self.show()
        
  
def main():

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
