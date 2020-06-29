from classes import modal
from forms import UIAbrirModal, UIAPIModal
from PyQt5.QtWidgets import QMainWindow, QApplication

class Singleton(object):
    
    __instance = None
    
    def __new__(cls,**kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            super(Singleton,cls.__instance).__init__()
        return cls.__instance

class A(Singleton):
    def __new__(cls, *args, **kwargs): # call __new__ from father
        return super(A, cls).__new__(cls, **kwargs)

    def __init__(self):
        print("A instance")

class B(Singleton):
    def __init__(self):
        print("B Instace")

    def __new__(cls, *args, **kwargs):
        return super(B, cls).__new__(cls, **kwargs)

from PyQt5.QtWidgets import QApplication
from forms import UILogin, UIMainWindow
from classes import logger,timer,session
from functools import partial
import sip,sys

class modal1(modal):

    def __init__(self,MainWindow):
        super(modal1,self).__init__(MainWindow)

    def setupUI(self):
        print("setting ui up")

    def disconnectSignals(self):
        pass

class modal2(modal):

    def __init__(self,MainWindow):
        super(modal2,self).__init__(MainWindow)
    
    def setupUI(self):
        print("setting ui up")

    def disconnectSignals(self):
        pass

class application(QApplication):

    def __init__(self,*args):
        super(application,self).__init__(*args)

    def main(self):
        main = QMainWindow()
        main.show()
        m = modal1(**{"asd":"asd"})
        print(m)
        m.close()
        m2 = modal1(**{"asd":"asd"})
        print(m2)
        m3 = modal1(**{"asd":"asd"})
        print(m3)


app = application([])
app.main()
app.exec()


def function1(*args: Parent,modal ):
    args[0]


function1(QMainWindow,modal)






#a = A()
#b = B()
#a2 = A()
#b2 = B()

#print(a)
#print(a2)
#print(b)
#print(b2)



