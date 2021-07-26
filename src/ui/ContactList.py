from PyQt5 import QtWidgets, QtCore
from .ContactCard import ContactCard

contactInfoList = [{
  "id": 1,
  "contactName": "Jessy"
}, {
  "id": 2,
  "contactName": "Jones"
}]

class ContactList(QtWidgets.QListWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.setObjectName("contactlist")
        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.initStyles()
        self.initContacts()

    def initContacts(self):
        for i in contactInfoList:
            self.addContactTOList(i)

    def addContactTOList(self, contactInfo):
        listItem = QtWidgets.QListWidgetItem()
        contactCard = ContactCard(self)
        contactCard.initContactInfo(contactInfo['id'], contactInfo['contactName'])
        listItem.setSizeHint(contactCard.sizeHint())
        self.addItem(listItem)
        self.setItemWidget(listItem, contactCard)

    def initStyles(self):
        self.setStyleSheet("""
        QListWidget#contactlist{
            border-radius: 4px;
            border: none;
        } 
        """)

