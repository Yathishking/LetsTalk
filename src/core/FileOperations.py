from PyQt5 import QtWidgets, QtCore


def getFilesInfo():
    fp = QtWidgets.QFileDialog.getOpenFileNames()[0]
    try:
        fileinfolist = [QtCore.QFileInfo(i) for i in fp]
        return fileinfolist
    except IndexError:
        return 


def getFileInfo():
    fp = QtWidgets.QFileDialog.getOpenFileName()[0]
    if fp == '':
        return
    fileinfo = QtCore.QFileInfo(fp)
    return fileinfo



