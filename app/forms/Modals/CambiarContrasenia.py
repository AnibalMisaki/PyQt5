from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QPixmap, QColor, QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from classes import modal,Logica, Worker, API
from resources import *

class UIContraseniaModal(modal):

    def __init__(self,**kwargs):
        super(UIContraseniaModal,self).__init__(**kwargs)

    def setupUI(self):
        ContraseniaModal = self
        ContraseniaModal.setObjectName("ContraseniaModal")
        ContraseniaModal.setWindowModality(QtCore.Qt.WindowModal)
        ContraseniaModal.resize(385, 454)
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
        icon.addPixmap(QtGui.QPixmap("../../../../../../../../.designer/if_16_1751363.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.lblNewPass = QtWidgets.QLabel(self.ContentFrame)
        self.lblNewPass.setGeometry(QtCore.QRect(30, 35, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblNewPass.setFont(font)
        self.lblNewPass.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblNewPass.setObjectName("lblNewPass")
        self.btnAceptar = QtWidgets.QPushButton(self.ContentFrame)
        self.btnAceptar.setGeometry(QtCore.QRect(110, 170, 71, 41))
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
        self.txtOldPass2_2 = QtWidgets.QLabel(self.ContentFrame)
        self.txtOldPass2_2.setGeometry(QtCore.QRect(19, 125, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txtOldPass2_2.setFont(font)
        self.txtOldPass2_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtOldPass2_2.setObjectName("txtOldPass2_2")
        self.txtOldPass = QtWidgets.QLabel(self.ContentFrame)
        self.txtOldPass.setGeometry(QtCore.QRect(20, 80, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txtOldPass.setFont(font)
        self.txtOldPass.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txtOldPass.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtOldPass.setObjectName("txtOldPass")
        self.txtNewPass = QtWidgets.QLineEdit(self.ContentFrame)
        self.txtNewPass.setGeometry(QtCore.QRect(170, 30, 101, 21))
        self.txtNewPass.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtNewPass.setObjectName("txtNewPass")
        self.txtNewPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtOldPass1 = QtWidgets.QLineEdit(self.ContentFrame)
        self.txtOldPass1.setGeometry(QtCore.QRect(170, 75, 101, 21))
        self.txtOldPass1.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtOldPass1.setObjectName("txtOldPass1")
        self.txtOldPass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Status = QtWidgets.QLabel(self.ContentFrame)
        self.Status.setGeometry(QtCore.QRect(120, 160, 51, 51))
        self.Status.setMaximumSize(QtCore.QSize(64, 64))
        self.Status.setText("")
        self.Status.setPixmap(QtGui.QPixmap(":/source/img/Cargando.gif"))
        self.Status.setScaledContents(True)
        self.Status.setObjectName("Status")
        self.txtOldPass2 = QtWidgets.QLineEdit(self.ContentFrame)
        self.txtOldPass2.setGeometry(QtCore.QRect(170, 120, 101, 21))
        self.txtOldPass2.setStyleSheet("border-bottom:1px solid black;border-top:none;")
        self.txtOldPass2.setObjectName("txtOldPass2")
        self.txtOldPass2.setEchoMode(QtWidgets.QLineEdit.Password)
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
        if self.txtOldPass1.text() != self.txtOldPass2.text():
            QMessageBox.warning(self,"¡Error!","¡Error! Contraseñas no coinciden")
            return
        if self.txtNewPass.text() == "" or len(self.txtNewPass.text()) < 3:
            QMessageBox.warning(self,"¡Error!","¡Error! Nueva contraseña no valida")
            return
        reply = self.prompt("Confirmacion","¿Son estos datos correctos?")
        if reply == QMessageBox.Yes:
            self.btnAceptar.hide()
            self.Status.show()
            self.movie.start()
            worker = Worker(Logica.actualizarContrasenia,**{"access_token":self.session.access_token,"data":{"Id":self.session.id,"Password":self.txtNewPass.text(),"OldPassword":self.txtOldPass1.text() }})
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
        QMessageBox.information(self,"¡Aviso!","Contraseña actualizada")
        self.close()


    def retranslateUi(self, ContraseniaModal):
        _translate = QtCore.QCoreApplication.translate
        ContraseniaModal.setWindowTitle(_translate("ContraseniaModal", "Sistema SCADA"))
        self.lblSCADA.setText(_translate("ContraseniaModal", "SCADA"))
        self.lblTitle.setText(_translate("ContraseniaModal", "Cambiar Contraseña"))
        self.ContentBox.setTitle(_translate("ContraseniaModal", "Información"))
        self.lblNewPass.setText(_translate("ContraseniaModal", "Nueva Contraseña:"))
        self.btnAceptar.setText(_translate("ContraseniaModal", "OK"))
        self.txtOldPass2_2.setText(_translate("ContraseniaModal", "Repetir Contraseña:"))
        self.txtOldPass.setText(_translate("ContraseniaModal", "Antigua Contraseña:"))
