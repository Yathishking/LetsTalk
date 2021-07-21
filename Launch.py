from PyQt5 import QtWidgets
from sys import argv, exit
from src.ui.CentralWidget import CentralWidget


class Launcher(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWidget = CentralWidget(self)  # Central Widget
        self.setCentralWidget(self.mainWidget)
        self.initUI()
        self.initStyles()

    def initUI(self):
        self.setWindowTitle('LetsTalk')
        self.setGeometry(0, 0, 1366, 720)
        self.show()

    def initStyles(self):
        self.setStyleSheet("""
            background-color: #212121;
            color: whitesmoke;
        """)


def main():
    application = QtWidgets.QApplication(argv)
    exe = Launcher()
    exit(application.exec_())


if __name__ == "__main__":
    main()

