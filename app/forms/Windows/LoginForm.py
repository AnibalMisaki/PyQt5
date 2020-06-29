from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie, QPainter, QPixmap, QKeySequence, QKeyEvent
from PyQt5.QtWidgets import QMessageBox, QApplication, QGraphicsDropShadowEffect, QMainWindow, QApplication, QShortcut
from classes import Logica, Worker, form
from ..Modals import UIRecuperarModal
from resources import *

class UILogin(form):

    def __init__(self):
        super(UILogin,self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi()

    def setupUi(self):
        Login = self
        Login.setObjectName("Login")
        Login.resize(427, 548)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Login.setFont(font)
        Login.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/source/img/if_16_1751363.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet("background-color: rgb(255, 255, 255);")
        Login.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.MainFrame = QtWidgets.QFrame(Login)
        self.MainFrame.setGeometry(QtCore.QRect(10, 10, 411, 531))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(4)
        self.shadow.setOffset(2)
        self.MainFrame.setGraphicsEffect(self.shadow)
        self.label_3 = QtWidgets.QLabel(self.MainFrame)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 71, 71))
        self.label_3.setStyleSheet("background-color: rgb(65, 105, 225);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/source/img/iiie.png"))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.MainFrame)
        self.label.setGeometry(QtCore.QRect(10, 5, 81, 101))
        self.label.setStyleSheet("background-color: rgb(65, 105, 225);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/source/img/logo.png"))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.MainFrame)
        self.frame_2.setGeometry(QtCore.QRect(40, 190, 321, 311))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(40, 50, 41, 41))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/source/img/Usuario.png"))
        self.label_6.setObjectName("label_6")
        self.txtUsuario = QtWidgets.QLineEdit(self.frame_2)
        self.txtUsuario.setGeometry(QtCore.QRect(100, 70, 141, 21))
        self.txtUsuario.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtUsuario.setObjectName("txtUsuario")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(40, 110, 51, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/source/img/Password.png"))
        self.label_7.setObjectName("label_7")
        self.txtPassword = QtWidgets.QLineEdit(self.frame_2)
        self.txtPassword.setGeometry(QtCore.QRect(100, 130, 141, 21))
        self.txtPassword.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.lblForgottenPass = QtWidgets.QLabel(self.frame_2)
        self.lblForgottenPass.setGeometry(QtCore.QRect(90, 190, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblForgottenPass.setFont(font)
        self.lblForgottenPass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lblForgottenPass.setStyleSheet("QLabel{color: rgb(0, 0, 255); }lblForgottenPass:hover{color:rgb(0,0,125);}")
        self.lblForgottenPass.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.lblForgottenPass.setObjectName("lblForgottenPass")
        self.btnAceptar = QtWidgets.QPushButton(self.frame_2)
        self.btnAceptar.setGeometry(QtCore.QRect(90, 240, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnAceptar.setFont(font)
        self.btnAceptar.setStyleSheet("border:1px solid green;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/source/img/OK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAceptar.setIcon(icon1)
        self.btnAceptar.setIconSize(QtCore.QSize(24, 24))
        self.btnAceptar.setShortcut("")
        self.btnAceptar.setCheckable(False)
        self.btnAceptar.setFlat(True)
        self.btnAceptar.setObjectName("btnAceptar")
        self.label_4 = QtWidgets.QLabel(self.MainFrame)
        self.label_4.setGeometry(QtCore.QRect(130, 140, 151, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.MainFrame)
        self.label_5.setGeometry(QtCore.QRect(50, 180, 91, 15))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.MainFrame)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(255, 255, 0);background-color: rgb(65, 105, 225);")
        self.label_2.setObjectName("label_2")
        self.btnExit = QtWidgets.QPushButton(self.MainFrame)
        self.btnExit.setGeometry(QtCore.QRect(385, 5, 24, 24))
        self.btnExit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/source/img/Cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon2)
        self.btnExit.setIconSize(QtCore.QSize(24, 24))
        self.btnExit.setFlat(True)
        self.btnExit.setObjectName("btnExit")
        self.graphicsView = QtWidgets.QGraphicsView(self.MainFrame)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 411, 116))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setStyleSheet("background-color: rgb(65, 105, 225);")
        self.graphicsView.setObjectName("graphicsView")
        self.frame_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.graphicsView.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.btnExit.raise_()
        self.center()
        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        # shorcut
        
        self.shortcut = QShortcut(Qt.Key_Return,self)
        self.shortcut.activated.connect(self.btnAceptar_Click)
        
        # movie

        self.movie = QMovie(":/source/img/Cargando.gif") # 80 ,200
        self.lblmovie = QtWidgets.QLabel(self.frame_2)
        self.lblmovie.setGeometry(QtCore.QRect(135, 235,48,48))
        self.lblmovie.setMovie(self.movie)
        self.lblmovie.hide()
        self.movie.setScaledSize(QtCore.QSize(48,48))

        # listener

        self.btnAceptar.clicked.connect(self.btnAceptar_Click)
        self.lblForgottenPass.mousePressEvent = self.mousePress_Click
        self.btnExit.clicked.connect(self.exit)
        
        # end
    
    def mousePress_Click(self,evt):
        if evt.buttons() == Qt.LeftButton:
            UI = UIRecuperarModal(self)
            UI.show()

    def btnAceptar_Click(self):
        if(self.txtUsuario.text() == "" or self.txtPassword.text() == ""):
            QMessageBox.warning(self,"¡Advertencia!","Rellene los campos solicitados")
            self.lblmovie.hide()
            self.btnAceptar.show()
            return
        self.btnAceptar.hide()
        self.lblmovie.show()
        self.movie.start()
        worker = Worker(Logica.IniciarSesion ,**{"Usuario":self.txtUsuario.text(),"Password":self.txtPassword.text()})
        worker.signals.finished.connect(self.btnAceptar_CallBack)
        self.threadpool.start(worker)

    def btnAceptar_CallBack(self,s):
        self.lblmovie.hide()
        self.btnAceptar.show()
        if isinstance(s,Exception):
            QMessageBox.information(self,"¡Error!",str(s))
            return
        if(s.id is None): # If returns None, API is online, but mongodb isnt
            QMessageBox.warning(self,"¡Error!", "No se pudo iniciar sesion")
            return
        if(s.id == ""): # If returns an empty string, credentials are bad
            QMessageBox.warning(self,"¡Error!", "Usuario y/o contraseña incorrectos")
            return
        if(s.id != "" and s.enabled == False): # If Enabled is false, then cannot login
            QMessageBox.warning(self,"¡Advertencia!", "Usuario no tiene permitido iniciar sesion")
            return
        self.txtUsuario.setText("")
        self.txtPassword.setText("")
        self.btnAceptar.clicked.disconnect(self.btnAceptar_Click)
        self.btnExit.clicked.disconnect(self.exit)
        self.signals.login.emit(s)
        self.close()
                
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
            
    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Sistema SCADA"))
        self.lblForgottenPass.setText(_translate("Login", "¿Olvidaste tu contraseña?"))
        self.btnAceptar.setText(_translate("Login", "Iniciar Sesión"))
        self.label_4.setText(_translate("Login", "Iniciar Sesión"))
        self.label_5.setText(_translate("Login", "Credenciales"))
        self.label_2.setText(_translate("Login", "SCADA"))