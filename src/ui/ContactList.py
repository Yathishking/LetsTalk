from PyQt5 import QtWidgets, QtCore
from .ContactCard import ContactCard


class ContactList(QtWidgets.QListWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.setObjectName("contactlist")
        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.initStyles()
        self.addContactTOList()
        self.addContactTOList()

    def addContactTOList(self):
        listItem = QtWidgets.QListWidgetItem()
        contactCard = ContactCard(self)
        listItem.setSizeHint(contactCard.sizeHint())
        self.addItem(listItem)
        self.setItemWidget(listItem, contactCard)

    def initStyles(self):
        self.setStyleSheet("""
        QWidget#contactlist{
            border-radius: 4px;
            border: 2px solid #212121;
        }  
        """)

