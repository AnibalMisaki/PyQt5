from pymongo.collection import ObjectId

class usuario(object):

    def __init__(self,dict = None):
        if dict is None:
            self.id = ObjectId().__str__()
            self.nombres = "Usuario1"
            self.tipo = "Usuario"
            self.usuario = "usuario.scada"
            self.email = "usuario@gmail.com"
            self.enabled = False
            self.access_token = None
            self.refresh_token = None
        else:
            self.id = dict["Id"]
            self.nombres = dict["Nombres"]
            self.tipo = dict["Tipo"]
            self.usuario = dict["Usuario"]
            self.email = dict["Email"]
            self.enabled = dict["Enabled"]
            if "access_token" in dict:
                self.access_token = dict["access_token"]
            if "refresh_token" in dict:
                self.refresh_token = dict["refresh_token"]

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def nombres(self):
        return self.__nombres

    @nombres.setter
    def nombres(self,value):
        if len(value) < 3 or len(value) > 32 and value != None:
            raise ValueError("¡Error! \"%s\" no es un nombre valido\nMinimo 3 caracteres, Maximo 32" % value.__str__())
        self.__nombres = value

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,value):
        if value != "Administrador" and value != "Usuario" and value != None:
            raise ValueError("¡Error! Tipo de usuario invalido")
        self.__tipo = value

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self,value):
        if len(value) < 3 or len(value) > 24 and value != None:
            raise ValueError("¡Error! \"%s\" no es un usuario valido\nMinimo 3 caracteres, Maximo 24" % value.__str__())
        self.__usuario = value

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,value):
        import re
        if not re.search("^((\w|ñ){1,}(\.){0,1}){1,}@(\w|ñ){3,}((\.)[ñA-Za-z]{2,3}){1,}",value) and self.usuario != "administrador.scada" and value != None:
            raise ValueError("¡Error! \"%s\" no es un email valido" % value)
        self.__email = value
    
    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self,value):
        self.__enabled = self.toBool(value)

    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self,value):
        self.__access_token = value
    
    @property
    def refresh_token(self):
        return self.__refresh_token

    @refresh_token.setter
    def refresh_token(self,value):
        self.__refresh_token = value
        #return Exception("¡Error! Solo se puede asignar un refresh token")

    def toJSON(self):
        return {
            "Id":self.id,
            "Nombres":self.nombres,
            "Usuario":self.usuario,
            "Email":self.email,
            "Password":self.randomPassword(),
            "Tipo":self.tipo,
            "Enabled":self.enabled
        }

    @staticmethod
    def randomPassword(lenght=12):
        import random
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        txtPass = ""
        for i in range(lenght):
            txtPass += alphabet[random.randint(0,alphabet.__len__()-1)]
        return txtPass

    @staticmethod
    def toBool(str):
        if str in ["true","True",1,"verdadero",True]:
            return True
        else:
            return False

