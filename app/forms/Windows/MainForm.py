from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QMessageBox, QShortcut, QInputDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QKeySequence, QMovie
from classes import form, Worker, Logica, device, workSpace,container, session
from forms import UIAbrirModal,UIDispositivoWidget, UIConfiguracionesModal, UIDispositvoModal, UIUsuariosModal,UIReportesModal, UIAPIModal, UICuentaModal
from resources import *
from bson import ObjectId
from functools import partial

class UIMainWindow(form):

    def __init__(self):
        super(UIMainWindow,self).__init__()
        self.__containers = dict()
        self.setupUi()
        self.session = session()

    def setupUi(self):
        MainWindow = self
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 740)
        MainWindow.setMinimumSize(QtCore.QSize(840, 740))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/source/img/if_16_1751363.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.MainFrame = QtWidgets.QWidget(MainWindow)
        self.MainFrame.setStyleSheet("")
        self.MainFrame.setObjectName("MainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ContainerFrame = QtWidgets.QFrame(self.MainFrame)
        self.ContainerFrame.setStyleSheet("background-color: rgb(255, 255, 255);\n""")
        self.ContainerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ContainerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ContainerFrame.setObjectName("ContainerFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ContainerFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TitileLayout = QtWidgets.QGridLayout()
        self.TitileLayout.setSpacing(0)
        self.TitileLayout.setObjectName("TitileLayout")
        self.lblIIE = QtWidgets.QLabel(self.ContainerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblIIE.sizePolicy().hasHeightForWidth())
        self.lblIIE.setSizePolicy(sizePolicy)
        self.lblIIE.setStyleSheet("background-color: rgb(65, 105, 225);\n""margin:0px;")
        self.lblIIE.setText("")
        self.lblIIE.setPixmap(QtGui.QPixmap(":/source/img/iiie.png"))
        self.lblIIE.setObjectName("lblIIE")
        self.TitileLayout.addWidget(self.lblIIE, 0, 0, 1, 1)
        self.lblSCADA = QtWidgets.QLabel(self.ContainerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSCADA.sizePolicy().hasHeightForWidth())
        self.lblSCADA.setSizePolicy(sizePolicy)
        self.lblSCADA.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.lblSCADA.setFont(font)
        self.lblSCADA.setAutoFillBackground(False)
        self.lblSCADA.setStyleSheet("color: rgb(255, 255, 0);background-color: rgb(65, 105, 225);\n margin:0px;")
        self.lblSCADA.setObjectName("lblSCADA")
        self.TitileLayout.addWidget(self.lblSCADA, 0, 1, 1, 1)
        self.lblLogo = QtWidgets.QLabel(self.ContainerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLogo.sizePolicy().hasHeightForWidth())
        self.lblLogo.setSizePolicy(sizePolicy)
        self.lblLogo.setStyleSheet("background-color: rgb(65, 105, 225);\n margin:0px;")
        self.lblLogo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap(":/source/img/logo.png"))
        self.lblLogo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblLogo.setObjectName("lblLogo")
        self.TitileLayout.addWidget(self.lblLogo, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.TitileLayout)
        self.ContentLayout = QtWidgets.QVBoxLayout()
        self.ContentLayout.setSpacing(0)
        self.ContentLayout.setObjectName("ContentLayout")
        self.MenuFrame = QtWidgets.QFrame(self.ContainerFrame)
        self.MenuFrame.setMinimumSize(QtCore.QSize(0, 24))
        self.MenuFrame.setStyleSheet("margin:0px;")
        self.MenuFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MenuFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MenuFrame.setLineWidth(0)
        self.MenuFrame.setObjectName("MenuFrame")
        self.MenuArchivo = QtWidgets.QToolButton(self.MenuFrame)
        self.MenuArchivo.setGeometry(QtCore.QRect(0, 0, 71, 24))
        self.MenuArchivo.setStyleSheet("margin:0px;")
        self.MenuArchivo.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.MenuArchivo.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.MenuArchivo.setAutoRaise(True)
        self.MenuArchivo.setArrowType(QtCore.Qt.NoArrow)
        self.MenuArchivo.setObjectName("MenuArchivo")
        self.MenuConfiguraciones = QtWidgets.QToolButton(self.MenuFrame)
        self.MenuConfiguraciones.setGeometry(QtCore.QRect(70, 0, 121, 24))
        self.MenuConfiguraciones.setStyleSheet("margin:0px;")
        self.MenuConfiguraciones.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.MenuConfiguraciones.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.MenuConfiguraciones.setAutoRaise(True)
        self.MenuConfiguraciones.setArrowType(QtCore.Qt.NoArrow)
        self.MenuConfiguraciones.setObjectName("MenuConfiguraciones")
        self.MenuReportes = QtWidgets.QToolButton(self.MenuFrame)
        self.MenuReportes.setGeometry(QtCore.QRect(190, 0, 91, 24))
        self.MenuReportes.setStyleSheet("margin:0px;")
        self.MenuReportes.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.MenuReportes.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.MenuReportes.setAutoRaise(True)
        self.MenuReportes.setArrowType(QtCore.Qt.NoArrow)
        self.MenuReportes.setObjectName("MenuReportes")
        self.ContentLayout.addWidget(self.MenuFrame)
        self.workSpaceTab = QtWidgets.QTabWidget(self.ContainerFrame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.workSpaceTab.setFont(font)
        self.workSpaceTab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.workSpaceTab.setElideMode(QtCore.Qt.ElideLeft)
        #self.workSpaceTab.setTabsClosable(True)
        self.workSpaceTab.setMovable(True)
        self.workSpaceTab.setObjectName("workSpaceTab")
        self.workSpace1 = QtWidgets.QWidget()
        self.workSpace1.setObjectName("workSpace1")
        self.workSpaceTab.addTab(self.workSpace1, "")
        self.WorkSpace2 = QtWidgets.QWidget()
        self.WorkSpace2.setObjectName("WorkSpace2")
        self.workSpaceTab.addTab(self.WorkSpace2, "")
        self.ContentLayout.addWidget(self.workSpaceTab)
        self.verticalLayout_2.addLayout(self.ContentLayout)
        self.StatusFrame = QtWidgets.QFrame(self.ContainerFrame)
        self.StatusFrame.setMinimumSize(QtCore.QSize(0, 24))
        self.StatusFrame.setStyleSheet("margin:0px;")
        self.StatusFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.StatusFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StatusFrame.setLineWidth(0)
        self.StatusFrame.setObjectName("StatusFrame")
        self.lblStatus = QtWidgets.QLabel(self.StatusFrame)
        self.lblStatus.setGeometry(QtCore.QRect(5, 2, 54, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblStatus.setFont(font)
        self.lblStatus.setLineWidth(0)
        self.lblStatus.setScaledContents(False)
        self.lblStatus.setObjectName("lblStatus")
        self.Status = QtWidgets.QLabel(self.StatusFrame)
        self.Status.setGeometry(QtCore.QRect(65, 4, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Status.setFont(font)
        self.Status.setStyleSheet("color: rgb(0, 170, 127);")
        self.Status.setLineWidth(0)
        self.Status.setScaledContents(False)
        self.Status.setAlignment(QtCore.Qt.AlignLeft)
        self.Status.setObjectName("Status")
        self.StatusCircle = QtWidgets.QLabel(self.StatusFrame)
        self.StatusCircle.setGeometry(QtCore.QRect(50, 7, 12, 12))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.StatusCircle.setFont(font)
        self.StatusCircle.setStyleSheet("background-color:green; border-radius:5px;")
        self.StatusCircle.setLineWidth(0)
        self.StatusCircle.setText("")
        self.StatusCircle.setScaledContents(False)
        self.StatusCircle.setAlignment(QtCore.Qt.AlignCenter)
        self.StatusCircle.setObjectName("StatusCircle")
        self.verticalLayout_2.addWidget(self.StatusFrame)
        self.verticalLayout.addWidget(self.ContainerFrame)
        MainWindow.setCentralWidget(self.MainFrame)
        self.retranslateUi(MainWindow)
        self.workSpaceTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Shortcuts

        self.shortcut_new = QShortcut(QKeySequence(Qt.CTRL+Qt.Key_N),self)
        self.shortcut_new.activated.connect(self.MenuNuevo_Click)
        self.shortcut_open = QShortcut(QKeySequence(Qt.CTRL+Qt.Key_A),self)
        self.shortcut_open.activated.connect(self.MenuAbrir_Click)
        self.shortcut_save = QShortcut(QKeySequence(Qt.CTRL+Qt.Key_S),self)
        self.shortcut_save.activated.connect(self.MenuGuardar_Click)
        self.shortcut_saveAs = QShortcut(QKeySequence(Qt.CTRL+Qt.Key_G),self)
        self.shortcut_saveAs.activated.connect(self.MenuGuardarComo_Click)
        self.shortcut_close = QShortcut(QKeySequence(Qt.CTRL+Qt.Key_E),self)
        self.shortcut_close.activated.connect(self.MenuCerrar_Click)
        self.shortcut_delete = QShortcut(QKeySequence(Qt.CTRL+Qt.Key_X),self)
        self.shortcut_delete.activated.connect(self.MenuEliminar_Click)
        self.shortcut_logout = QShortcut(QKeySequence(Qt.CTRL+Qt.Key_Z),self)
        self.shortcut_logout.activated.connect(self.MenuCerrarSesion_Click)
        self.shortcut_exit = QShortcut(QKeySequence(Qt.Key_Alt+Qt.Key_F4),self)
        self.shortcut_exit.activated.connect(self.MenuSalir_Click)

        self.shortcut_settings = QShortcut(QKeySequence(Qt.CTRL+Qt.Key_C),self)
        self.shortcut_settings.activated.connect(self.MenuConfiguraciones_Click)
        self.shortcut_devices = QShortcut(QKeySequence(Qt.CTRL+Qt.Key_D),self)
        self.shortcut_devices.activated.connect(self.MenuDispositivos_Click)
        self.shortcut_api = QShortcut(QKeySequence(Qt.CTRL+Qt.Key_H),self)
        self.shortcut_api.activated.connect(self.MenuAPI_Click)
        self.shortcut_users = QShortcut(QKeySequence(Qt.CTRL+Qt.Key_U),self)
        self.shortcut_users.activated.connect(self.MenuUsuarios_Click)
        self.shortcut_account = QShortcut(QKeySequence(Qt.CTRL+Qt.Key_P),self)
        self.shortcut_account.activated.connect(self.MenuCuenta_Click)

        self.shortcut_reportes = QShortcut(QKeySequence(Qt.CTRL+Qt.Key_R),self)
        self.shortcut_reportes.activated.connect(self.MenuReportes_Click)
        
        self.movie = QMovie(":/source/img/Cargando.gif") # 80 ,200
        self.movie.setScaledSize(QtCore.QSize(20,20))

        # define Menus
        self.defineMenuArchivo()
        self.defineMenuConfiguraciones()
        self.defineMenuReportes()
            
        # listener

    def defineMenuArchivo(self):
        # Definicion de menus
        archivoMenu = QMenu()
        archivoMenu.addAction("{:15s}{:>16s}".format("Nuevo","Ctrl+N"),self.MenuNuevo_Click)
        archivoMenu.addAction("{:15s}{:>19s}".format("Abrir","Ctrl+A"),self.MenuAbrir_Click)
        archivoMenu.addAction("{:15s}{:>15s}".format("Guardar","Ctrl+S"),self.MenuGuardar_Click)
        archivoMenu.addAction("{:15s}{:>8s}".format("Guardar Como","Ctrl+G"),self.MenuGuardarComo_Click)
        archivoMenu.addAction("{:15s}{:>17s}".format("Cerrar","Ctrl+E"),self.MenuCerrar_Click)
        archivoMenu.addAction("{:15s}{:>16s}".format("Eliminar","Ctrl+X"), self.MenuEliminar_Click)
        archivoMenu.addAction("{:15s}{:>11s}".format("Cerrar Sesión","Ctrl+Z"),self.MenuCerrarSesion_Click)
        archivoMenu.addAction("{:15s}{:>19s}".format("Salir","Alt+f4"),self.MenuSalir_Click)

        self.MenuArchivo.setMenu(archivoMenu)
        defaultAction = QAction("Abrir",self)
        defaultAction.triggered.connect(self.MenuAbrir_Click)
        self.MenuArchivo.setDefaultAction(defaultAction)

    def defineMenuConfiguraciones(self):
        configuracionesMenu = QMenu()
        configuracionesMenu.addAction("{:15s}{:>12s}".format("Configuraciones","Ctrl+C"),self.MenuConfiguraciones_Click)
        configuracionesMenu.addAction("{:15s}{:>17s}".format("Dispostivos","Ctrl+D"),self.MenuDispositivos_Click)
        configuracionesMenu.addAction("{:15s}{:>19s}".format("API Local","Ctrl+H"),self.MenuAPI_Click)
        configuracionesMenu.addAction("{:15s}{:>19s}".format("Usuarios","Ctrl+U"),self.MenuUsuarios_Click)
        configuracionesMenu.addAction("{:15s}{:>20s}".format("Cuenta","Ctrl+P"),self.MenuCuenta_Click)
        configuracionesMenu.addAction("{:15s}{:>20s}".format("Acerca de",""), self.MenuAcerca_Click)

        self.MenuConfiguraciones.setMenu(configuracionesMenu)
        defaultAction = QAction("Dispositivos",self)
        defaultAction.triggered.connect(self.MenuDispositivos_Click)
        self.MenuConfiguraciones.setDefaultAction(defaultAction)

    def defineMenuReportes(self):

        ReportesMenu = QMenu()
        ReportesMenu.addAction("{:15s}{:>10s}".format("Reportes","Ctrl+R"),self.MenuReportes_Click)
        
        self.MenuReportes.setMenu(ReportesMenu)
        defaultAction = QAction("Reportes",self)
        defaultAction.triggered.connect(self.MenuReportes_Click)
        self.MenuReportes.setDefaultAction(defaultAction)

    # Menu Archivo

    def MenuNuevo_Click(self):
        name = QInputDialog.getText(self,"Nombre","Ingrese nombre del proyecto")
        if not all(name):
            return
        work = workSpace({"Id":ObjectId().__str__(),"Nombre":name[0],"Devices":None,"DriversCount":0})
        tabName = self.workSpaceTab.currentWidget().objectName()
        if tabName in self.__containers.keys():
            reply = QMessageBox.question(
            self, "Confirmacion",
            "¿Seguro? Esto sobreescribira el proyecto actual",
            QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.No:
                return
        containerObject = container({"tab":self.workSpaceTab.currentWidget(),"workSpace":work,"devicesContainer":dict()  })
        self.__containers[tabName] = containerObject
        self.workSpaceTab.setTabText(self.workSpaceTab.indexOf(self.workSpaceTab.currentWidget()),work.nombre)
    
    def MenuAbrir_Click(self):
        dialog = UIAbrirModal(**{"Parent":self,"IsDelete":False})
        print(dialog)
        dialog.show()
        dialog.signals.success.connect(self.AbrirAction)

    def AbrirAction(self,workSpace):
        worker = Worker(Logica.AbrirProyecto,**{"access_token":self.session.access_token,"id":workSpace.id})
        worker.signals.finished.connect(self.MostrarDispositivos)
        self.threadpool.start(worker)

    def MenuGuardar_Click(self):
        tabName = self.workSpaceTab.currentWidget().objectName()
        if tabName not in self.__containers.keys():
            QMessageBox.warning(self,"¡Error!","¡Error! No hay datos que guardar\nAbra un proyecto(Ctrl+A) o cree uno nuevo(Ctrl+N)")
            return
        self.actualizarEstado("Guardando...","white","slategray",self.movie)
        workSpace = self.serializeWorkSpace(self.workSpaceTab.currentWidget().objectName())
        worker = Worker(Logica.Guardar,**{"access_token":self.session.access_token,"data":workSpace})
        worker.signals.finished.connect(self.GuardarAction)
        self.threadpool.start(worker)
    
    def MenuGuardarComo_Click(self):
        tabName = self.workSpaceTab.currentWidget().objectName()
        if tabName not in self.__containers.keys():
            QMessageBox.warning(self,"¡Error!","¡Error! No hay datos que guardar\nAbra un proyecto(Ctrl+A) o cree uno nuevo(Ctrl+N)")
            return
        name = QInputDialog.getText(self,"Nombre","Ingrese nombre del proyecto")
        if not all(name):
            return
        workSpace = self.__containers[self.workSpaceTab.currentWidget().objectName()].workSpace
        workSpace.id = ObjectId().__str__()
        workSpace.nombre = name[0]
        self.workSpaceTab.setTabText(self.workSpaceTab.indexOf(self.workSpaceTab.currentWidget()),workSpace.nombre)
        workSpace = self.serializeWorkSpace(self.workSpaceTab.currentWidget().objectName())
        worker = Worker(Logica.Guardar,**{"access_token":self.session.access_token,"data":workSpace})
        worker.signals.finished.connect(self.GuardarAction)
        self.threadpool.start(worker)
    
    def MenuCerrar_Click(self):
        tabName = self.workSpaceTab.currentWidget().objectName()
        if tabName not in self.__containers.keys():
            QMessageBox.warning(self,"¡Error!","¡Error! No hay nada en esta pestaña\nAbra un proyecto(Ctrl+A) o cree uno nuevo(Ctrl+N)")
            return
        reply = QMessageBox.question(
        self, "Confirmacion",
        "¿Guardar antes de cerrar?",
        QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel  )
        if reply == QMessageBox.Save:
            self.actualizarEstado("Guardando...","white","slategray",self.movie)
            workSpace = self.serializeWorkSpace(tabName)
            worker = Worker(Logica.Guardar,**{"access_token":self.session.access_token,"data":workSpace})
            worker.signals.finished.connect(partial(self.GuardarAction,IsClose=True,Tab=self.workSpaceTab.currentWidget()))
            self.threadpool.start(worker)
        if reply == QMessageBox.No:
            self.cleanWorkSpace(self.workSpaceTab.currentWidget().objectName())
            self.__containers.pop(tabName)
            self.workSpaceTab.setTabText(self.workSpaceTab.indexOf(self.workSpaceTab.currentWidget()),"Tab %s" % (self.workSpaceTab.indexOf(self.workSpaceTab.currentWidget()) + 1) )
    
    def GuardarAction(self,response,IsClose = False,Tab = None):
        from datetime import datetime
        if isinstance(response,Exception):
            self.actualizarEstado("¡Error! Fallo al contactar con el servicio SCADA a las %s" % datetime.now().strftime("%I:%M del dia %d/%m"),"red","red")
            if IsClose:
                QMessageBox.warning(self,"¡Error!","¡Error! Fallo al guardar, La operacion (Cerrar) no ha sido completada") 
            return
        if response["Success"] == 'true':
            self.actualizarEstado("¡Exito! Guardado exitoso a las %s" % datetime.now().strftime("%I:%M del dia %d/%m"),"green","green")
            if IsClose:
                self.cleanWorkSpace(Tab.objectName())
                self.__containers.pop(Tab.objectName())
                self.workSpaceTab.setTabText(self.workSpaceTab.indexOf(Tab),"Tab %s" % (self.workSpaceTab.indexOf(Tab) + 1))
                
        else:
            self.actualizarEstado("¡Error! Fallo al guardar a las %s" % datetime.now().strftime("%I:%M del dia %d/%m"),"red","red")
            if IsClose:
                QMessageBox.warning(self,"¡Error!","¡Error! Fallo al guardar, La operacion (Cerrar) no ha sido completada") 

    def MenuEliminar_Click(self):
        dialog = UIAbrirModal(**{"Parent":self,"IsDelete":True})
        dialog.show()
        dialog.signals.success.connect(self.EliminarAction)

    def EliminarAction(self,workSpace):
        for x in self.__containers.items():
           if x[1].workSpace.id == workSpace.id:
               QMessageBox.warning(self,"¡Error!","¡Error! El proyecto que intenta eliminar se encuentra abierto\nCierre dicho proyecto antes de continuar")
               return
        self.actualizarEstado("Eliminado...","white","slategray",self.movie)
        worker = Worker(Logica.EliminarProyecto,**{"access_token":self.session.access_token,"id":workSpace.id})
        worker.signals.finished.connect(self.EliminarAction_Callback)
        self.threadpool.start(worker)
    
    def EliminarAction_Callback(self,response):
        from datetime import datetime
        if isinstance(response,Exception):
            self.actualizarEstado("¡Error! Fallo al contactar con el servicio SCADA a las %s, No se pudo eliminar" % datetime.now().strftime("%I:%M del dia %d/%m"),"red","red")
            return
        if response["Success"] == 'true':
            self.actualizarEstado("¡Exito! Eliminado exitosamente a las %s" % datetime.now().strftime("%I:%M del dia %d/%m"),"green","green")
        else:
            self.actualizarEstado("¡Error! Fallo al Eliminar a las %s" % datetime.now().strftime("%I:%M del dia %d/%m"),"red","red")

    def MenuCerrarSesion_Click(self):
        reply = QMessageBox.question(
            self, "Confirmacion",
            "¿Cerrar Sesiòn?",
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.signals.logout.emit()
            self.close()

    def MenuSalir_Click(self):
        reply = QMessageBox.question(
            self, "Confirmacion",
            "¿Seguro que desea salir?",
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()

    # Menu archivo

    # methods of settings:menu
    def MenuConfiguraciones_Click(self):
        UI = UIConfiguracionesModal(**{"Parent":self})
        UI.show()

    def MenuDispositivos_Click(self):
        UI = UIDispositvoModal(**{"Parent":self,"workSpaces":self.__containers})
        UI.show()

    def MenuAPI_Click(self):
        UI = UIAPIModal(**{"Parent":self})
        UI.show()

    def MenuUsuarios_Click(self):
        UI = UIUsuariosModal(**{"Parent":self})
        UI.show()
    
    def MenuCuenta_Click(self):
        UI = UICuentaModal(**{"Parent":self})
        UI.show()
    
    def MenuAcerca_Click(self):
        print("about")

    # methods of reports:menu
    def MenuReportes_Click(self):
        UIReportes = UIReportesModal(**{"Parent":self})
        UIReportes.show()
        
    # utils Methods

    def MostrarDispositivos(self,workSpace:workSpace):
        if isinstance(workSpace,Exception):
            QMessageBox.warning(self,"¡Error!", "Fallo al cargar el proyecto")
            return
        tabName = self.workSpaceTab.currentWidget().objectName()
        for x in self.__containers.items():
            if x[1].workSpace.id == workSpace.id:
                QMessageBox.warning(self,"Advertencia","¡Error! Proyecto ya ha sido abierto")
                return
        if tabName in self.__containers.keys():
            reply = QMessageBox.question(
            self, "Confirmacion",
            "¿Seguro? Esto sobreescribira el proyecto actual",
            QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.No:
                return
        self.workSpaceTab.setTabText(self.workSpaceTab.indexOf(self.workSpaceTab.currentWidget()),workSpace.nombre)
        self.paintDevices(workSpace)

    def paintDevices(self,workSpace:workSpace):
        devices = workSpace.devices
        parent = self.workSpaceTab.currentWidget()
        devicesContainer = dict()
        for device in devices:
            UIDevice = UIDispositivoWidget(parent,device)
            devicesContainer[device.unicID] = UIDevice
        containerObject = container({"tab":self.workSpaceTab.currentWidget(),"workSpace":workSpace,"devicesContainer":devicesContainer })
        self.__containers[parent.objectName()] = containerObject

    def serializeWorkSpace(self,tabName):
        workSpace = self.__containers[tabName].workSpace.toJSON()
        return workSpace

    def cleanWorkSpace(self,tabName):
        for d in self.__containers[tabName].devicesContainer.items():
            device = d[1]
            device.close()
            del device
        QtWidgets.QApplication.processEvents()

    def actualizarEstado(self,text,backColor = "white",color = "green",movie = None):
        self.movie.start() if movie != None else self.movie.stop()
        self.StatusCircle.setMovie(movie)
        self.Status.setText(text)
        self.Status.setStyleSheet("color:%s;" % color)
        self.StatusCircle.setMovie(movie)
        self.StatusCircle.setStyleSheet("background-color:%s; border-radius:5px;" % backColor)

    def closeEvent(self,event): # asks if user wants to close application
        if (event.spontaneous()) == False: 
            event.accept() 
            return
        self.exit(event)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Software SCADA"))
        self.lblSCADA.setText(_translate("MainWindow", "SCADA"))
        self.MenuArchivo.setText(_translate("MainWindow", "Archivo"))
        self.MenuConfiguraciones.setText(_translate("MainWindow", "Configuraciones"))
        self.MenuReportes.setText(_translate("MainWindow", "Reportes"))
        self.workSpaceTab.setTabText(self.workSpaceTab.indexOf(self.workSpace1), _translate("MainWindow", "Tab 1"))
        self.workSpaceTab.setTabText(self.workSpaceTab.indexOf(self.WorkSpace2), _translate("MainWindow", "Tab 2"))
        self.lblStatus.setText(_translate("MainWindow", "Estado:"))
        self.Status.setText(_translate("MainWindow", "En linea"))