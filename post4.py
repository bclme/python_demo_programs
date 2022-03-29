import sys
from PyQt6.QtWidgets import QApplication,  QWidget,  QTableWidget
from PyQt6.QtGui import  QPainter, QColor, QPen
from PyQt6.QtCore import Qt

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.initUI()

    def initUI(self):


        self.setGeometry(25, 45, 330, 325)
        self.setWindowTitle('Post 4')
        self.createTable()
        self.show()
        
 
    def createTable(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(24)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setFixedSize(280, 275)
        self.tableWidget.move(25, 25)
        self.tableWidget.setHorizontalHeaderLabels(['PM2.5', 'PM10'])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

    
    

 
def main():

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
