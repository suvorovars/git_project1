import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # Загружаем дизайн

        self.pushButton.clicked.connect(self.circle)

        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)

    def circle(self):
        x, y = [randint(10, 500) for i in range(2)]
        d = randint(10, 100)
        # создаем экземпляр QPainter, передавая холст (self.label.pixmap())
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor('#fde910'))  # лимонный цвет
        painter.setPen(pen)
        painter.drawEllipse(x, y, d, d)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
