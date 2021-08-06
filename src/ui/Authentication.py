from PyQt5 import QtWidgets, QtCore, QtGui


class Authentication(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.companyLogo = QtWidgets.QLabel()
        self.companyLogo.setPixmap(QtGui.QPixmap('/home/yathish/Desktop/'
                                                 'LetsTalk/LetsTalk/assets/images/Company-logo.png'))
        self.phone_number = QtWidgets.QLineEdit()
        self.phone_number.setPlaceholderText('Phone Number')
        self.username = QtWidgets.QLineEdit()
        self.username.setPlaceholderText('Username')
        self.otptext = QtWidgets.QLineEdit()
        self.otptext.setPlaceholderText('OTP')
        self.loginButton = QtWidgets.QPushButton('Login')
        self.closeButton = QtWidgets.QPushButton('Close')
        self.otpbutton = QtWidgets.QPushButton('Send a OTP')
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.initUI()
        self.initLayout()
        self.initStyles()
        self.signalLinker()
        self.exec_()

    def signalLinker(self):
        self.otpbutton.clicked.connect(self.updateLayout)
        self.loginButton.clicked.connect(self.closeDialog)
        self.closeButton.clicked.connect(self.rejectedCloseDialog)

    def initLayout(self):
        self.verticalLayout.addWidget(self.companyLogo, 4, QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.phone_number, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.otpbutton, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.closeButton, 0, QtCore.Qt.AlignBottom)
        self.setLayout(self.verticalLayout)

    def updateLayout(self):
        if self.phone_number.text() != '':
            self.verticalLayout.removeWidget(self.phone_number)
            self.phone_number.setParent(None)
            self.verticalLayout.removeWidget(self.otpbutton)
            self.otpbutton.setParent(None)
            self.verticalLayout.addWidget(self.username,  0, QtCore.Qt.AlignBottom)
            self.verticalLayout.addWidget(self.otptext, 0, QtCore.Qt.AlignBottom)
            self.verticalLayout.addWidget(self.loginButton, 0, QtCore.Qt.AlignBottom)
            self.verticalLayout.addWidget(self.closeButton, 0, QtCore.Qt.AlignBottom)
        return

    def initUI(self):
        self.setWindowTitle('Sign up')
        self.setGeometry(int(1136/2), int(768/4), 400, 400)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

    def initStyles(self):
        self.setStyleSheet("""
            QDialog{
                background: white;
                color: black;
            }
            QLineEdit{
                padding: 5px;
                border: none;
                border-bottom: 2px solid #212121;
                background: white;
                color: black;
            }
            QPushButton{
                padding: 5px;
                border: 1px solid whitesmoke;
                background: white;
                color: black;
            }
         """)

    def closeDialog(self):
        self.close()

    def rejectedCloseDialog(self):
        self.close()
        exit()

