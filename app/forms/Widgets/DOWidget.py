from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from classes import widget, variable, variableSignals

class UIDOVariable(widget):

    def __init__(self,var:variable):
        self.__variable = var
        self.variableSignals = variableSignals()
        super(UIDOVariable,self).__init__()
        self.setupUi()

    def setupUi(self):
        DOVariable = self
        DOVariable.setObjectName("DOVariable")
        DOVariable.resize(150, 25)
        DOVariable.setMinimumSize(QtCore.QSize(150, 25))
        self.MainFrame = QtWidgets.QFrame(DOVariable)
        self.MainFrame.setGeometry(QtCore.QRect(0, 0, 150, 25))
        self.MainFrame.setMinimumSize(QtCore.QSize(150, 25))
        self.MainFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MainFrame.setLineWidth(0)
        self.MainFrame.setObjectName("MainFrame")
        self.lblTileScroll = QtWidgets.QScrollArea(self.MainFrame)
        self.lblTileScroll.setGeometry(QtCore.QRect(0, 0, 110, 25))
        self.lblTileScroll.setMinimumSize(QtCore.QSize(110, 20))
        self.lblTileScroll.setMaximumSize(QtCore.QSize(100, 25))
        self.lblTileScroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTileScroll.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblTileScroll.setLineWidth(0)
        self.lblTileScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lblTileScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lblTileScroll.setWidgetResizable(True)
        self.lblTileScroll.setObjectName("lblTileScroll")
        self.ScrollLayout = QtWidgets.QWidget()
        self.ScrollLayout.setGeometry(QtCore.QRect(0, 0, 110, 25))
        self.ScrollLayout.setObjectName("ScrollLayout")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.ScrollLayout)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.lblTitle = QtWidgets.QLabel(self.ScrollLayout)
        self.lblTitle.setMaximumSize(QtCore.QSize(16666672, 16666672))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setLineWidth(0)
        self.lblTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblTitle.setWordWrap(True)
        self.lblTitle.setIndent(5)
        self.lblTitle.setObjectName("lblTitle")
        self.vboxlayout.addWidget(self.lblTitle)
        self.lblTileScroll.setWidget(self.ScrollLayout)
        self.btnValue = QtWidgets.QPushButton(self.MainFrame)
        self.btnValue.setGeometry(QtCore.QRect(108, 3, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnValue.setFont(font)
        self.btnValue.setStyleSheet("color:white;background-color:green;")
        self.btnValue.setObjectName("btnValue")
        self.btnValue.setStyleSheet("color:white;background-color:%s" % "green" if int(self.__variable.value) >= 1 else "red")
        self.retranslateUi(DOVariable)
        QtCore.QMetaObject.connectSlotsByName(DOVariable)
        self.show()

        #listener
        self.btnValue.clicked.connect(self.valueChanged)

    def valueChanged(self):
        self.__variable.value = 0 if int(self.__variable.value) > 0 else 1
        self.variableSignals.update.emit(self.__variable)

    def updateUI(self,var:variable):
        self.__variable = var
        self.btnValue.setText("on" if int(self.__variable.value) >= 1 else "off")
        self.btnValue.setStyleSheet("color:white;background-color:%s" % "green" if int(self.__variable.value) >= 1 else "red")
    
    def getVariable(self):
        return self.__variable.toJSON()

    def disconnectSignals(self): # used to disconnect all slots to delete all references
        self.btnValue.clicked.disconnect()
        self.variableSignals.disconnect()

    def retranslateUi(self, DOVariable):
        _translate = QtCore.QCoreApplication.translate
        DOVariable.setWindowTitle(_translate("DOVariable", "Form"))
        self.lblTitle.setText(_translate("DOVariable", self.__variable.nombre))
        self.btnValue.setText(_translate("DOVariable", "on" if int(self.__variable.value) >= 1 else "off" ))
