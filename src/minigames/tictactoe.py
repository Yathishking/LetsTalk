import typing
from PyQt5 import QtWidgets, QtCore, QtGui
from sys import argv, exit

playerSymbol = ['X', 'O']

winList = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(2, 0), (1, 1), (0, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
]

class Player:
    def __init__(self):
        self.playerId = 0
        self.playerSymbol = ''
        self.playerTurn = False
        self.playerBoxSelectionValue = []
        self.playerScore = 0

    def setPlayerID(self, pid):
        self.playerId = pid

    def setPlayerScore(self, score):
        self.playerScore = score

    def setPlayerSymbol(self, psymbol):
        self.playerSymbol = psymbol

    def setPlayerTurn(self, pturn: bool):
        self.playerTurn = pturn


class TicTacToe(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainwidget = QtWidgets.QWidget()
        self.gridlayout = QtWidgets.QGridLayout()
        self.gameLabel = QtWidgets.QLabel()
        self.gameWinner: Player = None
        self.players: typing.List[Player] = []
        self.gameStart: bool = False
        self.startButton = QtWidgets.QPushButton('Start Game')
        self.initGameLayout()
        self.mainwidget.setLayout(self.gridlayout)
        self.setCentralWidget(self.mainwidget)
        self.initUI()
        self.setupGame()
        self.show()

    def initUI(self):
        self.setFixedWidth(330)
        self.setFixedHeight(379)

    def alternateCursor(self, playerIconType):
        if playerIconType == 'O':
            cursor = QtGui.QCursor(QtGui.QPixmap('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/O.png'))
            self.setCursor(cursor)
        else:
            cursor = QtGui.QCursor(QtGui.QPixmap('/home/yathish/Desktop/LetsTalk/LetsTalk/assets/images/X.png'))
            self.setCursor(cursor)

    def setupGame(self):
        self.gridlayout.addWidget(self.startButton, 4, 0, 1, 3)
        self.gridlayout.addWidget(self.gameLabel, 5, 0, 1, 3)
        self.startButton.clicked.connect(self.GameLoop)
        for i in range(0, 2):
            player = Player()
            player.setPlayerID(i)
            player.setPlayerSymbol(playerSymbol[i])
            self.players.insert(i, player)

    def GameLoop(self):
        self.gameStart = True
        self.alternateCursor(self.players[0].playerSymbol)
        self.players[0].setPlayerTurn(True)
        self.players[1].setPlayerTurn(False)
        self.startButton.setDisabled(True)

    def playerWin(self):
        self.gameLabel.setText(f'Game won by {self.gameWinner.playerSymbol}')
        self.setDisabled(True)

    def gameEnd(self):
        for i in self.players:
            if i.playerScore == 1:
                self.playerWin()

    def updateScore(self, player: Player, value):
        player.playerBoxSelectionValue.append(value)
        player.playerBoxSelectionValue.sort()
        for i in winList:
            i.sort()
            if i == player.playerBoxSelectionValue:
                player.setPlayerScore(1)
                self.gameStart = False
                self.gameWinner = player
            elif i == [j for j in player.playerBoxSelectionValue if j in i]:
                player.setPlayerScore(1)
                self.gameStart = False
                self.gameWinner = player

    def takeTurn(self, stateValue = None):
        if self.gameStart and self.gameWinner is None:
            if self.players[0].playerTurn:
                self.players[1].setPlayerTurn(True)
                self.players[0].setPlayerTurn(False)
                self.alternateCursor(self.players[1].playerSymbol)
                self.updateScore(self.players[0], stateValue)
            else:
                self.players[0].setPlayerTurn(True)
                self.players[1].setPlayerTurn(False)
                self.alternateCursor(self.players[0].playerSymbol)
                self.updateScore(self.players[1], stateValue)
        else:
            self.playerWin()
        self.gameEnd()

    def initGameLayout(self):
        rows, columns = 3, 3
        for i in range(0, rows):
            for j in range(0, columns):
                label = ClickableLabel()
                label.setStateId((i, j))
                label.setFixedHeight(100)
                label.setFixedWidth(100)
                self.gridlayout.addWidget(label, i, j)
                label.clicked.connect(label.updateState)
                label.stateUpdated.connect(self.takeTurn)


class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal(QtGui.QPixmap)
    stateUpdated = QtCore.pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.stateid = (0, 0)
        self.setStyleSheet("""
            background: dodgerblue;
            color: whitesmoke;
        """)

    def setStateId(self, value):
        self.stateid = value

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.clicked.emit(self.cursor().pixmap())

    def updateState(self, pixmap: QtGui.QPixmap):
        self.setPixmap(pixmap.scaled(100, 100))
        self.stateUpdated.emit(self.stateid)


def main():
    app = QtWidgets.QApplication(argv)
    exe = TicTacToe()
    exit(app.exec_())


if __name__ == '__main__':
    main()
