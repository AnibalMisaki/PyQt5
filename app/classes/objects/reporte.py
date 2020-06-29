from datetime import datetime, date
import re

class reporte(object):

    def __init__(self,dict = None):
        if dict is None:
            self.nombreDispositivo = "devX"
            self.nombreVariable = "varX"
            self.fecha = date.today().strftime("%Y-%m-%d")
            self.hora = datetime.now().strftime("%I:%M:%S")
            self.value = 0
            self.condicion = "0==0"
            self.usuario = "usuariox"
            self.mensaje = "¡Alerta! Variable \"varX\" perteneciente a \"devX\" ha lanzado una alerta a las: XX:XX:XX del XX/XX"
            self.nivel = "aqua"
        else:
            self.nombreDispositivo = dict["NombreDispositivo"]
            self.nombreVariable = dict["NombreVariable"]
            self.fecha = dict["Fecha"]
            self.hora = dict["Hora"]
            self.value = dict["Valor"]
            self.condicion = dict["Condicion"]
            self.usuario = dict["Usuario"]
            self.mensaje = "¡Alerta! Variable \"%s\" perteneciente a \"%s\" ha lanzado una alerta a las: %s del %s" % (self.nombreVariable,self.nombreDispositivo,self.hora,datetime.now().strftime("%d/%m"))
            self.nivel = dict["Nivel"]


    @property
    def nombreDispositivo(self):
        return self.__nombreDispositivo

    @nombreDispositivo.setter
    def nombreDispositivo(self,value):
        if len(value) < 3 or value is None:
            raise ValueError("¡Error! \"%s\" no es un nombre valido\nMinimo 3 caracteres" % value.__str__())
        self.__nombreDispositivo = value

    @property
    def nombreVariable(self):
        return self.__nombreVariable

    @nombreVariable.setter
    def nombreVariable(self,value):
        if len(value) < 3 or value is None:
            raise ValueError("¡Error! \"%s\" no es un nombre valido\nMinimo 3 caracteres" % value.__str__())
        self.__nombreVariable = value

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self,value):
        try:
           datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("¡Error! Formato de fecha invalido\nFormato aceptado: YYYY-MM-DD")
        self.__fecha = value

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self,value):
        try:
            datetime.strptime(value, '%I:%M:%S')
        except ValueError:
            raise ValueError("¡Error! Formato de fecha invalido\nFormato aceptado: HH:MM:SS (12h)")
        self.__hora  = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self,value):
        self.__value = value

    @property
    def condicion(self):
        return self.__condicion

    @condicion.setter
    def condicion(self,value):
        if not re.search("^[0-9]{1,}((>|<|==|!=)[0-9]{1,}$)",value):
           raise ValueError("¡Error! \"%s\" no es una condicion valida" % value)
        self.__condicion = value

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self,value):
        self.__usuario = value

    @property
    def mensaje(self):
        return self.__mensaje

    @mensaje.setter
    def mensaje(self,value):
        self.__mensaje = value

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self,value):
        if value != "aqua" and value != "green" and value != "orange" and value != "red":
            raise ValueError("¡Error! \"%s\" no es un nivel valido" % value)
        self.__nivel = value

    def toJSON(self):
        return {
            "NombreDispositivo":self.nombreDispositivo,
            "NombreVariable":self.nombreVariable,
            "Fecha":self.fecha.__str__(),
            "Hora":self.hora.__str__(),
            "Valor":self.value,
            "Usuario":self.usuario,
            "Condicion":self.condicion,
            "Mensaje":self.mensaje,
            "Nivel":self.nivel
        }