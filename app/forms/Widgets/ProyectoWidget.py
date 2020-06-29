from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from classes import widget, workSpace
from functools import partial
from resources import *

class UIWidgetP(widget):

    def __init__(self, workSpace:workSpace,IsDelete = False):
        self.__IsDelete = IsDelete
        self.__workSpace = workSpace
        super(UIWidgetP,self).__init__()
        self.setupUi()

    def setupUi(self):
        Form = self
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(350, 96)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ProjectFrame = QtWidgets.QFrame(Form)
        self.ProjectFrame.setGeometry(QtCore.QRect(0, 0, 350, 96))
        self.ProjectFrame.setMinimumSize(QtCore.QSize(350, 96))
        self.ProjectFrame.setMaximumSize(QtCore.QSize(16777215, 96))
        self.ProjectFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProjectFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ProjectFrame.setObjectName("ProjectFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.ProjectFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.ProjectTitle = QtWidgets.QTextBrowser(self.ProjectFrame)
        self.ProjectTitle.setMaximumSize(QtCore.QSize(161, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ProjectTitle.setFont(font)
        self.ProjectTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ProjectTitle.setLineWidth(0)
        self.ProjectTitle.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ProjectTitle.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ProjectTitle.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.ProjectTitle.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.ProjectTitle.setDocumentTitle("")
        self.ProjectTitle.setOverwriteMode(False)
        self.ProjectTitle.setAcceptRichText(True)
        self.ProjectTitle.setOpenLinks(False)
        self.ProjectTitle.setObjectName("ProjectTitle")
        self.gridLayout.addWidget(self.ProjectTitle, 0, 0, 1, 1)
        self.btnAbrirFrame = QtWidgets.QFrame(self.ProjectFrame)
        self.btnAbrirFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.btnAbrirFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btnAbrirFrame.setLineWidth(0)
        self.btnAbrirFrame.setObjectName("btnAbrirFrame")
        self.btnAbrirLayout = QtWidgets.QVBoxLayout(self.btnAbrirFrame)
        self.btnAbrirLayout.setContentsMargins(0, 0, 0, 0)
        self.btnAbrirLayout.setSpacing(0)
        self.btnAbrirLayout.setObjectName("btnAbrirLayout")
        self.btnAbrir = QtWidgets.QPushButton(self.btnAbrirFrame)
        self.btnAbrir.setMinimumSize(QtCore.QSize(91, 31))
        self.btnAbrir.setMaximumSize(QtCore.QSize(91, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnAbrir.setFont(font)
        self.btnAbrir.setStyleSheet("border: 1px solid green;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/source/img/Abrir.png" if not self.__IsDelete else ":/source/img/Eliminar-SM.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAbrir.setIcon(icon)
        self.btnAbrir.setFlat(True)
        self.btnAbrir.setObjectName("btnAbrir")
        self.btnAbrirLayout.addWidget(self.btnAbrir, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.btnAbrirFrame, 0, 1, 2, 1)
        self.lblCount = QtWidgets.QLabel(self.ProjectFrame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblCount.setFont(font)
        self.lblCount.setObjectName("lblCount")
        self.gridLayout.addWidget(self.lblCount, 1, 0, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #listener
        self.btnAbrir.clicked.connect(partial(self.sucess,self.__workSpace,"¿Abrir este proyecto?" if not self.__IsDelete else "¿Eliminar este proyecto?"))

    def sizeHint(self):
        return QtCore.QSize(350,96)
    
    def disconnectSignals(self):
        self.btnAbrir.clicked.disconnect()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lblCount.setText(_translate("Form", "Contiene %s Controladores" % self.__workSpace.devicesCount))
        self.ProjectTitle.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\';\">%s</span></p></body></html>") % self.__workSpace.nombre )
        self.btnAbrir.setText(_translate("Form", "Abrir" if not self.__IsDelete else "Eliminar" ))
