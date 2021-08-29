from PyQt5 import QtGui, QtWidgets, QtMultimediaWidgets, QtMultimedia, QtCore
from sys import argv, exit


class FileWidgetDownloadButton(QtWidgets.QWidget):
    def __init__(self):
        super(FileWidgetDownloadButton, self).__init__()
        self.vlayout = QtWidgets.QVBoxLayout()
        self.spinbar = QtWidgets.QProgressBar()
        self.button = QtWidgets.QPushButton('Start')
        self.vlayout.addWidget(self.button)
        self.vlayout.addWidget(self.spinbar)
        self.setLayout(self.vlayout)
        self.button.clicked.connect(self.changePosition)
        self.spinbar.setStyleSheet("""
            color: dodgerblue;
            background-color: whitesmoke;
        """)
        self.spinbar.setFixedHeight(20)

    def changePosition(self):
        self.spinbar.setRange(0, 100)
        for i in range(0, 101):
            for j in range(0, 66556):
                pass
            self.spinbar.setValue(i)


class LTAudioPlayer(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.hlayout = QtWidgets.QHBoxLayout()
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.playButton = QtWidgets.QPushButton()
        self.playButton.setIcon(self.style().standardIcon(getattr(QtWidgets.QStyle, 'SP_MediaPlay')))
        self.audioplayer = QtMultimedia.QMediaPlayer()
        self.hlayout.addWidget(self.playButton)
        self.hlayout.addWidget(self.slider)
        self.setLayout(self.hlayout)
        self.playButton.clicked.connect(self.playOrPauseHandle)
        self.audioplayer.positionChanged.connect(self.connectSliderAndPlayer)
        self.setGeometry(100, 100, 400, 400)

    def openAudio(self, filepath):
        self.audioplayer.setMedia(
            QtMultimedia.QMediaContent(QtCore.QUrl
                                       .fromLocalFile(filepath)))

    def playOrPauseHandle(self):
        self.slider.setRange(0, self.audioplayer.duration())
        if self.audioplayer.state() == 1:
            self.audioplayer.pause()
            self.playButton.setIcon(self.style().standardIcon(getattr(QtWidgets.QStyle, 'SP_MediaPlay')))
        else:
            self.audioplayer.play()
            self.playButton.setIcon(self.style().standardIcon(getattr(QtWidgets.QStyle, 'SP_MediaPause')))

    def connectSliderAndPlayer(self, position):
        self.slider.setValue(position)


class LTMediaplayer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mediaplayer = QtMultimedia.QMediaPlayer()
        self.videoplayer = QtMultimediaWidgets.QVideoWidget()
        self.vlayout = QtWidgets.QVBoxLayout()
        self.vlayout.setAlignment(QtCore.Qt.AlignBottom)
        self.startbutton = QtWidgets.QPushButton('Start')
        self.pausebutton = QtWidgets.QPushButton('Pause')
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setTracking(True)
        self.startbutton.clicked.connect(self.startplay)
        self.pausebutton.clicked.connect(self.pauseVideo)
        self.mediaplayer.positionChanged.connect(self.connectSliderAndPlayer)
        self.slider.sliderMoved.connect(self.updatePlayerPosition)
        self.vlayout.addWidget(self.videoplayer)
        self.vlayout.addWidget(self.slider)
        self.vlayout.addWidget(self.startbutton)
        self.vlayout.addWidget(self.pausebutton)
        self.setLayout(self.vlayout)
        self.setGeometry(10, 10, 400, 400)
        self.setWindowTitle('Video player')

    def openVideo(self, filepath):
        self.mediaplayer.setMedia(
            QtMultimedia.QMediaContent(QtCore.QUrl
                                       .fromLocalFile(filepath)))
        self.mediaplayer.setVideoOutput(self.videoplayer)

    def startplay(self):
        self.slider.setRange(0, self.mediaplayer.duration())
        self.mediaplayer.play()

    def connectSliderAndPlayer(self, position):
        self.slider.setValue(position)

    def updatePlayerPosition(self, value):
        self.mediaplayer.setPosition(value)

    def pauseVideo(self):
        if self.mediaplayer.state() == 1:
            self.mediaplayer.pause()
            self.pausebutton.setText('Play')
        else:
            self.mediaplayer.play()
            self.pausebutton.setText('Pause')


def main():
    app = QtWidgets.QApplication(argv)
    exe = FileWidgetDownloadButton()
    exe.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()
