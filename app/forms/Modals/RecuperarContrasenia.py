from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QPixmap, QColor, QIcon
from PyQt5.QtWidgets import QMessageBox, QDialog, QApplication
from PyQt5.QtCore import Qt, QThreadPool
from classes import modal,Logica, Worker, usuario, Worker
from .CambiarContrasenia import UIContraseniaModal
from resources import *

class UIRecuperarModal(QDialog):

    def __init__(self,Parent):
        self.threadpool = QThreadPool() #QThearPool object to execute work class
        self.parent = Parent
        QDialog.__init__(self,Parent)
        self.setWindowFlags(Qt.FramelessWindowHint) # removes borders
        self.setAttribute(Qt.WA_TranslucentBackground) # Making it translucent to make a trick with the shadows
        self.setAttribute( Qt.WA_DeleteOnClose) # this should liberate ram
        self.setupUi()

    def setupUi(self):
        ContraseniaModal = self
        ContraseniaModal.setObjectName("ContraseniaModal")
        ContraseniaModal.setWindowModality(QtCore.Qt.WindowModal)
        ContraseniaModal.resize(385, 409)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ContraseniaModal.sizePolicy().hasHeightForWidth())
        ContraseniaModal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        ContraseniaModal.setFont(font)
        ContraseniaModal.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/source/img/if_16_1751363.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ContraseniaModal.setWindowIcon(icon)
        ContraseniaModal.setStyleSheet("background-color: rgb(255, 255, 255);")
        ContraseniaModal.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.verticalLayout = QtWidgets.QVBoxLayout(ContraseniaModal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainFrame = QtWidgets.QFrame(ContraseniaModal)
        self.MainFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MainFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TitleFrame = QtWidgets.QFrame(self.MainFrame)
        self.TitleFrame.setMaximumSize(QtCore.QSize(16777215, 116))
        self.TitleFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TitleFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TitleFrame.setObjectName("TitleFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.TitleFrame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lblSCADA = QtWidgets.QLabel(self.TitleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSCADA.sizePolicy().hasHeightForWidth())
        self.lblSCADA.setSizePolicy(sizePolicy)
        self.lblSCADA.setMinimumSize(QtCore.QSize(150, 116))
        self.lblSCADA.setMaximumSize(QtCore.QSize(16777215, 116))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.lblSCADA.setFont(font)
        self.lblSCADA.setAutoFillBackground(False)
        self.lblSCADA.setStyleSheet("color: rgb(255, 255, 0);background-color: rgb(65, 105, 225);\n"
"margin:0px;")
        self.lblSCADA.setObjectName("lblSCADA")
        self.gridLayout.addWidget(self.lblSCADA, 0, 1, 1, 1)
        self.ExitFrame = QtWidgets.QFrame(self.TitleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExitFrame.sizePolicy().hasHeightForWidth())
        self.ExitFrame.setSizePolicy(sizePolicy)
        self.ExitFrame.setMinimumSize(QtCore.QSize(0, 116))
        self.ExitFrame.setMaximumSize(QtCore.QSize(16777215, 116))
        self.ExitFrame.setStyleSheet("background-color: rgb(65, 105, 225);")
        self.ExitFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ExitFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ExitFrame.setLineWidth(0)
        self.ExitFrame.setObjectName("ExitFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ExitFrame)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lblIIE = QtWidgets.QLabel(self.ExitFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblIIE.sizePolicy().hasHeightForWidth())
        self.lblIIE.setSizePolicy(sizePolicy)
        self.lblIIE.setMaximumSize(QtCore.QSize(16777215, 116))
        self.lblIIE.setStyleSheet("background-color: rgb(65, 105, 225);\n"
"margin:0px;")
        self.lblIIE.setText("")
        self.lblIIE.setPixmap(QtGui.QPixmap(":/source/img/iiie.png"))
        self.lblIIE.setScaledContents(False)
        self.lblIIE.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIIE.setObjectName("lblIIE")
        self.gridLayout_4.addWidget(self.lblIIE, 0, 0, 2, 1)
        self.btnExit = QtWidgets.QPushButton(self.ExitFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy)
        self.btnExit.setMaximumSize(QtCore.QSize(32, 32))
        self.btnExit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btnExit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/source/img/Cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon1)
        self.btnExit.setIconSize(QtCore.QSize(24, 24))
        self.btnExit.setFlat(True)
        self.btnExit.setObjectName("btnExit")
        self.gridLayout_4.addWidget(self.btnExit, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.ExitFrame, 0, 2, 1, 1)
        self.lblUDB = QtWidgets.QLabel(self.TitleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblUDB.sizePolicy().hasHeightForWidth())
        self.lblUDB.setSizePolicy(sizePolicy)
        self.lblUDB.setMinimumSize(QtCore.QSize(0, 116))
        self.lblUDB.setMaximumSize(QtCore.QSize(16777215, 116))
        self.lblUDB.setStyleSheet("background-color: rgb(65, 105, 225);\n"
"margin:0px;")
        self.lblUDB.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblUDB.setText("")
        self.lblUDB.setPixmap(QtGui.QPixmap(":/source/img/logo.png"))
        self.lblUDB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblUDB.setObjectName("lblUDB")
        self.gridLayout.addWidget(self.lblUDB, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.TitleFrame)
        self.lblTitle = QtWidgets.QLabel(self.MainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle.sizePolicy().hasHeightForWidth())
        self.lblTitle.setSizePolicy(sizePolicy)
        self.lblTitle.setMaximumSize(QtCore.QSize(16777215, 38))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("margin-top:5px;")
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout_2.addWidget(self.lblTitle)
        self.ContentBox = QtWidgets.QGroupBox(self.MainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContentBox.sizePolicy().hasHeightForWidth())
        self.ContentBox.setSizePolicy(sizePolicy)
        self.ContentBox.setMinimumSize(QtCore.QSize(300, 0))
        self.ContentBox.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ContentBox.setFont(font)
        self.ContentBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ContentBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ContentBox.setFlat(True)
        self.ContentBox.setObjectName("ContentBox")
        self.ContentLayout = QtWidgets.QVBoxLayout(self.ContentBox)
        self.ContentLayout.setContentsMargins(0, 0, 0, 0)
        self.ContentLayout.setSpacing(0)
        self.ContentLayout.setObjectName("ContentLayout")
        self.ContentFrame = QtWidgets.QFrame(self.ContentBox)
        self.ContentFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ContentFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ContentFrame.setObjectName("ContentFrame")
        self.lblUsuario = QtWidgets.QLabel(self.ContentFrame)
        self.lblUsuario.setGeometry(QtCore.QRect(60, 30, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblUsuario.setFont(font)
        self.lblUsuario.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblUsuario.setObjectName("lblUsuario")
        self.btnAceptar = QtWidgets.QPushButton(self.ContentFrame)
        self.btnAceptar.setGeometry(QtCore.QRect(110, 130, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnAceptar.setFont(font)
        self.btnAceptar.setStyleSheet("border:1px solid green;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/source/img/OK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAceptar.setIcon(icon2)
        self.btnAceptar.setIconSize(QtCore.QSize(24, 24))
        self.btnAceptar.setShortcut("")
        self.btnAceptar.setCheckable(False)
        self.btnAceptar.setFlat(True)
        self.btnAceptar.setObjectName("btnAceptar")
        self.lblEmail = QtWidgets.QLabel(self.ContentFrame)
        self.lblEmail.setGeometry(QtCore.QRect(70, 75, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblEmail.setFont(font)
        self.lblEmail.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblEmail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblEmail.setObjectName("lblEmail")
        self.txtUsuario = QtWidgets.QLineEdit(self.ContentFrame)
        self.txtUsuario.setGeometry(QtCore.QRect(130, 25, 101, 21))
        self.txtUsuario.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtUsuario.setObjectName("txtUsuario")
        self.txtEmail = QtWidgets.QLineEdit(self.ContentFrame)
        self.txtEmail.setGeometry(QtCore.QRect(130, 70, 101, 21))
        self.txtEmail.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtEmail.setObjectName("txtEmail")
        self.Status = QtWidgets.QLabel(self.ContentFrame)
        self.Status.setGeometry(QtCore.QRect(120, 120, 51, 51))
        self.Status.setMaximumSize(QtCore.QSize(64, 64))
        self.Status.setText("")
        self.Status.setPixmap(QtGui.QPixmap(":/source/img/Cargando.gif"))
        self.Status.setScaledContents(True)
        self.Status.setObjectName("Status")
        self.ContentLayout.addWidget(self.ContentFrame)
        self.verticalLayout_2.addWidget(self.ContentBox, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.MainFrame)

        self.retranslateUi(ContraseniaModal)
        QtCore.QMetaObject.connectSlotsByName(ContraseniaModal)
        self.Status.hide()
        self.center()

        self.shortcut = QtWidgets.QShortcut(Qt.Key_Return,self)
        self.shortcut.activated.connect(self.btnAceptar_Click)

        # movie
        self.movie = QMovie(":/source/img/Cargando.gif") # 80 ,200
        self.movie.setScaledSize(QtCore.QSize(48,48))
        self.Status.setMovie(self.movie)
        self.Status.hide()
        
        #listener
        self.parent.signals.resize.connect(self.center)
        self.btnExit.clicked.connect(self.exit)
        self.btnAceptar.clicked.connect(self.btnAceptar_Click)

    def disconnectSignals(self):
        self.parent.signals.resize.disconnect(self.center)
        self.btnExit.clicked.disconnect(self.exit)
        self.btnAceptar.clicked.disconnect(self.btnAceptar_Click)

    def btnAceptar_Click(self):
        if self.txtUsuario.text() == "" or self.txtEmail.text() == "":
            QMessageBox.warning(self,"¡Error!","Rellene los campos solicitados")
            return
        reply = self.prompt("Confirmacion","¿Son estos datos correctos?")
        if reply == QMessageBox.Yes:
            self.btnAceptar.hide()
            self.Status.show()
            self.movie.start()
            worker = Worker(Logica.recuperarContrasenia,**{"data":{"Email":self.txtEmail.text(),"Usuario":self.txtUsuario.text(),"Password":UIRecuperarModal.randomPassword() }})
            worker.signals.finished.connect(self.validarUsuarioAction)
            self.threadpool.start(worker)

    def validarUsuarioAction(self,response):
        self.btnAceptar.show()
        self.Status.hide()
        self.movie.stop()
        if isinstance(response,Exception):
            QMessageBox.warning(self,"¡Error!",str(response))
            return
        if response["Success"] == 'false':
            QMessageBox.warning(self,'¡Error!',response["Message"])
            return
        QMessageBox.information(self,"¡Aviso!",response["Message"])
        self.close()

    def center(self): # this function is responsible for centering the modal with respect its father
        qr = self.frameGeometry()
        pr = self.parent.geometry()
        x = (self.parent.width() - qr.width()) / 2
        y = (self.parent.height() - qr.height()) / 2 
        self.setGeometry(x,y,qr.width(),qr.height())

    def exit(self): # this function is responsible to emit a cancelation signal if exit button was clicked
        reply = QMessageBox.question(
            self, "Confirmacion",
            "¿Seguro que desea cancelar?",
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            pass

    def prompt(self,title,text):
        reply = QMessageBox.question(
            self, title,
            text,
            QMessageBox.Yes | QMessageBox.No)
        return reply

    @staticmethod
    def randomPassword(lenght=12):
        import random
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        txtPass = ""
        for i in range(lenght):
            txtPass += alphabet[random.randint(0,alphabet.__len__()-1)]
        return txtPass

    def close(self):
        super().close()
        self.disconnectSignals()
        self.deleteLater()
        QApplication.processEvents()

    def retranslateUi(self, ContraseniaModal):
        _translate = QtCore.QCoreApplication.translate
        ContraseniaModal.setWindowTitle(_translate("ContraseniaModal", "Sistema SCADA"))
        self.lblSCADA.setText(_translate("ContraseniaModal", "SCADA"))
        self.lblTitle.setText(_translate("ContraseniaModal", "Recuperar Contraseña"))
        self.ContentBox.setTitle(_translate("ContraseniaModal", "Información"))
        self.lblUsuario.setText(_translate("ContraseniaModal", "Usuario:"))
        self.btnAceptar.setText(_translate("ContraseniaModal", "OK"))
        self.lblEmail.setText(_translate("ContraseniaModal", "Email:"))
