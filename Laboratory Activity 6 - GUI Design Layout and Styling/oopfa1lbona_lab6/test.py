import sys
import math
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QGridLayout,
    QWidget, QAction, QLineEdit, QPushButton, QMessageBox,
    QFileDialog, QFontDialog, QGroupBox
)
from PyQt5.QtGui import QIcon


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon('pythonico.ico'))
        self.setGeometry(100, 100, 300, 400)

        self.entry = QLineEdit(self)
        self.entry.setReadOnly(True)
        self.entry.setFixedHeight(40)

        self.initUI()
        self.loadmenu()
        self.show()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.entry)

        # Create grid layout for calculator buttons
        grid = QGridLayout()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('exp', 5, 2), ('C', 5, 3)
        ]

        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.clicked.connect(lambda _, t=text: self.on_button_click(t))
            grid.addWidget(button, row, col)

        main_layout.addLayout(grid)
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def loadmenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')

        saveAction = QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.save_to_file)
        fileMenu.addAction(saveAction)

        openAction = QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.open_file)
        fileMenu.addAction(openAction)

        clearAction = QAction('Clear', self)
        clearAction.setShortcut('Ctrl+C')
        clearAction.triggered.connect(self.clear_entry)
        editMenu.addAction(clearAction)

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

    def on_button_click(self, char):
        if char == '=':
            self.calculate_result()
        elif char == 'C':
            self.clear_entry()
        else:
            current_text = self.entry.text()
            self.entry.setText(current_text + char)

    def calculate_result(self):
        try:
            expression = self.entry.text()
            result = self.evaluate_expression(expression)
            self.entry.setText(str(result))
            self.save_operation(f"{expression} = {result}")
        except Exception as e:
            self.show_error("Invalid input")

    def evaluate_expression(self, expression):
        if expression.startswith('sin'):
            value = float(expression[3:])
            return math.sin(math.radians(value))  # Convert to radians
        elif expression.startswith('cos'):
            value = float(expression[3:])
            return math.cos(math.radians(value))  # Convert to radians
        elif expression.startswith('exp'):
            value = float(expression[3:])
            return math.exp(value)
        else:
            return eval(expression)

    def clear_entry(self):
        self.entry.clear()

    def save_operation(self, operation):
        with open("calculations.txt", "a") as file:
            file.write(operation + "\n")

    def save_to_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save calculator file", "",
                                                   "Text Files (*.txt);;All files (*)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.entry.text())

    def open_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open calculator file", "",
                                                  "Text Files (*.txt);;All files (*)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                data = file.read()
                self.entry.setText(data)

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec_())
