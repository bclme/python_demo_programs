import sys
from PyQt6.QtWidgets import QApplication,  QWidget,  QLabel
from PyQt6.QtGui import  QPainter, QColor, QPen
from PyQt6.QtCore import Qt

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.initUI()

    def initUI(self):


        self.setGeometry(25, 45, 640, 300)
        self.setWindowTitle('Post 3')
        self.show()
        
 
    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        
    
    
    def drawRectangles(self, qp):


        color = QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        qp.setBrush(QColor('#ffffff'))
        qp.drawRect(25, 25, 150, 30)

        pen = QPen()
        pen.setWidth(5)
        qp.setBrush(QColor('#00aa00'))
        qp.drawEllipse(25, 80, 300, 150)

        qp.setBrush(QColor('#d4d4d4'))
        qp.drawEllipse(40, 115, 270, 110)


        ii = 0
        while ii < 24:
            ii = ii + 1
            iii = (ii * 24) + 10
            qp.setBrush(QColor('#00aa00'))
            qp.drawRect(iii, 260, 22, 15)

 
def main():

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
