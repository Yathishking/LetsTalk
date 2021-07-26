from PyQt5 import QtWidgets, QtGui, QtCore
from src.core.Fonts import Heading, TimeFont, ContactListFont
from src.core.DataInfo import ContactInfo


class ContactCard(QtWidgets.QWidget):
    def __init__(self, parent):
        super(ContactCard, self).__init__(parent)
        self.hlayout = QtWidgets.QHBoxLayout(self)
        self.index = None
        self.contactImage = QtWidgets.QLabel()
        self.contactInfo = QtWidgets.QWidget()
        self.contactDataInfo = ContactInfo()
        self.contactName = QtWidgets.QLabel('Vincent Kapor')
        self.latestTextMessage = QtWidgets.QLabel('Hello')
        self.vlayout = QtWidgets.QVBoxLayout(self.contactInfo)
        self.lastSeenLabel = QtWidgets.QLabel('12:00')
        self.setMaximumHeight(60)
        self.setupObjects()
        self.initLayout()
        self.initStyles()

    def initContactInfo(self, id, contactName: str):
        self.contactDataInfo.contactName = contactName
        self.contactDataInfo.contactID = id
        self.contactName.setText(contactName)

    def setupObjects(self):
        lastseenlabelfont = TimeFont()
        contactNameFont = ContactListFont()
        self.setObjectName('contactcard')
        self.lastSeenLabel.setObjectName('lastseenlabel')
        self.contactInfo.setObjectName('contactinfo')
        self.contactImage.setObjectName('contactimage')
        self.contactName.setObjectName('contactname')
        self.latestTextMessage.setObjectName('latesttextmessage')
        self.contactName.setFont(contactNameFont)
        self.lastSeenLabel.setFont(lastseenlabelfont)
        self.contactImage\
            .setPixmap(QtGui.QIcon('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/contact-outline.png')
                       .pixmap(30, 30))

    def initLayout(self):
        self.vlayout.addWidget(self.contactName)
        self.vlayout.addWidget(self.latestTextMessage)
        self.contactInfo.setLayout(self.vlayout)
        self.hlayout.addWidget(self.contactImage, 0, alignment=QtCore.Qt.AlignLeft)
        self.hlayout.addWidget(self.contactInfo, 2, alignment=QtCore.Qt.AlignLeft)
        self.hlayout.addWidget(self.lastSeenLabel, 0, QtCore.Qt.AlignRight)
        self.setLayout(self.hlayout)
        self.vlayout.setContentsMargins(2, 2, 2, 2)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        opt = QtWidgets.QStyleOption()
        painter = QtGui.QPainter(self)
        opt.initFrom(self)
        self.style().drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, painter, self)

    def initStyles(self):
        self.setStyleSheet("""
        QWidget#contactcard{
            background: #1b1b1b;
            border: 1px solid #212121;
            border-radius: 4px;
        }
        QWidget{
            background: #1b1b1b;
        }
        """)

