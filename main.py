import sys
from random import randint

from ui_file import Ui_MainWindow
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        pen.setColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))  # лимонный цвет
        painter.setPen(pen)
        painter.drawEllipse(x, y, d, d)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
