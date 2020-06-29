from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie, QPixmap, QImage
from classes import workSpace, timer, widget, device, deviceSignals, Worker, Logica, variable, reporte
from . import UIAIVariable,UIAOVariable,UIDIVariable,UIDOVariable
from resources import *
from datetime import datetime
from functools import partial
from base64 import b64decode,b64encode

class UIDispositivoWidget(widget):

    # Status
    # State 0: Device is only write, never update
    # State 1: Device is read/write, waits to update itself
    # State 2: Device is updating his variables
    # State 3: Device is updating his UI

    def __init__(self,Parent,dispositivo:device):
        self.__dispostivo = dispositivo
        self.deviceSignals = deviceSignals()
        self.__status = 0
        self.__variablesContainer = dict()
        super(UIDispositivoWidget,self).__init__(Parent)
        self.setupUi()
    
    def setupUi(self):
        DispositivoWidget = self
        DispositivoWidget.setObjectName("DispositivoWidget")
        DispositivoWidget.setWindowModality(QtCore.Qt.WindowModal)
        DispositivoWidget.resize(330, 200)
        DispositivoWidget.setGeometry(self.__dispostivo.x,self.__dispostivo.y,330,200)
        DispositivoWidget.setMinimumSize(QtCore.QSize(330, 200))
        self.MainFrame = QtWidgets.QFrame(DispositivoWidget)
        self.MainFrame.setGeometry(QtCore.QRect( 0,0, 330, 200))
        self.MainFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MainFrame.setObjectName("MainFrame")
        self.Container = QtWidgets.QGroupBox(self.MainFrame)
        self.Container.setGeometry(QtCore.QRect(0, 0, 329, 199))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(True)
        font.setWeight(75)
        self.Container.setFont(font)
        self.Container.setObjectName("Container")
        self.lblImagen = QtWidgets.QLabel(self.Container)
        self.lblImagen.setGeometry(QtCore.QRect(10, 50, 120, 115))
        self.lblImagen.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblImagen.setLineWidth(0)
        self.lblImagen.setText("")
        self.lblImagen.setPixmap(Logica.byteArrayToImage(self.__dispostivo.image))
        self.lblImagen.setScaledContents(True)
        self.lblImagen.setObjectName("lblImagen")
        self.StatusFrame = QtWidgets.QFrame(self.Container)
        self.StatusFrame.setGeometry(QtCore.QRect(5, 20, 321, 24))
        self.StatusFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.StatusFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.StatusFrame.setLineWidth(0)
        self.StatusFrame.setObjectName("StatusFrame")
        self.lblStatus = QtWidgets.QLabel(self.StatusFrame)
        self.lblStatus.setGeometry(QtCore.QRect(10, 5, 45, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblStatus.setObjectName("lblStatus")
        self.lblTime = QtWidgets.QLabel(self.StatusFrame)
        self.lblTime.setGeometry(QtCore.QRect(170, 5, 115, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblTime.setFont(font)
        self.lblTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTime.setObjectName("lblTime")
        self.Time = QtWidgets.QLabel(self.StatusFrame)
        self.Time.setGeometry(QtCore.QRect(285, 0, 24, 24))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Time.setFont(font)
        self.Time.setLineWidth(0)
        self.Time.setText("")
        self.Time.setTextFormat(QtCore.Qt.PlainText)
        self.Time.setScaledContents(True)
        self.Time.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Time.setObjectName("Time")
        self.Status = QtWidgets.QLabel(self.StatusFrame)
        self.Status.setGeometry(QtCore.QRect(71, 5, 90, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Status.setFont(font)
        self.Status.setStyleSheet("color:gray;")
        self.Status.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Status.setObjectName("Status")
        self.StatusCircle = QtWidgets.QLabel(self.StatusFrame)
        self.StatusCircle.setGeometry(QtCore.QRect(56, 8, 12, 12))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.StatusCircle.setFont(font)
        self.StatusCircle.setStyleSheet("background-color:gray;border-radius:5px;")
        self.StatusCircle.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.StatusCircle.setMidLineWidth(1)
        self.StatusCircle.setText("")
        self.StatusCircle.setObjectName("StatusCircle")
        self.lblLast = QtWidgets.QLabel(self.Container)
        self.lblLast.setGeometry(QtCore.QRect(10, 175, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblLast.setFont(font)
        self.lblLast.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblLast.setObjectName("lblLast")
        self.Last = QtWidgets.QLabel(self.Container)
        self.Last.setGeometry(QtCore.QRect(78, 175, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Last.setFont(font)
        self.Last.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Last.setTextFormat(QtCore.Qt.RichText)
        self.Last.setObjectName("Last")
        self.VariablesScroll = QtWidgets.QScrollArea(self.Container)
        self.VariablesScroll.setGeometry(QtCore.QRect(140, 50, 175, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VariablesScroll.sizePolicy().hasHeightForWidth())
        self.VariablesScroll.setSizePolicy(sizePolicy)
        self.VariablesScroll.setMinimumSize(QtCore.QSize(175, 115))
        self.VariablesScroll.setLineWidth(0)
        self.VariablesScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.VariablesScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.VariablesScroll.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.VariablesScroll.setWidgetResizable(False)
        self.VariablesScroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.VariablesScroll.setObjectName("VariablesScroll")
        self.VariablesFrame = QtWidgets.QWidget()
        self.VariablesFrame.setGeometry(QtCore.QRect(0, 0, 175, 115))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VariablesFrame.sizePolicy().hasHeightForWidth())
        self.VariablesFrame.setSizePolicy(sizePolicy)
        self.VariablesFrame.setMinimumSize(QtCore.QSize(175, 115))
        self.VariablesFrame.setSizeIncrement(QtCore.QSize(0, 0))
        self.VariablesFrame.setObjectName("VariablesFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.VariablesFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setAlignment(Qt.AlignTop)
        self.VariablesScroll.setWidget(self.VariablesFrame)
        self.movie = QMovie(":/source/img/Cargando.gif")
        self.movie.setScaledSize(QtCore.QSize(64,64))
        self.retranslateUi(DispositivoWidget)
        QtCore.QMetaObject.connectSlotsByName(DispositivoWidget)
        self.show()

        if len(self.__dispostivo.variables) == 0 or len(list(filter(lambda var:(not var.output) ,self.__dispostivo.variables))) == 0:
            self.lblTime.setText("¡No hay variables!")
            self.Time.hide()
        else:
            timer.signals.time_elapsed.connect(self.time) # Signal emitted each second
            self.__status = 1
        self.lblImagen.mouseDoubleClickEvent = self.actualizarImagen
        for var in self.__dispostivo.variables:
            self.mostrarVariable(var)
        if (len(self.__dispostivo.variables)*25) > 115:
            self.VariablesFrame.setGeometry(0,0,175,len(self.__dispostivo.variables)*25)

    def updateUI(self,dev:device):
        self.__dispostivo = dev
        _translate = QtCore.QCoreApplication.translate
        self.Container.setTitle(_translate("DispositivoWidget", self.__dispostivo.nombre))
        self.lblImagen.setPixmap(Logica.byteArrayToImage(self.__dispostivo.image))
        if self.__status == 2: # if updating then wait untill finish and update
            self.deviceSignals.updated.connect(self.updateVariables)
            return
        self.updateVariables()

    def updateVariables(self):
        previousState = self.__status
        self.__status = 3
        self.updateState("Actualizando UI...",self.movie)
        self.cleanVariables()
        for var in self.__dispostivo.variables:
            self.mostrarVariable(var)
        if (len(self.__dispostivo.variables)*25) > 115:
            self.VariablesFrame.setGeometry(0,0,175,len(self.__dispostivo.variables)*25)
        if len(self.__dispostivo.variables) == 0 or len(list(filter(lambda var:(not var.output) ,self.__dispostivo.variables))) == 0:
            self.updateState("¡No hay variables!",subText=None)
            if previousState == 1 or previousState == 2:
                timer.signals.time_elapsed.disconnect(self.time)
            self.__status = 0
        else:
            self.updateState("Actualizando en ",subText=str(self.__dispostivo.time))
            if previousState == 0: # previousState 0 is device only write
                timer.signals.time_elapsed.connect(self.time) # Signal emitted each second
            self.__status = 1

    def mostrarVariable(self,var:variable):
            UIvariable = None
            if (var.analogic and not var.output):
                UIvariable = UIAIVariable(var)
            if (var.analogic and var.output):
                UIvariable = UIAOVariable(var)
                UIvariable.variableSignals.update.connect(self.actualizarVariable)
            if (not var.analogic and not var.output):
                UIvariable = UIDIVariable(var)
            if(not var.analogic and var.output):
                UIvariable = UIDOVariable(var)
                UIvariable.variableSignals.update.connect(self.actualizarVariable)
            self.verticalLayout.addWidget(UIvariable,0,Qt.AlignTop)
            self.__variablesContainer[var.unicID] = UIvariable

    def actualizarImagen(self,event):
        from PyQt5.QtCore import QByteArray, QFileInfo
        from PyQt5.QtWidgets import QMessageBox
        fileName = QFileDialog.getOpenFileName(self,"Abrir",filter="Images (*.png *.jpg)")  # options=QtWidgets.QFileDialog.DontUseNativeDialog
        if all(fileName):
            info = QFileInfo(fileName[0])
            if info.size() > 32000:
                QMessageBox.warning(self,"¡Error!","No se permite archivos de mas de 32kb")
                return
            str_base64 = Logica.imageToByteArray(fileName[0])
            if str_base64 is None:
                QMessageBox.warning(self,"¡Error!","Fallo al cargar la imagen")
                return
            self.lblImagen.setPixmap( Logica.byteArrayToImage(str_base64) )
            self.__dispostivo.image = str_base64

    def disconnectSignals(self):
        if self.__status != 0:
            timer.signals.time_elapsed.disconnect(self.time)
        self.lblImagen.mouseDoubleClickEvent = None
        self.cleanVariables()
    
    def cleanVariables(self):
        for v in self.__variablesContainer.items():
            variable = v[1]
            if (variable.getVariable())["IsOutput"] == True:
                variable.variableSignals.update.disconnect(self.actualizarVariable)
            variable.close()
        self.__variablesContainer.clear()
        
    def getDevice(self):
        variables = []
        for v in self.__variablesContainer.items():
            variables.append(v[1].getVariable())
        device = self.__dispostivo.toJSON()
        device["variables"] = variables
        return device

    def time(self):
        if self.__status == 1:
            time = int(self.Time.text())-1
            if time == 0:
                self.__status = 2
                self.actualizarVariables(self.__dispostivo.variables)
            else:
                self.Time.setText(str(time))

    def actualizarVariables(self,variablesList:list): # Updates all input variables
        variablesList = list(filter(lambda var: (not var.output) ,variablesList))
        variablesList = list(self.variablesListToJSON(variablesList))
        self.updateState("Actualizando...",self.movie)
        self.deviceSignals.updating.emit()
        worker = Worker(Logica.LeerSensor,**{"access_token":self.session.access_token,"ID":self.__dispostivo.id,"Token":self.__dispostivo.token,"data":variablesList})
        worker.signals.finished.connect(self.actualizarVariables_Callback)
        self.threadpool.start(worker)  

    def actualizarVariables_Callback(self,variablesList:list): # callback for worker
        if isinstance(variablesList,Exception): # No connection with API SCADA
            self.deviceSignals.error.emit(variablesList)
            self.updateDeviceState("Sin Conexion")
        else:
            if len(variablesList) == 0:
                self.deviceSignals.error.emit(Exception("No hay acceso a internet")) # No Internet connection
                self.updateDeviceState("Desconectado","red")
            else:
                for v in variablesList:
                    if not v.expresion is None:
                        v.value = Logica.evaluarExpresion(v.expresion,v.value)
                    if not v.notify is None: # If notify option is active
                        if Logica.evaluarExpresion(v.notify.replace("-","").strip(),v.value): # evaluate if condition is true
                           self.nuevoReporte(v)
                    self.__variablesContainer[v.unicID].updateUI(v)
                    self.updateDeviceState("Conectado","green")
                    self.Last.setText(datetime.now().strftime("%d/%m/%Y %I:%M:%S %p"))
                    self.__dispostivo.lastUpdate = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
                    for i,var in enumerate(self.__dispostivo.variables): # to update his value
                        if var.unicID == v.unicID:
                            self.__dispostivo.variables[i].value = v.value
        if len(list(filter(lambda var:(not var.output) ,self.__dispostivo.variables))) == 0:
            self.updateState("¡No hay variables!",subText=None)
            self.__status = 0
        else:
            self.updateState("Actualizando en ",subText=str(self.__dispostivo.time))
            self.__status = 1
        self.deviceSignals.updated.emit()

    def nuevoReporte(self,v:variable):
        from datetime import date, time
        report = reporte({
            "NombreDispositivo":self.__dispostivo.nombre,
            "NombreVariable":v.nombre,
            "Valor":v.value,
            "Usuario":self.session.usuario,
            "Fecha":date.today().strftime("%Y-%m-%d"),
            "Hora":time().strftime("%I:%M:%S"),
            "Condicion": "%s%s" % (v.value,v.notify.replace("-","")[1:]),
            "Nivel":v.nivel,
        })
        worker = Worker(Logica.nuevoReporte,**{"access_token":self.session.access_token,"data":report.toJSON()})
        worker.signals.finished.connect(self.nuevoReporteAction)
        self.threadpool.start(worker)
    
    def nuevoReporteAction(self,response):
        if isinstance(response,Exception):
            pass
        if not response["Success"] == 'true':
            pass
        
    def actualizarVariable(self,var:variable):
        self.__status = 2
        current_time =  int(self.Time.text()) if self.Time.text() != '' else self.__dispostivo.time
        self.VariablesFrame.setEnabled(False)
        self.updateState("Actualizando...",self.movie)
        self.deviceSignals.updating.emit()
        worker = Worker(Logica.ActualizarSensor, **{"access_token":self.session.access_token,"ID":self.__dispostivo.id,"Token":self.__dispostivo.token,"data":var.toJSON() })
        worker.signals.finished.connect(partial(self.actualizarVariable_Callback,var,current_time))
        self.threadpool.start(worker)

    def actualizarVariable_Callback(self,var:variable,current_time,response):
        if isinstance(response,Exception):
            self.deviceSignals.error.emit(response)
            self.updateDeviceState("Sin Conexion")
        else:
            if response["success"] == "false" :
                self.deviceSignals.error.emit(Exception("No hay acceso a internet"))
                self.updateDeviceState("Desconectado","red")
            else:
                self.updateDeviceState("Conectado","green")
                self.Last.setText(datetime.now().strftime("%d/%m/%Y %I:%M:%S %p"))
                self.__dispostivo.lastUpdate = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
                self.__variablesContainer[var.unicID].updateUI(var)
        self.VariablesFrame.setEnabled(True)
        if len(list(filter(lambda var:(not var.output) ,self.__dispostivo.variables))) == 0:
            self.updateState("¡No hay variables!",subText=None)
            self.__status = 0
        else:
            self.updateState("Actualizando en ",subText=str(current_time))
            self.__status = 1
        self.movie.stop()
        self.deviceSignals.updated.emit()

    def variablesListToJSON(self,variablesList:list):
        for var in variablesList:
            yield var.toJSON()
    
    def updateState(self,text,Movie = None,subText = ""):
        self.Time.setMovie(Movie) if not Movie is None else self.Time.setText(subText)
        self.Time.hide() if subText is None else self.Time.show()
        self.lblTime.setText(text)
        self.movie.start() if Movie != None else self.movie.stop()

    def updateDeviceState(self,text="Desconocido",color="gray"):
        self.Status.setText(text)
        self.Status.setStyleSheet("color:%s" % color)
        self.StatusCircle.setStyleSheet("background-color:%s;border-radius:5px;" % color)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            point = self.pos() + event.globalPos() - self.dragPos
            if ((point.x() <= 0 or point.x() >= self.Parent.frameSize().width() - 330 ) or (point.y() <= 0 or point.y() >= self.Parent.frameSize().height() - 200)) :
                event.ignore()
            else:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.__dispostivo.x = self.pos().x()
                self.__dispostivo.y = self.pos().y()
                self.dragPos = event.globalPos()

    def retranslateUi(self, DispositivoWidget):
        _translate = QtCore.QCoreApplication.translate
        DispositivoWidget.setWindowTitle(_translate("DispositivoWidget", "Form"))
        self.Container.setTitle(_translate("DispositivoWidget", self.__dispostivo.nombre))
        self.lblStatus.setText(_translate("DispositivoWidget", "Estado:"))
        self.lblTime.setText(_translate("DispositivoWidget", "Actualizando en "))
        self.Time.setText(_translate("DispostivoWidget", str(self.__dispostivo.time)))
        self.Status.setText(_translate("DispositivoWidget", "Desconocido"))
        self.lblLast.setText(_translate("DispositivoWidget", "Ultima Vez:"))
        self.Last.setText(_translate("DispositivoWidget", self.__dispostivo.lastUpdate))
