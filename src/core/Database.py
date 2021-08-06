from PyQt5 import QtSql

queryDict = {
    'userclass': """
     CREATE TABLE IF NOT EXISTS USER_DATA (id int, username varchar(25), password varchar(256), ph_no int(10),
               logged_in date)
    """,
    'chatclass': """CREATE TABLE IF NOT EXISTS CHAT_DATA(id int primary key , name varchar(25))"""
}


class AppDataBase:
    def __init__(self):
        self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.query = QtSql.QSqlQuery()
        self.database.setDatabaseName('AppDatabase')
        self.database.setHostName('Local')
        self.initDataBase()

    def initDataBase(self):
        self.openDataBase()

        if not self.query.exec(queryDict['userclass']):
            print('Error:', self.query.lastError().text())
            return
        if not self.query.exec(queryDict['chatclass']):
            print('Error:', self.query.lastError().text())

    def openDataBase(self):
        if self.database.open():
            return
        print("Nope")

    def insertData(self):
        pass

    def deleteData(self):
        pass