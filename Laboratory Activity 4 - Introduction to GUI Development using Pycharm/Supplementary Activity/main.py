import sys
from PyQt5.QtWidgets import QApplication
from registration import App  # Import the Registration class

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())
