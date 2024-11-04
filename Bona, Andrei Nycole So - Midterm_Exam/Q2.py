import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Special Midterm Exam in OOP"
        self.x = 200
        self.y = 200
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        self.button = QPushButton('Click to Change Color', self)
        self.button.clicked.connect(self.action)
        self.button.move(145, 150)
        self.show()
    def action(self):
        self.button.setStyleSheet("background-color : yellow")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())