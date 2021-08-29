from PyQt5 import QtCore
from asyncio import sleep


class Worker(QtCore.QRunnable):
    def __init__(self):
        super(Worker, self).__init__()
        pass

    def run(self) -> None:
        for i in range(0, 10):
            sleep(1)
            print(i)


class ThreadComponent:
    def __init__(self):
        self.threadpool = QtCore.QThreadPool()
        worker = Worker()
        self.threadpool.start(worker)
