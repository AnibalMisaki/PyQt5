import json,re

class configuracion(object):

    def __init__(self,dict = None):
        self.apiLocal = _apiLocal(dict)
        self.apiExterna = _apiExterna(dict)
        self.mongoDB = _mongoDB(dict)

    @property
    def apiLocal(self):
        return self.__apiLocal

    @apiLocal.setter
    def apiLocal(self,value):
        self.__apiLocal = value

    @property
    def mongoDB(self):
        return self.__mongoDB

    @mongoDB.setter
    def mongoDB(self,value):
        self.__mongoDB = value

    @property
    def apiExterna(self):
        return self.__apiExterna

    @apiExterna.setter
    def apiExterna(self,value):
        self.__apiExterna = value

    def toJSON(self):
        return {
            "APISCADA":self.apiLocal.toJSON(),
            "MONGO":self.mongoDB.toJSON(),
            "APIPARTICLE":self.apiExterna.toJSON()
        }

class _apiLocal(object):

    def __init__(self,dict):
        self.__IPv4 = re.compile(r'(^| )((?:[1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:[1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])($| |/)')
        self.__portV4 = re.compile(r'^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$')
        if dict is None:
            self.IP = "127.0.0.1"
            self.puerto = "8080"
        else:
            self.IP = dict["APISCADA"]["Host"]
            self.puerto = dict["APISCADA"]["Port"]

    @property
    def IP(self):
        return self.__IP

    @IP.setter
    def IP(self,value):
        if not self.__IPv4.match(value):
            raise ValueError("¡Error! API Local\nDirección IP No valida ")
        self.__IP = value
    
    @property
    def puerto(self):
        return self.__Port

    @puerto.setter
    def puerto(self,value):
        if not self.__portV4.match(value):
            raise ValueError("¡Error! API Local\nPuerto No valido (0-65535) ")
        self.__Port = value

    def toJSON(self):
        return{
            "Host":self.IP,
            "Port":self.puerto
        }

class _mongoDB(object):

    def __init__(self,dict):
        self.__IPv4 = re.compile(r'(^| )((?:[1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:[1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])($| |/)')
        self.__portV4 = re.compile(r'^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$')
        if dict is None:
            self.IP = "127.0.0.1"
            self.puerto = "27017"
            self.usuario = ""
            self.password = ""
            self.dataBase = "SCADA"
        else:
            self.IP = dict["MONGO"]["MONGO_HOST"]
            self.puerto = dict["MONGO"]["MONGO_PORT"]
            self.usuario = dict["MONGO"]["MONGO_USER"]
            self.password = dict["MONGO"]["MONGO_PASS"]
            self.dataBase = dict["MONGO"]["MONGO_DBNAME"]

    @property
    def IP(self):
        return self.__IP

    @IP.setter
    def IP(self,value):
        if not self.__IPv4.match(value):
            raise ValueError("¡Error! MongoDB\nDirección IP No valida ")
        self.__IP = value
    
    @property
    def puerto(self):
        return self.__Port

    @puerto.setter
    def puerto(self,value):
        if not self.__portV4.match(value):
            raise ValueError("¡Error! MongoDB\nPuerto No valido (0-65535) ")
        self.__Port = value

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self,value):
        self.__usuario = value

    @property
    def password(self):
        return self.__pass

    @password.setter
    def password(self,value):
        self.__pass = value

    @property
    def dataBase(self):
        return self.__database

    @dataBase.setter
    def dataBase(self,value):
        if value == "":
            raise ValueError("¡Error! MongoDB\nDebe ingresar el nombre de la base de datos")
        self.__database = value

    def toJSON(self):
        return {
            "MONGO_HOST":self.IP,
            "MONGO_PORT":self.puerto,
            "MONGO_USER":self.usuario,
            "MONGO_PASS":self.password,
            "JSON_AS_ASCII":False,
            "MONGO_DBNAME":self.dataBase
        }
    
class _apiExterna(object):

    def __init__(self,dict):
        if dict is None:
            self.uri = "api.particle.io/v1/devices"
        else:
            self.uri = dict["APIPARTICLE"]["URI"]

    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self,value):
        if value == "":
            raise ValueError("¡Error! API Externa\nDebe ingresar una url valida")
        self.__uri = value

    def toJSON(self):
        return {
            "URI":self.uri
        }

class API(object):

    def __init__(self,dict = None):
        self.__IPv4 = re.compile(r'(^| )((?:[1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:[1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])($| |/)')
        self.__Domain = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}(\.[a-zA-Z])?[a-zA-Z0-9]{1,61}\.[a-zA-Z]{2,}|(localhost)$')
        self.__portV4 = re.compile(r'^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$')
        if dict is None:
            self.IP = "127.0.0.1"
            self.puerto = "8080"
        else:
            self.IP = dict["APISCADA"]["Host"]
            self.puerto = dict["APISCADA"]["Port"]

    @property
    def IP(self):
        return self.__IP

    @IP.setter
    def IP(self,value):
        if not self.__IPv4.match(value) and not self.__Domain.match(value):
            raise ValueError("¡Error! API Local\nDirección IP o dominio no valido")
        self.__IP = value
    
    @property
    def puerto(self):
        return self.__Port

    @puerto.setter
    def puerto(self,value):
        if value != None and not self.__portV4.match(value):
            raise ValueError("¡Error! API Local\nPuerto No valido (0-65535) ")
        self.__Port = value
    
    @property
    def HTTP_PROTOCOL(self):
        return self.__htttps

    @HTTP_PROTOCOL.setter
    def HTTP_PROTOCOL(self,value):
        if value != "http" and value != "https":
           raise ValueError("¡Error! Protocolos admitidos (HTTP|HTTPS)")
        self.__htttps = value

    def toJSON(self):
        return{
            "Host":self.IP,
            "Port":self.puerto,
            "HTTP_PROTOCOL":self.HTTP_PROTOCOL
        }

