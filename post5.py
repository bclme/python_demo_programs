import sys
import time
from PyQt6.QtWidgets import QApplication,  QWidget, QPushButton, QProgressBar
from PyQt6.QtCore import Qt

TIME_LIMIT = 100

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.initUI()

    def initUI(self):

        self.progress = QProgressBar(self)
        self.progress.setGeometry(25, 35, 305, 20)
        self.progress.setMaximum(100)
        self.progress.setStyleSheet("QProgressBar::chunk "
                          "{"
                          "background-color: red;text-align: center"
                          "}")
        self.progress.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        pb3 = QPushButton('Process', self)
        pb3.setGeometry(50, 100, 250, 30)
        pb3.setStyleSheet('QPushButton {background-color: #2F569B; color: #d4d4d4;}')
        pb3.clicked.connect(self.onClick_pb3)

        self.setGeometry(25, 45, 350, 150)
        self.setWindowTitle('Post 5')
        self.show()
        
 
    def onClick_pb3(self):
 
       count = 0
       while count < TIME_LIMIT:
            count += 1
            time.sleep(0.01)
            self.progress.setValue(count)
                

def main():

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
