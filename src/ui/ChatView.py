import typing
from PyQt5 import QtWidgets, QtCore, QtGui
from src.core.Fonts import ButtonFont, MessageFont, ContactNameFont, TimeFont
from src.core.emoji import EmojiPicker


class ChatView(QtWidgets.QStackedWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super(ChatView, self).__init__(parent)
        self.setObjectName('chatview')
        self.addView()
        self.initStyles()

    def initStyles(self):
        self.setStyleSheet("""
            background-color: #1b1b1b;
            border-radius: 4px;    
        """)

    def addView(self):
        view = ChatWidget()
        self.addWidget(view)


class ChatWidgetBody(QtWidgets.QListWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName('chatwidgetbody')
        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.initStyles()

    def initStyles(self):
        self.setStyleSheet("""
            QListWidget#chatwidgetbody{
                border-top: 2px solid #212121;   
            }
        """)

    def addWidget(self, text: str = 'Hello'):
        listItem = QtWidgets.QListWidgetItem()
        message = MessageWidget()
        message.textMSGLabel.setText(text)
        listItem.setSizeHint(message.sizeHint())
        self.addItem(listItem)
        self.setItemWidget(listItem, message)
        self.setCurrentItem(listItem)


class ChatWidgetHeader(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.setObjectName('chatwidgetheader')
        self.hlayout = QtWidgets.QHBoxLayout(self)
        self.ContactPic = QtWidgets.QLabel()
        self.ContactName = QtWidgets.QLabel('Vincent Kapor')
        self.burgerMenu = QtWidgets.QPushButton()
        self.setupObjects()
        self.initLayout()
        self.initStyles()

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
        self.hlayout = QtWidgets.QHBoxLayout(self)
        self.emojiOption = QtWidgets.QPushButton()
        self.emojiPicker = EmojiPicker()
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
        self.emojiOption.setIcon(QtGui.QIcon('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/emoji.png'))
        self.sendButton.setIcon(QtGui.QIcon('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/send.png'))
        self.emojiOption.setIconSize(QtCore.QSize(23, 23))
        self.emojiPicker.setMessageInputWidget(self.messageInput)
        self.emojiOption.clicked.connect(self.showEmojiTab)

    def initLayout(self):
        self.hlayout.addWidget(self.emojiOption, 0, QtCore.Qt.AlignLeft)
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
        """)


class ChatWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.chatwidgetheader = ChatWidgetHeader(self)
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

