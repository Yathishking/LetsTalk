import typing
from PyQt5 import QtWidgets, QtCore, QtGui
from src.core.Fonts import ButtonFont, MessageFont, ContactNameFont, TimeFont
from src.core.emoji import EmojiPicker
from src.core.FileOperations import getFileInfo
from .MessageWidgets import MessageWidget, FileWidget
from Test import test


class ChatView(QtWidgets.QStackedWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super(ChatView, self).__init__(parent)
        self.setObjectName('chatview')
        self.initStyles()

    def initStyles(self):
        self.setStyleSheet("""
            background-color: #1b1b1b;
            border-radius: 4px;    
        """)

    def addView(self, contactInfo):
        view = ChatWidget(contactInfo)
        index = self.addWidget(view)
        return index


class ChatWidget(QtWidgets.QWidget):
    def __init__(self, contactinfo):
        super().__init__()
        self.contactInfo = contactinfo
        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.chatwidgetheader = ChatWidgetHeader(self)
        self.chatwidgetheader.initContactInfo(contactinfo)
        self.chatwidgetbody = ChatWidgetBody(self)
        self.chatwidgetfooter = ChatWidgetFooter(self)
        self.initLayout()
        self.signalLinker()

    def initLayout(self):
        self.vlayout.addWidget(self.chatwidgetheader, 0)
        self.vlayout.addWidget(self.chatwidgetbody, 8)
        self.vlayout.addWidget(self.chatwidgetfooter, 0, QtCore.Qt.AlignBottom)
        self.setLayout(self.vlayout)

    def signalLinker(self):
        self.chatwidgetfooter.sendButton.clicked.connect(self.sendMessage)
        self.chatwidgetfooter.attachmentOption.clicked.connect(self.attachFile)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == QtCore.Qt.Key_Return:
            self.sendMessage()

    def sendMessage(self):
        message = self.chatwidgetfooter.messageInput.text()
        if message == '':
            return
        else:
            self.chatwidgetbody.addWidget(message)
            self.chatwidgetfooter.messageInput.clear()
            self.chatwidgetfooter.messageInput.focusWidget()
            return

    def attachFile(self):
        fileinfo = getFileInfo()
        self.chatwidgetbody.addFileWidget(fileinfo)
        self.chatwidgetfooter.messageInput.focusWidget()


class ChatWidgetBody(QtWidgets.QScrollArea):
    def __init__(self, parent):
        super().__init__(parent)
        self.topwidget = QtWidgets.QWidget()
        self.vlayout = QtWidgets.QVBoxLayout()
        self.topwidget.setLayout(self.vlayout)
        self.vlayout.setAlignment(QtCore.Qt.AlignBottom)
        self.vlayout.setSpacing(0)
        self.vlayout.setContentsMargins(10, 0, 10, 0)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.addWidget(alignment=QtCore.Qt.AlignLeft)
        self.setWidget(self.topwidget)
        self.setWidgetResizable(True)
        self.scrollbar = self.verticalScrollBar()
        self.scrollbar.rangeChanged.connect(self.moveScrollToBottom)

    def addWidget(self, text: str = 'Hello', alignment: QtCore.Qt.AlignmentFlag = QtCore.Qt.AlignRight):
        message = MessageWidget()
        message.setAlignment(alignment)
        message.textMSGLabel.setText(text)
        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(message, 0, alignment)
        hlayout.setSpacing(0)
        hlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.addLayout(hlayout)

    def addFileWidget(self, fileInfo: QtCore.QFileInfo, alignment: QtCore.Qt.AlignmentFlag = QtCore.Qt.AlignRight):
        file = FileWidget()
        file.setAlignment(alignment)
        file.setFileInfo(fileInfo)
        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(file, 0, alignment)
        hlayout.setSpacing(0)
        hlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.addLayout(hlayout)

    def moveScrollToBottom(self, minvalue, maxvalue):
        self.verticalScrollBar().setValue(maxvalue)


class ChatWidgetHeader(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.setObjectName('chatwidgetheader')
        self.contactInfo = ''
        self.hlayout = QtWidgets.QHBoxLayout(self)
        self.ContactPic = QtWidgets.QLabel()
        self.ContactName = QtWidgets.QLabel('Vincent Kapor')
        self.burgerMenu = QtWidgets.QPushButton()
        self.setupObjects()
        self.initLayout()
        self.initStyles()

    def initContactInfo(self, contactInfo):
        self.contactInfo = contactInfo
        self.ContactName.setText(self.contactInfo.contactName)

    def setupObjects(self):
        newIcon = QtGui.QIcon('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/contact-outline.png')
        contactfont = ContactNameFont()
        self.burgerMenu.setIcon(QtGui.QIcon('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/menu.png'))
        self.ContactPic.setPixmap(newIcon.pixmap(30, 30))
        self.ContactPic.setObjectName('contactpic')
        self.ContactName.setObjectName('contactname')
        self.ContactName.setFont(contactfont)
        self.burgerMenu.setObjectName('burgermenu')

    def initLayout(self):
        self.hlayout.addWidget(self.ContactPic, 1, QtCore.Qt.AlignLeft)
        self.hlayout.addWidget(self.ContactName, 10, QtCore.Qt.AlignLeft)
        self.hlayout.addWidget(self.burgerMenu, 0, QtCore.Qt.AlignRight)
        self.setLayout(self.hlayout)

    def initStyles(self):
        self.setStyleSheet("""
        QWidget#chatwidgetheader{
            border: 2px solid grey;
            background-color: #1b1b1b;
        }
        QLabel{
            color: dodgerblue;
        }
        QLabel#contactpic{
            border-radius: 15px;
        }
        QPushButton#burgermenu{
            background-color: #212121;
            padding: 5px;
        }
        """)


class ChatWidgetFooter(QtWidgets.QWidget):
    def __init__(self, parent):
        super(ChatWidgetFooter, self).__init__(parent)
        self.emojiPicker = EmojiPicker()
        self.hlayout = QtWidgets.QHBoxLayout(self)
        self.emojiOption = QtWidgets.QPushButton()
        self.attachmentOption = QtWidgets.QPushButton()
        self.messageInput = QtWidgets.QLineEdit()
        self.sendButton = QtWidgets.QPushButton('Send')
        self.setupObjects()
        self.initLayout()
        self.initStyles()

    def setupObjects(self):
        buttonFont = ButtonFont()
        self.emojiOption.setFont(buttonFont)
        self.sendButton.setFont(buttonFont)
        self.messageInput.setFont(buttonFont)
        self.emojiOption.setObjectName('emojioption')
        self.messageInput.setObjectName('messageinput')
        self.sendButton.setObjectName('sendbutton')
        self.attachmentOption.setObjectName('attachfile')
        self.emojiOption.setIcon(QtGui.QIcon('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/emoji.png'))
        self.attachmentOption.setIcon(
            QtGui.QIcon('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/attachfile-white.png'))
        self.sendButton.setIcon(QtGui.QIcon('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/send.png'))
        self.emojiOption.setIconSize(QtCore.QSize(23, 23))
        self.emojiPicker.setMessageInputWidget(self.messageInput)
        self.emojiOption.clicked.connect(self.showEmojiTab)

    def initLayout(self):
        self.hlayout.addWidget(self.emojiOption, 0, QtCore.Qt.AlignLeft)
        self.hlayout.addWidget(self.attachmentOption, 0, QtCore.Qt.AlignLeft)
        self.hlayout.addWidget(self.messageInput, 10)
        self.hlayout.addWidget(self.sendButton, 0, QtCore.Qt.AlignRight)
        qwidget = QtWidgets.QWidget()
        qwidget.setLayout(self.hlayout)
        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(qwidget)
        vlayout.addWidget(self.emojiPicker)
        self.emojiPicker.hide()
        self.setLayout(vlayout)

    def showEmojiTab(self):
        self.emojiPicker.show()

    def initStyles(self):
        self.setStyleSheet("""
            QPushButton#sendbutton{
                color: dodgerblue;
                border: none;
                background-color: #212121;
                padding: 5px;
                border-radius: 4px;
            }
            QPushButton#sendbutton:pressed, QPushButton#emojioption:pressed{
                background-color: #1b1b1b;
            }
            QLineEdit#messageinput{
                color: azure;
                border: none;
                padding: 5px;
                background-color: #212121;
                border-radius: 2px;
            }
            QPushButton#emojioption{
                color: dodgerblue;
                border: none;
                background-color: #212121;
                padding: 5px;
                border-radius: 4px;
            }
            QPushButton#attachfile{
                color: dodgerblue;
                border: none;
                background-color: #212121;
                padding: 5px;
                border-radius: 4px;
            }
        """)

