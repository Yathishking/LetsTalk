from PyQt5 import QtWidgets, QtCore, QtGui
from src.core.Fonts import Heading


class CompanyHeader(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.hlayout = QtWidgets.QHBoxLayout(self)
        self.searchLabel = QtWidgets.QLabel()
        self.companyNameLabel = QtWidgets.QLabel('LetsTalk')
        self.menu = QtWidgets.QPushButton()
        self.setupObjects()
        self.customSetup()
        self.signalLinker()
        self.initLayout()
        self.initStyles()

    def setupObjects(self):
        heading = Heading()
        self.searchLabel.setObjectName('searchlabel')
        self.companyNameLabel.setObjectName('companynamelabel')
        self.menu.setObjectName('mainmenubutton')
        self.searchLabel.setPixmap(QtGui.QIcon('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/search.png')
                                   .pixmap(20, 20))
        self.menu.setIcon(QtGui.QIcon('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/menu.png'))
        self.companyNameLabel.setFont(heading)

    def signalLinker(self):
        self.menu.clicked.connect(self.handleMenuClick)

    def initLayout(self):
        self.hlayout.addWidget(self.menu, 0, QtCore.Qt.AlignRight)
        self.hlayout.addWidget(self.companyNameLabel, 10, QtCore.Qt.AlignLeft)
        self.hlayout.addWidget(self.searchLabel, 0, QtCore.Qt.AlignLeft)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        opt = QtWidgets.QStyleOption()
        painter = QtGui.QPainter(self)
        opt.initFrom(self)
        self.style().drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, painter, self)

    def initStyles(self):
        self.setStyleSheet("""
            QPushButton#mainmenubutton{
                color: dodgerblue;
                border: none;
                background-color: #212121;
                padding: 5px;
                border-radius: 4px;
            }
            QPushButton#mainmenubutton:pressed{
                background-color: #1b1b1b;
                color: whitesmoke;
            }
            QPushButton::menu-indicator {
            image: none;
            }
        """)

    def customSetup(self):
        mainmenu = QtWidgets.QMenu()
        mainmenu.setObjectName('mainmenu')
        logout = QtWidgets.QAction('Logout', self)
        settings = QtWidgets.QAction('Settings', self)
        mainmenu.addAction(settings)
        mainmenu.addSeparator()
        mainmenu.addAction(logout)
        self.menu.setMenu(mainmenu)
        mainmenu.setStyleSheet("""
            QMenu#mainmenu{
                background-color: #212121;
                color: whitesmoke;
            }
            QMenu#mainmenu::item{
                background-color: transparent;
                color: whitesmoke;
            }
            QMenu#mainmenu::item:selected {
                background-color: #1b1b1b;
            }     
        """)

    def handleMenuClick(self, point):
        self.menu.showMenu()
