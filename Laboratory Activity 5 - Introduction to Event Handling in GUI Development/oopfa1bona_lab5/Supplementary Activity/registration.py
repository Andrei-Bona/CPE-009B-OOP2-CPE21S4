from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__() #initializes the main window like in the previous one
        #window = QMainWindow()
        self.title = "Account Register System"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(200,200,400,500)
        self.setWindowIcon(QIcon('pythonico.ico')) #sets an icon


        self.MainLabel = QLabel('Account Register System', self)
        self.MainLabel.setFont(QFont('Times New Roman', 10))
        self.MainLabel.setStyleSheet("color: blue;")
        self.MainLabel.move(130, 20)

        self.firstname = QLabel('First Name: ', self)
        self.firstname.setFont(QFont('Times New Roman', 10))
        self.firstname.move(50, 70)
        self.firstname = QLineEdit(self)
        self.firstname.move(125, 55)
        self.firstname.resize(200, 40)

        self.lastname = QLabel('Last Name: ', self)
        self.lastname.setFont(QFont('Times New Roman', 10))
        self.lastname.move(50, 120)
        self.lastname = QLineEdit(self)
        self.lastname.move(125, 105)
        self.lastname.resize(200, 40)

        self.username = QLabel('Username: ', self)
        self.username.setFont(QFont('Times New Roman', 10))
        self.username.move(50, 170)
        self.username = QLineEdit(self)
        self.username.move(125, 155)
        self.username.resize(200, 40)

        self.password = QLabel('Password: ', self)
        self.password.setFont(QFont('Times New Roman', 10))
        self.password.move(50, 220)
        self.password = QLineEdit(self)
        self.password.move(125, 205)
        self.password.resize(200, 40)

        self.email = QLabel('Email Address: ', self)
        self.email.setFont(QFont('Times New Roman', 10))
        self.email.move(50, 270)
        self.email = QLineEdit(self)
        self.email.move(125, 255)
        self.email.resize(200, 40)

        self.con_number = QLabel('Contact\nNumber: ', self)
        self.con_number.setFont(QFont('Times New Roman', 10))
        self.con_number.move(50, 310)
        self.con_number = QLineEdit(self)
        self.con_number.move(125, 305)
        self.con_number.resize(200, 40)


        self.submit = QPushButton('Submit', self)
        self.submit.setToolTip("Done?")
        self.submit.move(125, 400) # button.move(x,y)
        self.submit.clicked.connect(self.submit_input)


        clear = QPushButton('Clear', self)
        clear.setToolTip("Reset?")
        clear.move(250, 400) # button.move(x,y)
        clear.clicked.connect(self.clear_input)



        self.show()

    @pyqtSlot()
    def submit_input(self):
        first_name = self.firstname.text()
        last_name = self.lastname.text()
        username = self.username.text()
        password = self.password.text()
        email = self.email.text()
        contact_number = self.con_number.text()

        if not all([first_name, last_name, username, password, email, contact_number]):
            QMessageBox.warning(self, "Missing Inputs", "Please enter all information.", QMessageBox.Ok)
            return
        QMessageBox.information(self, "Submitted", "Successfully Submitted", QMessageBox.Ok)
        self.clear_input()
        message = f"Submitted:\nFirst Name: {first_name}\nLast Name: {last_name}\nUsername: {username}\nEmail: {email}\nContact Number: {contact_number}"

        t = TextFileReaderWrite()
        t.append(filepath="sample.txt", data=message)
        t.read("sample.txt")




    def clear_input(self):
        self.firstname.clear()
        self.lastname.clear()
        self.username.clear()
        self.password.clear()
        self.email.clear()
        self.con_number.clear()

