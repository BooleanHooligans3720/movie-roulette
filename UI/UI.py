import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPainter, QPen, QPixmap, QBrush


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movie Roullette")
        self.setGeometry(300, 200, 860, 540)
        self.canvas = QPixmap(860, 540)
        self.label = QLabel()
        self.canvas.fill(Qt.GlobalColor.transparent)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)
        self.draw_something()
        
    def draw_something(self):
        painter = QPainter(self.canvas)
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor("#003D82"))
        painter.setPen(pen)
        brush = QBrush()
        brush.setColor(QColor("#003D82"))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(0, 0, 860, 540)
        pen.setColor(QColor("#0C53A6"))
        brush.setColor(QColor("#0C53A6"))
        painter.setBrush(brush)
        painter.setPen(pen)
        painter.drawRoundedRect(120, 0, 750, 120, 0, 0)
        painter.drawRoundedRect(0, 120, 120, 540, 0, 0)
        pen.setColor(QColor("#2B6ABC"))
        brush.setColor(QColor("#2B6ABC"))
        painter.setBrush(brush)
        painter.setPen(pen)
        painter.drawRoundedRect(0, 0, 120, 120, 0, 0)
        painter.end()
        self.label.setPixmap(self.canvas)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()