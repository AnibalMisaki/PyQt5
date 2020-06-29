from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from classes import widget, variable, variableSignals

class UIAOVariable(widget):

    def __init__(self,var:variable):
        self.__variable = var
        self.variableSignals = variableSignals()
        super(UIAOVariable,self).__init__()
        self.setupUi()

    def setupUi(self):
        AOVariable = self
        AOVariable.setObjectName("AOVariable")
        AOVariable.resize(150, 25)
        AOVariable.setMinimumSize(QtCore.QSize(150, 25))
        self.MainFrame = QtWidgets.QFrame(AOVariable)
        self.MainFrame.setGeometry(QtCore.QRect(0, 0, 150, 25))
        self.MainFrame.setMinimumSize(QtCore.QSize(150, 25))
        self.MainFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MainFrame.setLineWidth(0)
        self.MainFrame.setObjectName("MainFrame")
        self.lblTileScroll = QtWidgets.QScrollArea(self.MainFrame)
        self.lblTileScroll.setGeometry(QtCore.QRect(0, 0, 100, 25))
        self.lblTileScroll.setMinimumSize(QtCore.QSize(100, 20))
        self.lblTileScroll.setMaximumSize(QtCore.QSize(100, 25))
        self.lblTileScroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTileScroll.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblTileScroll.setLineWidth(0)
        self.lblTileScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lblTileScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lblTileScroll.setWidgetResizable(True)
        self.lblTileScroll.setObjectName("lblTileScroll")
        self.ScrollLayout = QtWidgets.QWidget()
        self.ScrollLayout.setGeometry(QtCore.QRect(0, 0, 100, 25))
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
        self.SpinValue = QtWidgets.QDoubleSpinBox(self.MainFrame)
        self.SpinValue.setGeometry(QtCore.QRect(100, 0, 50, 24))
        self.SpinValue.setFrame(True)
        self.SpinValue.setReadOnly(False)
        self.SpinValue.setDecimals(0)
        self.SpinValue.setMaximum(255.0)
        self.SpinValue.setProperty("value", self.__variable.value)
        self.SpinValue.setObjectName("SpinValue")

        self.retranslateUi(AOVariable)
        QtCore.QMetaObject.connectSlotsByName(AOVariable)
        self.show()

        #listener
        self.SpinValue.valueChanged.connect(self.valueChanged)
        #self.SpinValue.va

    def valueChanged(self):
        self.__variable.value = int(self.SpinValue.value())
        self.variableSignals.update.emit(self.__variable)

    def updateUI(self,var:variable):
        self.__variable = var
        self.SpinValue.setProperty("value", str(self.__variable.value))

    def getVariable(self):
        return self.__variable.toJSON()
    
    def disconnectSignals(self): # used to disconnect all slots to delete all references
        self.SpinValue.valueChanged.disconnect(self.valueChanged)
        self.variableSignals.disconnect()

    def retranslateUi(self, AOVariable):
        _translate = QtCore.QCoreApplication.translate
        AOVariable.setWindowTitle(_translate("AOVariable", "Form"))
        self.lblTitle.setText(_translate("AOVariable", self.__variable.nombre))
