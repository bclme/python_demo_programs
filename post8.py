import sys
import numpy as np
from matplotlib.backends.qt_compat import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

def onclick(event):
    global clicks
    clicks.append(event.xdata)

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        
        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3), dpi=115))
        dynamic_canvas.setParent(self)
        dynamic_canvas.move(25,25)
        self._dynamic_ax = dynamic_canvas.figure.subplots()
        dynamic_canvas.figure.canvas.mpl_connect('button_press_event', onclick)
        self._dynamic_ax.grid()
        self._timer = dynamic_canvas.new_timer(
            100, [(self._update_window, (), {})])
        self._timer.start()

        button_stop = QtWidgets.QPushButton('Stop', self)
        button_stop.setGeometry(625, 95, 100, 40)
        button_stop.clicked.connect(self._timer.stop)

        button_start = QtWidgets.QPushButton('Start', self)
        button_start.setGeometry(625, 40, 100, 40)
        button_start.clicked.connect(self._timer.start)
 
        
        self.setGeometry(25, 45, 745, 400)
        self.setWindowTitle('Post 8')
        self.show()

    def _update_window(self):
        self._dynamic_ax.clear()
        global x, y1, y2, y3, N, count_iter, last_number_clicks
        x.append(x[count_iter] + 0.01)
        y1.append(np.random.random())
        idx_inf = max([count_iter-N, 0])
        if last_number_clicks < len(clicks):
            for new_click in clicks[last_number_clicks:(len(clicks))]:
                rowPosition = self.table_clicks.rowCount()
                self.table_clicks.insertRow(rowPosition)
                self.table_clicks.setItem(rowPosition,0, QtWidgets.QTableWidgetItem(str(new_click)))
                self.table_clicks.setItem(rowPosition,1, QtWidgets.QTableWidgetItem("Descripcion"))
            last_number_clicks = len(clicks)
        self._dynamic_ax.plot(x[idx_inf:count_iter], y1[idx_inf:count_iter],'-o', color='b')
        count_iter += 1
        self._dynamic_ax.figure.canvas.draw()
#%%
if __name__ == "__main__":
    pressed_key = {}
    clicks = []
    last_number_clicks = len(clicks)
    N = 25
    y1 = [np.random.random()]
    x = [0]
    count_iter = 0
    qapp = QtWidgets.QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    sys.exit(qapp.exec())
