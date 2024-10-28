import sys
import math
from PyQt5.QtWidgets import *

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.entry = QLineEdit(self)
        self.entry.setReadOnly(True)

        self.loadmenu()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.entry)

        grid = QGridLayout()

        names = [
            '7', '8', '9', '/', '',
            '4', '5', '6', '*', '',
            '1', '2', '3', '-', '',
            '0', '.', '=', '+', '',
            'sin', 'cos', 'exp', 'C', ''
        ]

        # Add the QLineEdit to the layout
        grid.addWidget(self.entry, 0, 0, 1, 5)

        # Using a loop to generate positions
        positions = [(i, j) for i in range(1, 6) for j in range(5)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(lambda _, t=name: self.on_button_click(t))
            grid.addWidget(button, *position)

        main_layout.addLayout(grid)
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def loadmenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')

        editButton = QAction('Clear', self)
        editButton.setShortcut('Ctrl+M')
        editButton.triggered.connect(self.clear_entry)
        editMenu.addAction(editButton)

        saveButton = QAction('Save', self)
        saveButton.setShortcut('Ctrl+S')
        saveButton.triggered.connect(self.save_to_file)
        fileMenu.addAction(saveButton)

        openButton = QAction('Open', self)
        openButton.setShortcut('Ctrl+O')
        openButton.triggered.connect(self.open_file)
        fileMenu.addAction(openButton)

        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

    def clear_entry(self):
        self.entry.clear()

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
        except Exception as e:
            self.show_error("Invalid input")

    def evaluate_expression(self, expression):
        # Handle trigonometric and exponential functions
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
            return eval(expression)  # Evaluate the expression

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
