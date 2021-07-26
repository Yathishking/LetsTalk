from PyQt5 import QtSql


class ChatDataBase:
    def __init__(self):
        self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.query = QtSql.QSqlQuery()
        self.database.setDatabaseName('Chat Database')
        self.database.setHostName('Local')

    def openDataBase(self):
        if self.database.open():
            return
        print("Nope")

    def insertData(self):
        pass

    def deleteData(self):
        pass