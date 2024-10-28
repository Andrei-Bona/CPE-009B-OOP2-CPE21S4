import sys
import math
from PyQt5.QtWidgets import *

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.entry = QLineEdit(self)

        self.loadmenu()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(grid)

        names = ['7', '8', '9', '/', '',
                 '4', '5', '6', '*', '',
                 '1', '2', '3', '-', '',
                 '0', '.', '=', '+', '',
                 'sin', 'cos', 'exp', 'clear','']
        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 0,1,1,5)

        # using a loop to generate positions
        positions = [(i, j) for i in range(1,7) for j in range(1,6)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

    def loadmenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')

        editButton = QAction('Clear', self)
        editButton.setShortcut('ctrl+M')
        editButton.triggered.connect(self.cleartext)
        editMenu.addAction(editButton)

        saveButton = QAction('Save', self)
        saveButton.setShortcut('ctrl+S')
        saveButton.triggered.connect(self.saveFileDialog)
        fileMenu.addAction(saveButton)

        openButton = QAction('Open', self)
        openButton.setShortcut('ctrl+O')
        openButton.triggered.connect(self.openFileNameDialog)
        fileMenu.addAction(openButton)

        exitButton = QAction('Exit', self)
        exitButton.setShortcut('ctrl+Q')
        exitButton.setStatusTip('Exit Application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

    def cleartext(self):
        self.notepad.text.clear()

    def on_button_click(self, char):
        if char == '=':
            self.calculate_result()
        elif char == 'C' or char == 'clear':
            self.entry.clear()
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
            return math.sin(value)
        elif expression.startswith('cos'):
            value = float(expression[3:])
            return math.cos(value)
        elif expression.startswith('exp'):
            value = float(expression[3:])
            return math.exp(value)
        else:
            return eval(expression)

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save calculations file", "",
                                                "Text Files (*.txt)", options = options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.notepad.text.toPlainText())

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open notepad file", "",
                                                  "Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                data = file.read()
                self.notepad.text.setText(data)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())