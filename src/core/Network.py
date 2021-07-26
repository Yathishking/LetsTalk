from PyQt5 import QtNetwork, QtCore


class ApplicationNetwork:
    def __init__(self):
        self.networkManager = QtNetwork.QNetworkAccessManager()
        self.request = QtNetwork.QNetworkRequest()
        self.reply = QtNetwork.QNetworkReply()

    def sendRequest(self):
        self.request.setUrl(QtCore.QUrl('http://localhost:8000'))
        self.reply = self.networkManager.post(self.request, QtCore.QByteArray())

    def replyHandler(self):
        if self.reply.error():
            print("Error")
        else:
            data = self.reply.readAll()
            value = str(data.data())
            print(value)
