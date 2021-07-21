import json, sys
import typing

from PyQt5 import QtWidgets, QtCore, QtGui

fp = open('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/vendor/emoji.json', 'r')
value: typing.List[typing.Dict] = json.loads(fp.read())
print(value.__len__())
row = 0
column = 0

class EmojiPicker(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.rowCount = value.__len__() / 15
        self.columnCount = 15
        self.setMessageInput = QtWidgets.QLineEdit()
        self.vlayout = QtWidgets.QVBoxLayout()
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.gridlayout = QtWidgets.QGridLayout()
        self.initLayout()
        self.show()

    def setMessageInputWidget(self, messageInput: QtWidgets.QLineEdit):
        self.setMessageInput = messageInput

    def initLayout(self):
        qwidget = QtWidgets.QWidget()
        qwidget.setLayout(self.gridlayout)
        self.initEmojis()
        self.scrollArea.setWidget(qwidget)
        self.vlayout.addWidget(self.scrollArea)
        self.setLayout(self.vlayout)

    def initEmojis(self):
        global row, column
        for i in value:
            if row > self.rowCount - 1:
                break
            emojilabel = EmojiLabel(i)
            emojilabel.setText(i['emoji'])
            emojilabel.clicked.connect(self.addToMessageInput)
            self.gridlayout.addWidget(emojilabel, row, column)
            if column > self.columnCount - 1:
                row = row + 1
                column = 0
            else:
                column = column + 1

    def addToMessageInput(self, emoji: str):
        self.setMessageInput.setText(f"{self.setMessageInput.text()} {emoji}")
        self.hide()


class EmojiLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal(str)

    def __init__(self, data):
        super().__init__()
        self.data = data
        font = self.font()
        font.setPointSize(12)
        self.setFont(font)

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.clicked.emit(self.text())

def main():
    application = QtWidgets.QApplication(sys.argv)
    ui = EmojiPicker()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
