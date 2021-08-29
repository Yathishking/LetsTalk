import math
import typing
from PyQt5 import QtWidgets, QtCore, QtGui, QtMultimediaWidgets, QtMultimedia
from src.core.Fonts import MessageFont, TimeFont
from src.include.CustomUIElements import LTAudioPlayer, LTMediaplayer

media = ['jpg', 'mp3', 'mpeg', 'mp4', 'mkv']
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


class MessageWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.hlayout = QtWidgets.QHBoxLayout(self)
        self.mainWidget = QtWidgets.QWidget(self)
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

    def setAlignment(self, alignment):
        if alignment is QtCore.Qt.AlignLeft:
            self.mainWidget.setStyleSheet("""
                background-color: dodgerblue;
                color: white;
                border-radius: 10px;
                border-top-left-radius: 0;
            """)
        else:
            self.initStyles()

    def initStyles(self):
        self.setStyleSheet("""
        background-color: dodgerblue;
        color: white;
        border-radius: 10px;
        border-top-right-radius: 0;
        """)


class FileWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mainvlayout = QtWidgets.QVBoxLayout(self)
        self.mainWidget = QtWidgets.QWidget(self)
        self.downloadProgressBar = QtWidgets.QProgressBar()
        self.downloadProgressBar.setFixedHeight(20)
        self.fileInfo = QtCore.QFileInfo()
        timefont = TimeFont()
        self.vlayout = QtWidgets.QVBoxLayout()
        self.nhlayout = QtWidgets.QHBoxLayout()
        self.downloadFileButton = QtWidgets.QPushButton()
        self.fileName = QtWidgets.QLabel()
        self.filesize = QtWidgets.QLabel()
        self.timeSentLabel = QtWidgets.QLabel("12:00", self)
        self.timeSentLabel.setFont(timefont)
        self.setContentsMargins(0, 5, 0, 5)
        self.setupObjects()
        self.initLayout()

    def setupObjects(self):
        self.downloadFileButton.setObjectName('downloadFileButton')
        self.downloadFileButton.setIcon(
            QtGui.QIcon('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/download-white.png'))
        self.downloadFileButton.clicked.connect(self.downloadFile)

    def downloadFile(self):
        pass

    def setFileInfo(self, fileinfo: QtCore.QFileInfo):
        self.fileInfo = fileinfo
        filename = fileinfo.fileName()
        filesize = fileinfo.size()
        self.downloadProgressBar.setRange(0, filesize)
        self.filesize.setText(convert_size(filesize))
        self.filesize.setToolTip(f"{filesize} bytes")

        if filename.__len__() > 10:
            fpinfolist = filename.split('.')
            self.fileName.setText(f"{fpinfolist[0][0:10]}...")
            self.fileName.setToolTip(filename)
        else:
            self.fileName.setText(filename)

        for i in media:
            if i in fileinfo.fileName():
                if i == 'jpg':
                    mediaLabel = QtWidgets.QLabel()
                    image = QtGui.QPixmap(fileinfo.absoluteFilePath())
                    image = image.scaled(200, 200)
                    mediaLabel.setPixmap(image)
                    self.mainvlayout.insertWidget(0, mediaLabel)
                    return
                elif i == 'mp3':
                    audioplayer = LTAudioPlayer()
                    audioplayer.openAudio(fileinfo.absoluteFilePath())
                    self.mainvlayout.insertWidget(0, audioplayer)
                    return
                else:
                    mediaplayer = LTMediaplayer()
                    mediaplayer.openVideo(fileinfo.absoluteFilePath())
                    self.mainvlayout.insertWidget(0, mediaplayer)
                    return

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        opt = QtWidgets.QStyleOption()
        painter = QtGui.QPainter(self)
        opt.initFrom(self)
        self.style().drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, painter, self)

    def initLayout(self):
        qwidget = QtWidgets.QWidget()
        self.vlayout.addWidget(self.fileName)
        self.vlayout.addWidget(self.filesize)
        qwidget.setLayout(self.vlayout)
        self.nhlayout.addWidget(self.downloadFileButton)
        self.nhlayout.addWidget(qwidget)
        self.nhlayout.addWidget(self.timeSentLabel)
        self.mainWidget.setLayout(self.nhlayout)
        self.mainvlayout.addWidget(self.mainWidget)
        self.setLayout(self.mainvlayout)
        self.parent()

    def setAlignment(self, alignment):
        self.setStyleSheet(f"""
            background-color: dodgerblue;
            color: white;
            border-radius: 10px;
            border-top-{'left' if alignment is QtCore.Qt.AlignLeft else 'right'}-radius: 0;
        """)
        self.initStyles()

    def initStyles(self):
        self.downloadFileButton.setStyleSheet("""
            QPushButton#downloadFileButton{
                background-color: skyblue;
                border-radius: 5px;
            }
        """)
