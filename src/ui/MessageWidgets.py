import typing
from PyQt5 import QtWidgets, QtCore, QtGui
from src.core.Fonts import ButtonFont, MessageFont, TimeFont


class MessageWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.hlayout = QtWidgets.QHBoxLayout(self)
        self.mainWidget = QtWidgets.QWidget(self)
        self.mainWidget.setStyleSheet("""
        background-color: dodgerblue;
        color: white;
        border-radius: 10px;
        border-top-right-radius: 0;
        """)
        messageFont = MessageFont()
        timefont = TimeFont()
        self.nhlayout = QtWidgets.QHBoxLayout(self.mainWidget)
        self.textMSGLabel = QtWidgets.QLabel('hello', self)
        self.textMSGLabel.setFont(messageFont)
        self.timeSentLabel = QtWidgets.QLabel("12:00", self)
        self.timeSentLabel.setFont(timefont)
        self.textMessage: typing.Any = ''
        self.timeSent: typing.Any = ''
        self.initLayout()

    def setMessage(self, message: str):
        if message == '':
            return
        self.textMessage = message

    def initLayout(self):
        self.nhlayout.addWidget(self.textMSGLabel)
        self.nhlayout.addWidget(self.timeSentLabel)
        self.mainWidget.resize(self.textMSGLabel.sizeHint())
        self.mainWidget.setLayout(self.nhlayout)
        self.hlayout.addWidget(self.mainWidget, 1, QtCore.Qt.AlignRight)
        self.setLayout(self.hlayout)
        self.nhlayout.setContentsMargins(10, 5, 3, 5)


class FileWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.hlayout = QtWidgets.QHBoxLayout(self)
        self.mainWidget = QtWidgets.QWidget(self)
        self.mainWidget.setStyleSheet("""
        background-color: dodgerblue;
        color: white;
        border-radius: 10px;
        border-top-right-radius: 0;
        """)
        self.fileInfo = QtCore.QFileInfo()
        timefont = TimeFont()
        self.vlayout = QtWidgets.QVBoxLayout()
        self.nhlayout = QtWidgets.QHBoxLayout()
        self.downloadFileButton = QtWidgets.QPushButton()
        self.fileName = QtWidgets.QLabel()
        self.filesize = QtWidgets.QLabel()
        self.timeSentLabel = QtWidgets.QLabel("12:00", self)
        self.timeSentLabel.setFont(timefont)
        self.setupObjects()
        self.initLayout()
        self.initStyles()

    def setupObjects(self):
        self.downloadFileButton.setObjectName('downloadFileButton')
        self.downloadFileButton.setIcon(
            QtGui.QIcon('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/download-white.png'))

    def setFileInfo(self, fileinfo: QtCore.QFileInfo):
        self.fileInfo = fileinfo
        self.fileName.setText(fileinfo.fileName())
        self.filesize.setText(str(fileinfo.size()))

    def initLayout(self):
        qwidget = QtWidgets.QWidget()
        self.vlayout.addWidget(self.fileName)
        self.vlayout.addWidget(self.filesize)
        qwidget.setLayout(self.vlayout)
        self.nhlayout.addWidget(self.downloadFileButton)
        self.nhlayout.addWidget(qwidget)
        self.nhlayout.addWidget(self.timeSentLabel)
        self.mainWidget.setLayout(self.nhlayout)
        self.hlayout.addWidget(self.mainWidget, 1, QtCore.Qt.AlignRight)
        self.setLayout(self.hlayout)
        self.nhlayout.setContentsMargins(10, 5, 3, 5)

    def initStyles(self):
        self.downloadFileButton.setStyleSheet("""
            QPushButton#downloadFileButton{
                background-color: skyblue;
                border-radius: 5px;
            }
        """)

