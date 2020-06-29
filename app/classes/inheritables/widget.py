from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtCore import Qt, QObject, pyqtSlot, pyqtSignal, QThreadPool
from ..utils.session import session
from functools import partial

class widgetSignals(QObject):

    sucess = pyqtSignal(object)
    edit = pyqtSignal(object)
    delete = pyqtSignal(object)
    copy = pyqtSignal(object)
    enable = pyqtSignal(object)
    disable = pyqtSignal(object)

class widget(QWidget):

    threadpool = QThreadPool()

    def __init__(self,Parent=None):
        self.Parent = Parent
        self.signals = widgetSignals()
        QWidget.__init__(self,Parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.session = session() # Automatic get session from program

    def sucess(self, result:object,text):
        reply = QMessageBox.question(
            self, "Confirmacion",
            text,
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.signals.sucess.emit(result)
            self.signals.sucess.disconnect()
            self.close()
        else:
            pass

    def edit(self,tilte:str,text:str):
        reply = self.prompt(tilte,text)
        if reply == QMessageBox.Yes:
            self.signals.edit.emit(self.variable)

    def delete(self,title:str,text:str):
        reply = self.prompt(title,text)
        if reply == QMessageBox.Yes:
            self.signals.delete.emit(self.variable)

    def close(self):
        super().close()
        self.disconnectSignals()
        self.deleteLater()
        QApplication.processEvents()

    def disconnectSignals(self):
        raise NotImplementedError

    def disconnectSuccess(self,handler):
        self.signals.sucess.disconnect(handler)
    def disconnectEdit(self,handler):
        self.signals.edit.disconnect(handler)
    def disconnectDelete(self,handler):
        self.signals.delete.disconnect(handler)

    def prompt(self,title,text):
        reply = QMessageBox.question(
            self, title,
            text,
            QMessageBox.Yes | QMessageBox.No)
        return reply
