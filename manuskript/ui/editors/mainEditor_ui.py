# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manuskript/ui/editors/mainEditor_ui.ui'
#
# Created: Mon Feb  8 08:54:11 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainEditor(object):
    def setupUi(self, mainEditor):
        mainEditor.setObjectName("mainEditor")
        mainEditor.resize(791, 319)
        self.verticalLayout = QtWidgets.QVBoxLayout(mainEditor)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab = QtWidgets.QTabWidget(mainEditor)
        self.tab.setDocumentMode(True)
        self.tab.setTabsClosable(True)
        self.tab.setMovable(True)
        self.tab.setProperty("tabBarAutoHide", False)
        self.tab.setObjectName("tab")
        self.verticalLayout.addWidget(self.tab)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.btnRedacFolderText = QtWidgets.QPushButton(mainEditor)
        self.btnRedacFolderText.setCheckable(True)
        self.btnRedacFolderText.setObjectName("btnRedacFolderText")
        self.buttonGroup = QtWidgets.QButtonGroup(mainEditor)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btnRedacFolderText)
        self.horizontalLayout_19.addWidget(self.btnRedacFolderText)
        self.btnRedacFolderCork = QtWidgets.QPushButton(mainEditor)
        self.btnRedacFolderCork.setCheckable(True)
        self.btnRedacFolderCork.setChecked(True)
        self.btnRedacFolderCork.setObjectName("btnRedacFolderCork")
        self.buttonGroup.addButton(self.btnRedacFolderCork)
        self.horizontalLayout_19.addWidget(self.btnRedacFolderCork)
        self.btnRedacFolderOutline = QtWidgets.QPushButton(mainEditor)
        self.btnRedacFolderOutline.setCheckable(True)
        self.btnRedacFolderOutline.setObjectName("btnRedacFolderOutline")
        self.buttonGroup.addButton(self.btnRedacFolderOutline)
        self.horizontalLayout_19.addWidget(self.btnRedacFolderOutline)
        self.sldCorkSizeFactor = QtWidgets.QSlider(mainEditor)
        self.sldCorkSizeFactor.setMinimumSize(QtCore.QSize(100, 0))
        self.sldCorkSizeFactor.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sldCorkSizeFactor.setMinimum(50)
        self.sldCorkSizeFactor.setMaximum(200)
        self.sldCorkSizeFactor.setProperty("value", 100)
        self.sldCorkSizeFactor.setOrientation(QtCore.Qt.Horizontal)
        self.sldCorkSizeFactor.setObjectName("sldCorkSizeFactor")
        self.horizontalLayout_19.addWidget(self.sldCorkSizeFactor)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem)
        self.textFormat = textFormat(mainEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textFormat.sizePolicy().hasHeightForWidth())
        self.textFormat.setSizePolicy(sizePolicy)
        self.textFormat.setMinimumSize(QtCore.QSize(20, 20))
        self.textFormat.setObjectName("textFormat")
        self.horizontalLayout_19.addWidget(self.textFormat)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem1)
        self.lblRedacWC = QtWidgets.QLabel(mainEditor)
        self.lblRedacWC.setMinimumSize(QtCore.QSize(10, 0))
        self.lblRedacWC.setText("")
        self.lblRedacWC.setObjectName("lblRedacWC")
        self.horizontalLayout_19.addWidget(self.lblRedacWC)
        self.lblRedacProgress = QtWidgets.QLabel(mainEditor)
        self.lblRedacProgress.setMinimumSize(QtCore.QSize(100, 6))
        self.lblRedacProgress.setMaximumSize(QtCore.QSize(200, 14))
        self.lblRedacProgress.setText("")
        self.lblRedacProgress.setObjectName("lblRedacProgress")
        self.horizontalLayout_19.addWidget(self.lblRedacProgress)
        self.btnRedacFullscreen = QtWidgets.QPushButton(mainEditor)
        self.btnRedacFullscreen.setText("")
        icon = QtGui.QIcon.fromTheme("view-fullscreen")
        self.btnRedacFullscreen.setIcon(icon)
        self.btnRedacFullscreen.setObjectName("btnRedacFullscreen")
        self.horizontalLayout_19.addWidget(self.btnRedacFullscreen)
        self.verticalLayout.addLayout(self.horizontalLayout_19)

        self.retranslateUi(mainEditor)
        self.tab.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(mainEditor)

    def retranslateUi(self, mainEditor):
        _translate = QtCore.QCoreApplication.translate
        mainEditor.setWindowTitle(_translate("mainEditor", "Form"))
        self.btnRedacFolderText.setText(_translate("mainEditor", "Text"))
        self.btnRedacFolderCork.setText(_translate("mainEditor", "Index cards"))
        self.btnRedacFolderOutline.setText(_translate("mainEditor", "Outline"))
        self.btnRedacFullscreen.setShortcut(_translate("mainEditor", "F11"))

from manuskript.ui.editors.textFormat import textFormat
