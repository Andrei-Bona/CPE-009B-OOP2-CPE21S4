import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QFont

class App(QWidget):

    def __init__(self):
        super().__init__()  # Initializes the main window
        self.title = "Account Register System"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(200, 200, 400, 500)
        self.setWindowIcon(QIcon('pythonico.ico'))  # Sets an icon

        # Main Label
        self.MainLabel = QLabel('Account Register System', self)
        self.MainLabel.setFont(QFont('Times New Roman', 10))
        self.MainLabel.setStyleSheet("color: blue;")
        self.MainLabel.move(130, 20)

        # First Name
        self.firstname_label = QLabel('First Name: ', self)
        self.firstname_label.setFont(QFont('Times New Roman', 10))
        self.firstname_label.move(50, 70)
        self.firstname_input = QLineEdit(self)
        self.firstname_input.move(125, 55)
        self.firstname_input.resize(200, 40)

        # Last Name
        self.lastname_label = QLabel('Last Name: ', self)
        self.lastname_label.setFont(QFont('Times New Roman', 10))
        self.lastname_label.move(50, 120)
        self.lastname_input = QLineEdit(self)
        self.lastname_input.move(125, 105)
        self.lastname_input.resize(200, 40)

        # Username
        self.username_label = QLabel('Username: ', self)
        self.username_label.setFont(QFont('Times New Roman', 10))
        self.username_label.move(50, 170)
        self.username_input = QLineEdit(self)
        self.username_input.move(125, 155)
        self.username_input.resize(200, 40)

        # Password
        self.password_label = QLabel('Password: ', self)
        self.password_label.setFont(QFont('Times New Roman', 10))
        self.password_label.move(50, 220)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)  # Hide password input
        self.password_input.move(125, 205)
        self.password_input.resize(200, 40)

        # Email
        self.email_label = QLabel('Email Address: ', self)
        self.email_label.setFont(QFont('Times New Roman', 10))
        self.email_label.move(50, 270)
        self.email_input = QLineEdit(self)
        self.email_input.move(125, 255)
        self.email_input.resize(200, 40)

        # Contact Number
        self.con_number_label = QLabel('Contact\nNumber: ', self)
        self.con_number_label.setFont(QFont('Times New Roman', 10))
        self.con_number_label.move(50, 310)
        self.con_number_input = QLineEdit(self)
        self.con_number_input.move(125, 305)
        self.con_number_input.resize(200, 40)

        # Submit Button
        self.submit = QPushButton('Submit', self)
        self.submit.setToolTip("Done?")
        self.submit.move(125, 400)  # Button position
        self.submit.clicked.connect(self.submit_input)

        # Clear Button
        clear = QPushButton('Clear', self)
        clear.setToolTip("Reset?")
        clear.move(250, 400)  # Button position
        clear.clicked.connect(self.clear_input)

        self.show()

    def submit_input(self):
        first_name = self.firstname_input.text().strip()
        last_name = self.lastname_input.text().strip()
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        email = self.email_input.text().strip()
        contact_number = self.con_number_input.text().strip()

        # Check for empty fields
        if not all([first_name, last_name, username, password, email, contact_number]):
            QMessageBox.warning(self, "Missing Fields", "Please fill in all fields.", QMessageBox.Ok)
            return

        # Save to text file
        with open('accounts.txt', mode='a') as file:  # Append mode
            file.write(f"{first_name}, {last_name}, {username}, {password}, {email}, {contact_number}\n")

        QMessageBox.information(self, "Registration Successful", "Your account has been registered successfully!", QMessageBox.Ok)
        self.clear_input()  # Optionally clear inputs after successful registration

    def clear_input(self):
        self.firstname_input.clear()
        self.lastname_input.clear()
        self.username_input.clear()
        self.password_input.clear()
        self.email_input.clear()
        self.con_number_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
