from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox, QApplication
from PyQt5.QtCore import Qt,QObject, pyqtSlot, pyqtSignal, QThreadPool, QPoint
from ..utils.session import session


class modalSignals(QObject): # A class to emit signals at execution

    canceled = pyqtSignal() # not being implement at any moment
    success = pyqtSignal(object)

class modal(QDialog): # Class to be inherit to convert a window into a modal

    __instance = None # save the instance from the modal
    __instanced = False # save if already instanced

    def __new__(cls,**kwargs): # just can exits one instance from each modal that inherit this class
        if cls.__instance is None :
            cls.__instance =   QDialog.__new__(cls)
            QDialog.__init__(cls.__instance,kwargs["Parent"])
        return cls.__instance
    
    def __init__(self,**kwargs): #Parent must be a QMainWindow
        if not self.__instanced:
            self.session = session() # Automatic get session from program
            self.parent = kwargs["Parent"]
            self.signals = modalSignals() # Instance signals to be emited
            self.threadpool = QThreadPool() #QThearPool object to execute work class
            self.weight = 480 # for drag
            self.height = 720 # for drag
            self.dragPos = QPoint(0,0)
            self.setWindowFlags(Qt.FramelessWindowHint) # removes borders
            self.setAttribute(Qt.WA_TranslucentBackground) # Making it translucent to make a trick with the shadows
            self.setAttribute( Qt.WA_DeleteOnClose) # this should liberate ram
            self.setupUI()
            self.__instanced = True
        else:
            self.show()
            self.raise_()
            self.setWindowState(~Qt.WindowMinimized | Qt.WindowActive)
            self.activateWindow()
    
    def center(self): # this function is responsible for centering the modal with respect its father
        qr = self.frameGeometry()
        pr = self.parent.geometry()
        x = (self.parent.width() - qr.width()) / 2
        y = (self.parent.height() - qr.height()) / 2 
        self.setGeometry(x,y,qr.width(),qr.height())

    def exit(self): # this function is responsible to emit a cancelation signal if exit button was clicked
        reply = QMessageBox.question(
            self, "Confirmacion",
            "¿Seguro que desea cancelar?",
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.signals.canceled.emit()
            self.close()

    def prompt(self,title,text):
        reply = QMessageBox.question(
            self, title,
            text,
            QMessageBox.Yes | QMessageBox.No)
        return reply

    def setupUI(self): # virtual method, that should be implemente for each class that inherit
        raise NotImplementedError()

    def disconnectSignals(self): # virtual method, that should be implement for each class that inherit
        raise NotImplementedError()

    def disconnectSucces(self,handler):
        self.signals.success.disconnect(handler)
    def disconnectCancelled(self,handler):
        self.signals.canceled.disconnect(handler)

    def close(self):
        self.destroyInstance()
        super().close()
        self.disconnectSignals()
        self.deleteLater()
        QApplication.processEvents()

    @classmethod
    def destroyInstance(cls):
        cls.__instance = None
        cls.__instanced = False
        
    def success(self,_x:object): # this function is responsible to emit a success signal, if dialog was success
        self.signals.success.emit(_x)
        self.signals.success.disconnect()
        self.close()
    
    def cancel(self):
        self.signals.canceled.emit()
        self.signals.success.disconnect()
        self.close()

    def mousePressEvent(self, event): # it also get called on click a combobox
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            point = self.pos() + event.globalPos() - self.dragPos
             # Negative because it has a border for shadow, can be see it at qt designer with the .ui
            if ((point.x() <= -10 or point.x() >= self.parent.frameSize().width() - self.weight ) or (point.y() <= -10 or point.y() >= self.parent.frameSize().height() - self.height)) :
                event.ignore()
            else:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
