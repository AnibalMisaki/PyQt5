from PyQt5.QtCore import QTimer, pyqtSignal, QObject
from classes.objects.time import time

class timerSignals(QObject):    
    time_elapsed = pyqtSignal() # each second
    access_token_expired = pyqtSignal() # each 23 hours
    session_expired = pyqtSignal() # not being implemented, not necessary

class timer(QTimer):

    signals =  timerSignals()
    __instance = None # Instance of the timer; just can exists one on all the app
  
    def timerEvent(self,event):
        self.__time.addSeconds(1)
        print(self.__time.__dict__) # debug
        if self.__time.hours == 23:
            self.signals.access_token_expired.emit()
        self.signals.time_elapsed.emit()

    def __new__(cls,*args,**kwargs ):        
        if cls.__instance is None :
            cls.__instance =  QTimer.__new__(cls) 
            super(timer,cls.__instance).__init__()
            cls.__time = time()     
        return cls.__instance

    def restartTimer(self,timerid):
        self.killTimer(timerid)
        self.__time.restart()

    @property
    def time(self):
        return self.__time

