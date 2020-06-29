from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject
from ..objects import device

class deviceSignals(QObject):
    updating = pyqtSignal()
    updated = pyqtSignal()
    report_emitted = pyqtSignal(object)
    status_changes = pyqtSignal()
    error = pyqtSignal(Exception)


