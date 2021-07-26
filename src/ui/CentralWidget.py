import typing
from PyQt5 import QtWidgets
from .ContactList import ContactList
from .ChatView import ChatView
from .CompanyHeader import CompanyHeader


class CentralWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.centralLayout = QtWidgets.QHBoxLayout()
        self.mainview = QtWidgets.QWidget(self)
        self.vlayout = QtWidgets.QVBoxLayout(self.mainview)
        self.companyHeader = CompanyHeader(self.mainview)
        self.contactslist = ContactList(self)
        self.chatview = ChatView(self)
        self.initLayout()
        self.initStyles()
        self.signaLinker()

    def signaLinker(self):
        self.contactslist.itemClicked.connect(self.initChatView)

    def initChatView(self, item: QtWidgets.QListWidgetItem):
        widget = self.contactslist.itemWidget(item)
        if widget.index is not None:
            self.chatview.setCurrentIndex(widget.index)
            return
        index = self.chatview.addView(widget.contactDataInfo)
        widget.index = index
        self.chatview.setCurrentIndex(index)


    def initLayout(self):
        self.mainview.setMaximumWidth(300)
        self.vlayout.addWidget(self.companyHeader, 0)
        self.vlayout.addWidget(self.contactslist, 10)
        self.mainview.setLayout(self.vlayout)
        self.centralLayout.addWidget(self.mainview, 3)
        self.centralLayout.addWidget(self.chatview, 8)
        self.setLayout(self.centralLayout)

    def initStyles(self):
        self.mainview.setStyleSheet("""
            background-color: #212121;
            color: azure;
        """)
