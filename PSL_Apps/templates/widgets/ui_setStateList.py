# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PSL_Apps/templates/widgets/setStateList.ui'
#
# Created: Mon Jul 11 21:45:34 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(104, 105)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(100, 105))
        Form.setMaximumSize(QtCore.QSize(104, 105))
        Form.setStyleSheet(_fromUtf8("QFrame.PeripheralCollection{\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border: 1px solid black;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 rgb(97, 146, 121), stop: 0.5 rgb(65, 89, 111));\n"
"\n"
"}\n"
"\n"
"QLabel,QCheckBox {\n"
"color: white;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"}\n"
""))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widgetFrameOuter = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFrameOuter.sizePolicy().hasHeightForWidth())
        self.widgetFrameOuter.setSizePolicy(sizePolicy)
        self.widgetFrameOuter.setMinimumSize(QtCore.QSize(80, 0))
        self.widgetFrameOuter.setStyleSheet(_fromUtf8(""))
        self.widgetFrameOuter.setFrameShape(QtGui.QFrame.StyledPanel)
        self.widgetFrameOuter.setFrameShadow(QtGui.QFrame.Raised)
        self.widgetFrameOuter.setObjectName(_fromUtf8("widgetFrameOuter"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widgetFrameOuter)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setContentsMargins(3, 2, 3, 3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.title = QtGui.QLabel(self.widgetFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.verticalLayout_3.addWidget(self.title)
        self.ImageFrame = QtGui.QFrame(self.widgetFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageFrame.sizePolicy().hasHeightForWidth())
        self.ImageFrame.setSizePolicy(sizePolicy)
        self.ImageFrame.setMinimumSize(QtCore.QSize(90, 70))
        self.ImageFrame.setStyleSheet(_fromUtf8(""))
        self.ImageFrame.setObjectName(_fromUtf8("ImageFrame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.ImageFrame)
        self.gridLayout_3.setContentsMargins(0, 3, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.B1 = QtGui.QCheckBox(self.ImageFrame)
        self.B1.setObjectName(_fromUtf8("B1"))
        self.gridLayout_3.addWidget(self.B1, 0, 0, 1, 1)
        self.B3 = QtGui.QCheckBox(self.ImageFrame)
        self.B3.setObjectName(_fromUtf8("B3"))
        self.gridLayout_3.addWidget(self.B3, 2, 0, 1, 1)
        self.B4 = QtGui.QCheckBox(self.ImageFrame)
        self.B4.setObjectName(_fromUtf8("B4"))
        self.gridLayout_3.addWidget(self.B4, 3, 0, 1, 1)
        self.B2 = QtGui.QCheckBox(self.ImageFrame)
        self.B2.setObjectName(_fromUtf8("B2"))
        self.gridLayout_3.addWidget(self.B2, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.ImageFrame)
        self.verticalLayout.addWidget(self.widgetFrameOuter)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.B1, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Form.toggle1)
        QtCore.QObject.connect(self.B2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Form.toggle2)
        QtCore.QObject.connect(self.B3, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Form.toggle3)
        QtCore.QObject.connect(self.B4, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), Form.toggle4)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.widgetFrameOuter.setToolTip(_translate("Form", "Disable square waves and set them to High/Low", None))
        self.widgetFrameOuter.setProperty("class", _translate("Form", "ControlWidget", None))
        self.title.setText(_translate("Form", "Digital Outputs", None))
        self.B1.setText(_translate("Form", "SQR1", None))
        self.B3.setText(_translate("Form", "SQR3", None))
        self.B4.setText(_translate("Form", "SQR4", None))
        self.B2.setText(_translate("Form", "SQR2", None))

