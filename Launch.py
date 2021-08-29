from PyQt5 import QtWidgets, QtGui
from sys import argv, exit
from src.ui.CentralWidget import CentralWidget
from src.core.Database import AppDataBase
from src.ui.Authentication import Authentication
from src.core.Network import ApplicationNetwork
from src.core.Extensions import Extensions
from src.core.ThemeEngine import ThemeEngine


class Launcher(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWidget = CentralWidget(self)  # Central Widget
        self.setCentralWidget(self.mainWidget)
        self.initAppComponents()
        self.initUI()
        self.initStyles()

    def initAppComponents(self):
        appDataBase = AppDataBase()
        # auth = Authentication(self)
        appNetworkManager = ApplicationNetwork()
        extensionManager = Extensions()
        themeEngine = ThemeEngine(self)
        themeEngine.initTheme()

    def initUI(self):
        self.setWindowTitle('LetsTalk')
        self.setWindowIcon(QtGui.QIcon('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/Company-logo.png'))
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

