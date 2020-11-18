import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import QPoint
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.make_circle = QtWidgets.QPushButton(self.centralwidget)
        self.make_circle.setGeometry(QtCore.QRect(330, 500, 141, 41))
        self.make_circle.setObjectName("make_circle")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git и жёлтые окружности"))
        self.make_circle.setText(_translate("MainWindow", "Создать окружность"))


class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        qp.setBrush(self.get_random_qcolor())
        centre_x, centre_y = randint(0, self.width()), randint(0, self.height())
        diameter = randint(1, min(self.width(), self.height()) // 2)
        qp.drawEllipse(QPoint(centre_x, centre_y), diameter // 2, diameter // 2)

    def get_random_qcolor(self):
        return QColor(randint(0, 255), randint(0, 255), randint(0, 255))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yellow_circles = YellowCircles()
    yellow_circles.show()
    sys.exit(app.exec())
