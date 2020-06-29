from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from classes import widget, variable, variableSignals, Logica

class UIAIVariable(widget):

    def __init__(self,var:variable):
        self.__variable = var
        super(UIAIVariable,self).__init__()
        self.setupUi()

    def setupUi(self):
        AIVariable = self
        AIVariable.setObjectName("AIVariable")
        AIVariable.resize(150, 25)
        AIVariable.setMinimumSize(QtCore.QSize(150, 25))
        self.MainFrame = QtWidgets.QFrame(AIVariable)
        self.MainFrame.setGeometry(QtCore.QRect(0, 0, 150, 25))
        self.MainFrame.setMinimumSize(QtCore.QSize(150, 25))
        self.MainFrame.setMaximumSize(QtCore.QSize(150, 25))
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
        self.lblValue = QtWidgets.QLabel(self.MainFrame)
        self.lblValue.setGeometry(QtCore.QRect(110, 0, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblValue.setFont(font)
        self.lblValue.setStyleSheet("padding-top:5px;")
        self.lblValue.setLineWidth(0)
        self.lblValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblValue.setIndent(-1)
        self.lblValue.setObjectName("lblValue")

        self.retranslateUi(AIVariable)
        QtCore.QMetaObject.connectSlotsByName(AIVariable)
        self.show()

    def updateUI(self,var:variable):
        self.__variable = var
        self.lblValue.setText(str(self.__variable.value))

    def getVariable(self):
        return self.__variable.toJSON()
    
    def disconnectSignals(self): # used to disconnect all slots to delete all references
        pass

    def retranslateUi(self, AIVariable):
        _translate = QtCore.QCoreApplication.translate
        AIVariable.setWindowTitle(_translate("AIVariable", "Form"))
        self.lblTitle.setText(_translate("AIVariable", self.__variable.nombre))
        self.lblValue.setText(_translate("AIVariable", self.__variable.value.__str__()))