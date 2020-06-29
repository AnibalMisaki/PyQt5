import PyQt5
from PyQt5.QtCore import Qt,QObject, pyqtSlot, pyqtSignal, QThreadPool
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QMessageBox, QApplication
from PyQt5.QtGui import QIcon
from ..utils.session import session
from resources.resources import *

class formSignals(QObject):

    login = pyqtSignal(object)
    logout = pyqtSignal()
    finish = pyqtSignal()
    error = pyqtSignal(Exception)
    resize = pyqtSignal()

class form(QMainWindow): # class to be inherit to make a main window

    threadpool = QThreadPool()
    signals = formSignals()

    def __init__(self):
        QMainWindow.__init__(self)
        self.center()
        self.setWindowIcon(QIcon(':/source/img/if_16_1751363.ico'))
        self.setAttribute(Qt.WA_DeleteOnClose) 
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def resizeEvent(self,event):
        self.signals.resize.emit()

    def exit(self,event):
        reply = QMessageBox.question(
            self, "Confirmacion",
            "¿Seguro que desea salir?",
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.signals.finish.emit()
            if not (isinstance(event,bool)) : event.accept()
        else:
            if not (isinstance(event,bool)) : event.ignore()
