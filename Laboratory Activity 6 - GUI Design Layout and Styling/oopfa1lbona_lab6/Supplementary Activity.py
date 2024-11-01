import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QGridLayout, QWidget, QAction, QFileDialog, QMessageBox
from PyQt5.QtCore import *

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.textLine = QLineEdit(self)
        self.textLine.setReadOnly(True)
        self.textLine.setAlignment(Qt.AlignRight)
        self.textLine.setFixedHeight(40)

        self.loadmenu()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(grid)

        # Add the display area for the calculator
        grid.addWidget(self.textLine, 0, 0, 1, 5)

        # Button names and layout
        names = ['7', '8', '9', '/', '',
                 '4', '5', '6', '*', '',
                 '1', '2', '3', '-', '',
                 '0', '.', '=', '+', '',
                 'sin', 'cos', 'exp', 'clear', '']

        # Using a loop to generate positions and button connections
        positions = [(i, j) for i in range(1, 7) for j in range(5)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(self.create_button_handler(name))
            grid.addWidget(button, *position)

    def create_button_handler(self, char):
        def handler():
            self.on_button_click(char)
        return handler

    def loadmenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')

        editButton = QAction('Clear', self)
        editButton.setShortcut('Ctrl+M')
        editButton.triggered.connect(self.cleartext)
        editMenu.addAction(editButton)

        saveButton = QAction('Save', self)
        saveButton.setShortcut('Ctrl+S')
        saveButton.triggered.connect(self.saveFileDialog)
        fileMenu.addAction(saveButton)

        openButton = QAction('Open', self)
        openButton.setShortcut('Ctrl+O')
        openButton.triggered.connect(self.openFileNameDialog)
        fileMenu.addAction(openButton)

        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit Application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

    def cleartext(self):
        self.textLine.clear()

    def on_button_click(self, char):
        if char == '=':
            self.calculate_result()
        elif char == 'clear':
            self.cleartext()
        else:
            current_text = self.textLine.text()
            self.textLine.setText(current_text + char)

    def calculate_result(self):
        try:
            expression = self.textLine.text()
            result = self.evaluate_expression(expression)
            self.textLine.setText(str(result))
        except Exception:
            self.show_error("Invalid input")

    def evaluate_expression(self, expression):
        if expression.startswith('sin'):
            value = float(expression[3:])
            return math.sin(math.radians(value))
        elif expression.startswith('cos'):
            value = float(expression[3:])
            return math.cos(math.radians(value))
        elif expression.startswith('exp'):
            value = float(expression[3:])
            return math.exp(value)
        else:
            return eval(expression)

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save calculations file", "",
                                                   "Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.textLine.text())

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open notepad file", "",
                                                   "Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                data = file.read()
                self.textLine.setText(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
