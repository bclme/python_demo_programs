import sys
from PyQt6.QtWidgets import QApplication,  QWidget,  QTableWidget, QStyledItemDelegate, QTableWidgetItem
from PyQt6.QtGui import  QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QEvent, QObject

class Delegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        if index.data() == "100":
            return super(Delegate, self).createEditor(parent, option, index)

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.initUI()

    def initUI(self):


        self.setGeometry(25, 45, 330, 325)
        self.setWindowTitle('Post 10')
        self.createTable()
        self.show()
        
 
    def createTable(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.viewport().installEventFilter(self)
        #self.tableWidget.installEventFilter(self)
        #self.tableWidget.setEditTriggers(QTreeView.NoEditTriggers) 
        self.tableWidget.setRowCount(24)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setFixedSize(280, 275)
        self.tableWidget.move(25, 25)
        delegate = Delegate(self.tableWidget)
        self.tableWidget.setItemDelegate(delegate)
        text = '100'
        it = QTableWidgetItem(text)
        self.tableWidget.setItem(3, 1, it)        
        self.tableWidget.setHorizontalHeaderLabels(['PM2.5', 'PM10'])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        
    def eventFilter(self, source, event):
        #if self.tableWidget.selectedIndexes() != []:
            
        if event.type() == QEvent.Type.MouseButtonRelease:
                #if event.button() == QtCore.Qt.LeftButton:
            row = self.tableWidget.currentRow()
            col = self.tableWidget.currentColumn()
            if self.tableWidget.item(row, col) is not None:
                print(str(row) + " " + str(col) + " " + self.tableWidget.item(row, col).text())
            else:
                print(str(row) + " " + str(col))            
                    #self.test.leftClick(row, col)
                #elif event.button() == QtCore.Qt.RightButton:

                 #   row = self.tableWidget.currentRow()
                 #   col = self.tableWidget.currentColumn()
                 #   self.test.rightClick(row, col)
       
        return QObject.event(source, event)
 
def main():

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()