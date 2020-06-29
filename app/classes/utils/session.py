from PyQt5.QtWidgets import QMessageBox, QApplication
from ..objects.usuario import usuario

class session(object):

    __instance = None # Instance of the session; just can exists one on all the app

    def __new__(cls,*args,**kwargs ):        
        if cls.__instance is None :
            cls.__instance =  object.__new__(cls)
            super(session,cls.__instance).__init__()
            cls.__sessionObject = args[0]
        return cls.__instance

    def __init__(self,*args):
        if not self.isValid():
            QMessageBox.warning(None,"¡Error!","Session invalida o inexistente\nCerrado Aplicacion...")
            QApplication.exit(0)

    @property
    def nombres(self):
        return self.__sessionObject.nombres

    @property
    def access_token(self):
        return self.__sessionObject.access_token

    @property
    def usuario(self):
        return self.__sessionObject.usuario

    @property
    def tipo(self):
        return self.__sessionObject.tipo

    @property
    def email(self):
        return self.__sessionObject.email
    
    @property
    def id(self):
        return self.__sessionObject.id.__str__()
    
    def destroy(self):
        self.__instance = None
        self.__sessionObject = None

    def isValid(self): # just validate that an user object exits, if access_token is invalid o doesnt exist API will deny access
        return True if isinstance(self.__sessionObject,usuario) else False
