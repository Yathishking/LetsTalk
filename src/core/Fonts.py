from PyQt5 import QtGui


class ButtonFont(QtGui.QFont):
    def __init__(self):
        super().__init__()
        self.setBold(True)
        self.setFamily('Helvetica')
        self.setPixelSize(14)


class MessageFont(QtGui.QFont):
    def __init__(self):
        super().__init__()
        self.setBold(False)
        self.setFamily('Poppins')
        self.setPixelSize(14)


class ContactNameFont(QtGui.QFont):
    def __init__(self):
        super().__init__()
        self.setBold(True)
        self.setFamily('Poppins')
        self.setPixelSize(16)


class ContactListFont(QtGui.QFont):
    def __init__(self):
        super().__init__()
        self.setBold(False)
        self.setFamily('Poppins')
        self.setPixelSize(14)


class Heading(QtGui.QFont):
    def __init__(self):
        super().__init__()
        self.setBold(True)
        self.setFamily('Poppins')
        self.setPixelSize(18)


class TimeFont(QtGui.QFont):
    def __init__(self):
        super().__init__()
        self.setPixelSize(8)
        self.setFamily('Montserrat')
