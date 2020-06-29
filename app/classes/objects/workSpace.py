import json
from pymongo.collection import ObjectId
from uuid import UUID, uuid4

class workSpace(object):

    def __init__(self,dict=None):
        if dict is None:
            self.id = ObjectId().__str__()
            self.nombre = "workSpace 1"
            self.devices = []
            self.devicesCount = 0
        else:
            self.id = dict["Id"]
            self.nombre = dict["Nombre"]
            if not "Drivers" in dict.keys():
                self.devices = list([])
            else:
                self.devices = list(self.devicesToList(dict["Drivers"]))
            self.devicesCount = dict["DriversCount"]
        
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value:str):
        if not (ObjectId.is_valid(value)):
            raise ValueError("¡Error! %s no es ObjectID valido" % value)
        self.__id = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,value:str):
        if len(value) < 3 or value is None:
            raise ValueError("¡Error! %s no es un nombre valido" % value.__str__())
        self.__nombre = value

    @property
    def devices(self):
        return self.__devices
    
    @devices.setter
    def devices(self,value:list):
        if not type(value) is list or value is None:
            raise ValueError("¡Error! La lista de dispositivos debe ser del tipo \"list\"")
        for d in value:
            if not isinstance(d,device):
                raise ValueError("¡Error! La lista de dispositivos solo puede contener objetos de la clase \"device\"")                
        self.__devices = value    

    @property
    def devicesCount(self):
        return self.__devicesCount

    @devicesCount.setter
    def devicesCount(self,value:int):
        if value < 0 or value is None: 
            raise ValueError("¡Error! El numero de dispositivos en un workSpace no puede ser negativo o nulo")
        self.__devicesCount = value

    def toJSON(self):
        return  {
                 "Id":self.id,
                 "Nombre":self.nombre,
                 "Drivers":list(self.deviceToJSON()),
                 "DriversCount":self.devicesCount
                }

    def deviceToJSON(self):
        for d in self.devices:
            yield d.toJSON()

    def devicesToList(self,devices):
        if devices is None: return []
        for d in devices:
            yield device(d)

class device(object):

    def __init__(self,dict = None):
        if dict is None:
            self.unicID = uuid4().__str__()
            self.nombre = "dev1"
            self.empty = True
            self.time = 30
            self.x = 0
            self.y = 0
            self.id = "123456789"
            self.token = "123456789"
            self.image  = "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"
            self.lastUpdate = "Nunca"
            self.variables = []
        else:
            self.unicID = dict["UnicID"]
            self.nombre = dict["Nombre"]
            self.empty = False
            self.time = dict["Time"]
            self.x = dict["X"]
            self.y = dict["Y"]
            self.id = dict["ID"]
            self.token = dict["Token"]
            self.image = dict["Image"]
            self.lastUpdate = dict["LastUpdate"]
            self.variables = list(self.variablesToList(dict["Variables"]))
        
    @property
    def unicID(self):
        return self.__unicID

    @unicID.setter
    def unicID(self,value:str):
        try:
            (UUID(value,version=4))
        except ValueError:
            raise ValueError("¡Error! \"%s\" no es un GUIDv4 valido" % value)
        self.__unicID = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,value:str):
        if len(value) < 3 or value is None:
            raise ValueError("¡Error! \"%s\" no es un nombre valido, Min 3" % value.__str__())
        self.__nombre = value

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self,value):
        if (int(value) <= 0 or int(value > 999)):
            raise ValueError("¡Error! Rango de tiempo adminitdo 1-999")
        self.__time = int(value)
    
    @property
    def empty(self):
        return self.__empty

    @empty.setter
    def empty(self,value):
        if not isinstance(value,bool):
            raise ValueError("¡Error! Empty debe ser Verdadero o Falso")
        self.__empty = value

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,value:int):
        if value < 0 or value is None:
            self.__x = 0
            #raise AttributeError("¡Error! Coordenada X no puede ser negativa o nula, Reestablaciendo a 0")
        self.__x = value
    
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,value:int):
        if value < 0 or value is None:
            self.__y = 0
            #raise AttributeError("¡Error! Coordenada Y no puede ser negativa o nula, Reestablaciendo a 0")
        self.__y = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        if len(value) < 3 or None:
            raise ValueError("¡Error! \"%s\" no es ID valido" % value.__str__())
        self.__id = value

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self,value):
        if len(value) < 3 or None:
            raise ValueError("¡Error! \"%s\" no es Token valido" % value.__str__())
        self.__token = value

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self,value):
        if value is None or value == "":
            self.__image = "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"
        else:
            self.__image = value

    @property
    def variables(self):
        return self.__variables

    @variables.setter
    def variables(self,value):
        if not type(value) is list or value is None:
            raise ValueError("¡Error! La lista de dispositivos debe ser del tipo \"list\"") #y solo contener objetos de la clase \"device\"
        for v in value:
            if not isinstance(v,variable):
                raise ValueError("¡Error! La lista de dispositivos solo puede contener objetos de la clase \"variable\"")  
        self.__variables = value

    @property
    def lastUpdate(self):
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self,value):
        if value is None or value == "":
            self.__lastUpdate = "Nunca"
            #raise TypeError("¡Error! Ultima actualizacion no puede ser nulo o vacio, Reestableciendo")
        self.__lastUpdate = value

    def toJSON(self):
        return {
            "UnicID":self.unicID,
            "Nombre":self.nombre,
            "IsEmpty":False,
            "Time":self.time,
            "X":self.x,
            "Y":self.y,
            "ID":self.id,
            "Token":self.token,
            "Image":self.image,
            "Variables":list(self.varToJSON()),
            "LastUpdate":self.lastUpdate
        }

    def varToJSON(self):
        for v in self.variables:
            yield v.toJSON()

    def variablesToList(self,vars):
        if vars is None: return []
        for v in vars:
            yield variable(v)
    

