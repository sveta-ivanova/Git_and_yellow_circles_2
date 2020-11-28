import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Git и случайные окружности')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(10, 10)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp):
        x = randint(1, 350)
        y = randint(1, 350)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        w = randint(1, 120)
        qp.drawEllipse(x, y, w, w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
