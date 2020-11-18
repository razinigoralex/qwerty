import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import QPoint
from PyQt5 import uic


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.make_circle.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        centre_x, centre_y = randint(0, self.width()), randint(0, self.height())
        diameter = randint(1, min(self.width(), self.height()) // 2)
        qp.drawEllipse(QPoint(centre_x, centre_y), diameter // 2, diameter // 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yellow_circles = YellowCircles()
    yellow_circles.show()
    sys.exit(app.exec())
