from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject

class variableSignals(QObject):
    update = pyqtSignal(object)
    #updated = pyqtSignal(object)