class variable(object):

    def __init__(self, dict = None):
        if dict is None:
            self.unicID = uuid4().__str__()
            self.nombre = "var1"
            self.pin = "AI0"
            self.value = "0"
            self.analogic = True
            self.displayColor = None
            self.notify  = None
            self.nivel = None
            self.output = False
        else:
            self.unicID = dict["UnicID"]
            self.nombre = dict["Nombre"]
            self.pin = dict["PIN"]
            self.value = dict["Valor"]
            self.analogic = dict["Analogic"]
            self.displayColor = dict["DisplayColor"]
            self.expresion = dict["Expresion"]
            self.notify = dict["Notificar"]
            self.nivel = dict["Nivel"]
            self.output = dict["IsOutput"]

    @property
    def unicID(self):
        return self.__unicID

    @unicID.setter
    def unicID(self,value):
        try:
            (UUID(value,version=4))
        except ValueError:
            raise ValueError("¡Error! \"%s\" no es un GUIDv4 valido" % value)
        self.__unicID = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,value):
        if len(value) < 3 or value is None:
            raise ValueError("¡Error! \"%s\" no es un nombre valido\nMinimo 3 caracteres" % value.__str__())
        self.__nombre = value

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self,value):
        if value == "" or value is None:
            raise ValueError("¡Error! variable no valida")
        self.__pin = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self,value):
        self.__value = value

    @property
    def analogic(self):
        return self.__analogic

    @analogic.setter
    def analogic(self,value):
        if not isinstance(value,bool):
            raise ValueError("¡Error! Propiedad \"analogic\" solo admite booleanos" % value)
        self.__analogic = value
    
    @property
    def displayColor(self):
        return self.__displayColor

    @displayColor.setter
    def displayColor(self,value):
        if value == "" or value == "null":
            self.__displayColor = None
        self.__displayColor = value
    
    @property
    def expresion(self):
        return self.__expresion

    @expresion.setter
    def expresion(self,value):
        from classes import Logica
        if value == "" or value == "null" or value == '' or value is None:
            self.__expresion = None
            return
        if not Logica.evaluarExpresion(value) :
            raise ValueError("¡Error! \"%s\" no es una expresion valida\nLa expresion debe ser logica y contener solo a x" % value)
        self.__expresion = value

    @property
    def notify(self):
        return self.__notify

    @notify.setter
    def notify(self,value):
        import re
        if value == "" or value == "null" or value == None:
            self.__notify = None
            return
        if not re.search("^((x->|x-<|x==|x!=)[0-9]{1,}$)",value):
            raise ValueError("¡Error! \"%s\" no es un comparador valido" % value)
        self.__notify = value

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self,value):
        if value == "" or value == "null":
            self.__expresion = None
        if value != "aqua" and value != "green" and value != "orange" and value != "red" and value != None:
            raise ValueError("¡Error! \"%s\" no es un nivel valido" % value)
        self.__nivel = value

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self,value):
        if not isinstance(value,bool):
            raise ValueError("¡Error! Propiedad \"output\" solo admite booleanos ")
        self.__output = value

    def toJSON(self):
        return {
                "UnicID":self.unicID,
                "Nombre":self.nombre,
                "PIN":self.pin,
                "Valor":self.value,
                "Analogic":bool(self.analogic),
                "DisplayColor":self.displayColor,
                "Expresion":self.expresion,
                "Notificar":self.notify,
                "Nivel":self.nivel,
                "IsOutput":self.output
                }
