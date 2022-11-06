# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1270, 492)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionEXIT = QAction(MainWindow)
        self.actionEXIT.setObjectName(u"actionEXIT")
        self.actionnew_config = QAction(MainWindow)
        self.actionnew_config.setObjectName(u"actionnew_config")
        self.actionsave_config = QAction(MainWindow)
        self.actionsave_config.setObjectName(u"actionsave_config")
        self.actionlabel_config = QAction(MainWindow)
        self.actionlabel_config.setObjectName(u"actionlabel_config")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_ir5 = QLineEdit(self.centralwidget)
        self.lineEdit_ir5.setObjectName(u"lineEdit_ir5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_ir5.sizePolicy().hasHeightForWidth())
        self.lineEdit_ir5.setSizePolicy(sizePolicy1)
        self.lineEdit_ir5.setMaximumSize(QSize(60, 1000))
        self.lineEdit_ir5.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(20)
        self.lineEdit_ir5.setFont(font)
        self.lineEdit_ir5.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_ir5.setMaxLength(1)
        self.lineEdit_ir5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_ir5)

        self.lineEdit_ir3 = QLineEdit(self.centralwidget)
        self.lineEdit_ir3.setObjectName(u"lineEdit_ir3")
        sizePolicy1.setHeightForWidth(self.lineEdit_ir3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ir3.setSizePolicy(sizePolicy1)
        self.lineEdit_ir3.setMaximumSize(QSize(60, 1000))
        self.lineEdit_ir3.setBaseSize(QSize(0, 0))
        self.lineEdit_ir3.setFont(font)
        self.lineEdit_ir3.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_ir3.setMaxLength(1)
        self.lineEdit_ir3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_ir3)

        self.lineEdit_ir1 = QLineEdit(self.centralwidget)
        self.lineEdit_ir1.setObjectName(u"lineEdit_ir1")
        sizePolicy1.setHeightForWidth(self.lineEdit_ir1.sizePolicy().hasHeightForWidth())
        self.lineEdit_ir1.setSizePolicy(sizePolicy1)
        self.lineEdit_ir1.setMaximumSize(QSize(60, 1000))
        self.lineEdit_ir1.setBaseSize(QSize(0, 0))
        self.lineEdit_ir1.setFont(font)
        self.lineEdit_ir1.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_ir1.setMaxLength(1)
        self.lineEdit_ir1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_ir1)

        self.lineEdit_K31 = QLineEdit(self.centralwidget)
        self.lineEdit_K31.setObjectName(u"lineEdit_K31")
        sizePolicy1.setHeightForWidth(self.lineEdit_K31.sizePolicy().hasHeightForWidth())
        self.lineEdit_K31.setSizePolicy(sizePolicy1)
        self.lineEdit_K31.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K31.setBaseSize(QSize(0, 0))
        self.lineEdit_K31.setFont(font)
        self.lineEdit_K31.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K31.setMaxLength(1)
        self.lineEdit_K31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K31)

        self.lineEdit_K29 = QLineEdit(self.centralwidget)
        self.lineEdit_K29.setObjectName(u"lineEdit_K29")
        sizePolicy1.setHeightForWidth(self.lineEdit_K29.sizePolicy().hasHeightForWidth())
        self.lineEdit_K29.setSizePolicy(sizePolicy1)
        self.lineEdit_K29.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K29.setBaseSize(QSize(0, 0))
        self.lineEdit_K29.setFont(font)
        self.lineEdit_K29.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K29.setMaxLength(1)
        self.lineEdit_K29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K29)

        self.lineEdit_K27 = QLineEdit(self.centralwidget)
        self.lineEdit_K27.setObjectName(u"lineEdit_K27")
        sizePolicy1.setHeightForWidth(self.lineEdit_K27.sizePolicy().hasHeightForWidth())
        self.lineEdit_K27.setSizePolicy(sizePolicy1)
        self.lineEdit_K27.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K27.setBaseSize(QSize(0, 0))
        self.lineEdit_K27.setFont(font)
        self.lineEdit_K27.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K27.setMaxLength(1)
        self.lineEdit_K27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K27)

        self.lineEdit_K25 = QLineEdit(self.centralwidget)
        self.lineEdit_K25.setObjectName(u"lineEdit_K25")
        sizePolicy1.setHeightForWidth(self.lineEdit_K25.sizePolicy().hasHeightForWidth())
        self.lineEdit_K25.setSizePolicy(sizePolicy1)
        self.lineEdit_K25.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K25.setBaseSize(QSize(0, 0))
        self.lineEdit_K25.setFont(font)
        self.lineEdit_K25.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K25.setMaxLength(1)
        self.lineEdit_K25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K25)

        self.lineEdit_K23 = QLineEdit(self.centralwidget)
        self.lineEdit_K23.setObjectName(u"lineEdit_K23")
        sizePolicy1.setHeightForWidth(self.lineEdit_K23.sizePolicy().hasHeightForWidth())
        self.lineEdit_K23.setSizePolicy(sizePolicy1)
        self.lineEdit_K23.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K23.setBaseSize(QSize(0, 0))
        self.lineEdit_K23.setFont(font)
        self.lineEdit_K23.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K23.setMaxLength(1)
        self.lineEdit_K23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K23)

        self.lineEdit_K21 = QLineEdit(self.centralwidget)
        self.lineEdit_K21.setObjectName(u"lineEdit_K21")
        sizePolicy1.setHeightForWidth(self.lineEdit_K21.sizePolicy().hasHeightForWidth())
        self.lineEdit_K21.setSizePolicy(sizePolicy1)
        self.lineEdit_K21.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K21.setBaseSize(QSize(0, 0))
        self.lineEdit_K21.setFont(font)
        self.lineEdit_K21.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K21.setMaxLength(1)
        self.lineEdit_K21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K21)

        self.lineEdit_K19 = QLineEdit(self.centralwidget)
        self.lineEdit_K19.setObjectName(u"lineEdit_K19")
        sizePolicy1.setHeightForWidth(self.lineEdit_K19.sizePolicy().hasHeightForWidth())
        self.lineEdit_K19.setSizePolicy(sizePolicy1)
        self.lineEdit_K19.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K19.setBaseSize(QSize(0, 0))
        self.lineEdit_K19.setFont(font)
        self.lineEdit_K19.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K19.setMaxLength(1)
        self.lineEdit_K19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K19)

        self.lineEdit_K17 = QLineEdit(self.centralwidget)
        self.lineEdit_K17.setObjectName(u"lineEdit_K17")
        sizePolicy1.setHeightForWidth(self.lineEdit_K17.sizePolicy().hasHeightForWidth())
        self.lineEdit_K17.setSizePolicy(sizePolicy1)
        self.lineEdit_K17.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K17.setBaseSize(QSize(0, 0))
        self.lineEdit_K17.setFont(font)
        self.lineEdit_K17.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K17.setMaxLength(1)
        self.lineEdit_K17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K17)

        self.lineEdit_K15 = QLineEdit(self.centralwidget)
        self.lineEdit_K15.setObjectName(u"lineEdit_K15")
        sizePolicy1.setHeightForWidth(self.lineEdit_K15.sizePolicy().hasHeightForWidth())
        self.lineEdit_K15.setSizePolicy(sizePolicy1)
        self.lineEdit_K15.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K15.setBaseSize(QSize(0, 0))
        self.lineEdit_K15.setFont(font)
        self.lineEdit_K15.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K15.setMaxLength(1)
        self.lineEdit_K15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K15)

        self.lineEdit_K13 = QLineEdit(self.centralwidget)
        self.lineEdit_K13.setObjectName(u"lineEdit_K13")
        sizePolicy1.setHeightForWidth(self.lineEdit_K13.sizePolicy().hasHeightForWidth())
        self.lineEdit_K13.setSizePolicy(sizePolicy1)
        self.lineEdit_K13.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K13.setBaseSize(QSize(0, 0))
        self.lineEdit_K13.setFont(font)
        self.lineEdit_K13.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K13.setMaxLength(1)
        self.lineEdit_K13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K13)

        self.lineEdit_K11 = QLineEdit(self.centralwidget)
        self.lineEdit_K11.setObjectName(u"lineEdit_K11")
        sizePolicy1.setHeightForWidth(self.lineEdit_K11.sizePolicy().hasHeightForWidth())
        self.lineEdit_K11.setSizePolicy(sizePolicy1)
        self.lineEdit_K11.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K11.setBaseSize(QSize(0, 0))
        self.lineEdit_K11.setFont(font)
        self.lineEdit_K11.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K11.setMaxLength(1)
        self.lineEdit_K11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K11)

        self.lineEdit_K9 = QLineEdit(self.centralwidget)
        self.lineEdit_K9.setObjectName(u"lineEdit_K9")
        sizePolicy1.setHeightForWidth(self.lineEdit_K9.sizePolicy().hasHeightForWidth())
        self.lineEdit_K9.setSizePolicy(sizePolicy1)
        self.lineEdit_K9.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K9.setBaseSize(QSize(0, 0))
        self.lineEdit_K9.setFont(font)
        self.lineEdit_K9.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K9.setMaxLength(1)
        self.lineEdit_K9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K9)

        self.lineEdit_K7 = QLineEdit(self.centralwidget)
        self.lineEdit_K7.setObjectName(u"lineEdit_K7")
        sizePolicy1.setHeightForWidth(self.lineEdit_K7.sizePolicy().hasHeightForWidth())
        self.lineEdit_K7.setSizePolicy(sizePolicy1)
        self.lineEdit_K7.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K7.setBaseSize(QSize(0, 0))
        self.lineEdit_K7.setFont(font)
        self.lineEdit_K7.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K7.setMaxLength(1)
        self.lineEdit_K7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K7)

        self.lineEdit_K5 = QLineEdit(self.centralwidget)
        self.lineEdit_K5.setObjectName(u"lineEdit_K5")
        sizePolicy1.setHeightForWidth(self.lineEdit_K5.sizePolicy().hasHeightForWidth())
        self.lineEdit_K5.setSizePolicy(sizePolicy1)
        self.lineEdit_K5.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K5.setBaseSize(QSize(0, 0))
        self.lineEdit_K5.setFont(font)
        self.lineEdit_K5.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K5.setMaxLength(1)
        self.lineEdit_K5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K5)

        self.lineEdit_K3 = QLineEdit(self.centralwidget)
        self.lineEdit_K3.setObjectName(u"lineEdit_K3")
        sizePolicy1.setHeightForWidth(self.lineEdit_K3.sizePolicy().hasHeightForWidth())
        self.lineEdit_K3.setSizePolicy(sizePolicy1)
        self.lineEdit_K3.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K3.setBaseSize(QSize(0, 0))
        self.lineEdit_K3.setFont(font)
        self.lineEdit_K3.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K3.setMaxLength(1)
        self.lineEdit_K3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K3)

        self.lineEdit_K1 = QLineEdit(self.centralwidget)
        self.lineEdit_K1.setObjectName(u"lineEdit_K1")
        sizePolicy1.setHeightForWidth(self.lineEdit_K1.sizePolicy().hasHeightForWidth())
        self.lineEdit_K1.setSizePolicy(sizePolicy1)
        self.lineEdit_K1.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K1.setBaseSize(QSize(0, 0))
        self.lineEdit_K1.setFont(font)
        self.lineEdit_K1.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K1.setMaxLength(1)
        self.lineEdit_K1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_K1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_ir5 = QLabel(self.centralwidget)
        self.label_ir5.setObjectName(u"label_ir5")
        self.label_ir5.setMaximumSize(QSize(60, 16777215))
        self.label_ir5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_ir5)

        self.label_ir3 = QLabel(self.centralwidget)
        self.label_ir3.setObjectName(u"label_ir3")
        self.label_ir3.setMaximumSize(QSize(60, 16777215))
        self.label_ir3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_ir3)

        self.label_ir1 = QLabel(self.centralwidget)
        self.label_ir1.setObjectName(u"label_ir1")
        self.label_ir1.setMaximumSize(QSize(60, 16777215))
        self.label_ir1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_ir1)

        self.label_k31 = QLabel(self.centralwidget)
        self.label_k31.setObjectName(u"label_k31")
        self.label_k31.setMaximumSize(QSize(60, 16777215))
        self.label_k31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k31)

        self.label_k29 = QLabel(self.centralwidget)
        self.label_k29.setObjectName(u"label_k29")
        self.label_k29.setMaximumSize(QSize(60, 16777215))
        self.label_k29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k29)

        self.label_k27 = QLabel(self.centralwidget)
        self.label_k27.setObjectName(u"label_k27")
        self.label_k27.setMaximumSize(QSize(60, 16777215))
        self.label_k27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k27)

        self.label_k25 = QLabel(self.centralwidget)
        self.label_k25.setObjectName(u"label_k25")
        self.label_k25.setMaximumSize(QSize(60, 16777215))
        self.label_k25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k25)

        self.label_k23 = QLabel(self.centralwidget)
        self.label_k23.setObjectName(u"label_k23")
        self.label_k23.setMaximumSize(QSize(60, 16777215))
        self.label_k23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k23)

        self.label_k21 = QLabel(self.centralwidget)
        self.label_k21.setObjectName(u"label_k21")
        self.label_k21.setMaximumSize(QSize(60, 16777215))
        self.label_k21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k21)

        self.label_k19 = QLabel(self.centralwidget)
        self.label_k19.setObjectName(u"label_k19")
        self.label_k19.setMaximumSize(QSize(60, 16777215))
        self.label_k19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k19)

        self.label_k17 = QLabel(self.centralwidget)
        self.label_k17.setObjectName(u"label_k17")
        self.label_k17.setMaximumSize(QSize(60, 16777215))
        self.label_k17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k17)

        self.label_k15 = QLabel(self.centralwidget)
        self.label_k15.setObjectName(u"label_k15")
        self.label_k15.setMaximumSize(QSize(60, 16777215))
        self.label_k15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k15)

        self.label_k13 = QLabel(self.centralwidget)
        self.label_k13.setObjectName(u"label_k13")
        self.label_k13.setMaximumSize(QSize(60, 16777215))
        self.label_k13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k13)

        self.label_k11 = QLabel(self.centralwidget)
        self.label_k11.setObjectName(u"label_k11")
        self.label_k11.setMaximumSize(QSize(60, 16777215))
        self.label_k11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k11)

        self.label_k9 = QLabel(self.centralwidget)
        self.label_k9.setObjectName(u"label_k9")
        self.label_k9.setMaximumSize(QSize(60, 16777215))
        self.label_k9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k9)

        self.label_k7 = QLabel(self.centralwidget)
        self.label_k7.setObjectName(u"label_k7")
        self.label_k7.setMaximumSize(QSize(60, 16777215))
        self.label_k7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k7)

        self.label_k5 = QLabel(self.centralwidget)
        self.label_k5.setObjectName(u"label_k5")
        self.label_k5.setMaximumSize(QSize(60, 16777215))
        self.label_k5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k5)

        self.label_k3 = QLabel(self.centralwidget)
        self.label_k3.setObjectName(u"label_k3")
        self.label_k3.setMaximumSize(QSize(60, 16777215))
        self.label_k3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k3)

        self.label_k1 = QLabel(self.centralwidget)
        self.label_k1.setObjectName(u"label_k1")
        self.label_k1.setMaximumSize(QSize(60, 16777215))
        self.label_k1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_k1)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_ir6 = QLineEdit(self.centralwidget)
        self.lineEdit_ir6.setObjectName(u"lineEdit_ir6")
        sizePolicy1.setHeightForWidth(self.lineEdit_ir6.sizePolicy().hasHeightForWidth())
        self.lineEdit_ir6.setSizePolicy(sizePolicy1)
        self.lineEdit_ir6.setMaximumSize(QSize(60, 1000))
        self.lineEdit_ir6.setBaseSize(QSize(0, 0))
        self.lineEdit_ir6.setFont(font)
        self.lineEdit_ir6.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_ir6.setMaxLength(1)
        self.lineEdit_ir6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_ir6)

        self.lineEdit_ir4 = QLineEdit(self.centralwidget)
        self.lineEdit_ir4.setObjectName(u"lineEdit_ir4")
        sizePolicy1.setHeightForWidth(self.lineEdit_ir4.sizePolicy().hasHeightForWidth())
        self.lineEdit_ir4.setSizePolicy(sizePolicy1)
        self.lineEdit_ir4.setMaximumSize(QSize(60, 1000))
        self.lineEdit_ir4.setBaseSize(QSize(0, 0))
        self.lineEdit_ir4.setFont(font)
        self.lineEdit_ir4.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_ir4.setMaxLength(1)
        self.lineEdit_ir4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_ir4)

        self.lineEdit_ir2 = QLineEdit(self.centralwidget)
        self.lineEdit_ir2.setObjectName(u"lineEdit_ir2")
        sizePolicy1.setHeightForWidth(self.lineEdit_ir2.sizePolicy().hasHeightForWidth())
        self.lineEdit_ir2.setSizePolicy(sizePolicy1)
        self.lineEdit_ir2.setMaximumSize(QSize(60, 1000))
        self.lineEdit_ir2.setBaseSize(QSize(0, 0))
        self.lineEdit_ir2.setFont(font)
        self.lineEdit_ir2.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_ir2.setMaxLength(1)
        self.lineEdit_ir2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_ir2)

        self.lineEdit_K32 = QLineEdit(self.centralwidget)
        self.lineEdit_K32.setObjectName(u"lineEdit_K32")
        sizePolicy1.setHeightForWidth(self.lineEdit_K32.sizePolicy().hasHeightForWidth())
        self.lineEdit_K32.setSizePolicy(sizePolicy1)
        self.lineEdit_K32.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K32.setBaseSize(QSize(0, 0))
        self.lineEdit_K32.setFont(font)
        self.lineEdit_K32.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K32.setMaxLength(1)
        self.lineEdit_K32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K32)

        self.lineEdit_K30 = QLineEdit(self.centralwidget)
        self.lineEdit_K30.setObjectName(u"lineEdit_K30")
        sizePolicy1.setHeightForWidth(self.lineEdit_K30.sizePolicy().hasHeightForWidth())
        self.lineEdit_K30.setSizePolicy(sizePolicy1)
        self.lineEdit_K30.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K30.setBaseSize(QSize(0, 0))
        self.lineEdit_K30.setFont(font)
        self.lineEdit_K30.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K30.setMaxLength(1)
        self.lineEdit_K30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K30)

        self.lineEdit_K28 = QLineEdit(self.centralwidget)
        self.lineEdit_K28.setObjectName(u"lineEdit_K28")
        sizePolicy1.setHeightForWidth(self.lineEdit_K28.sizePolicy().hasHeightForWidth())
        self.lineEdit_K28.setSizePolicy(sizePolicy1)
        self.lineEdit_K28.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K28.setBaseSize(QSize(0, 0))
        self.lineEdit_K28.setFont(font)
        self.lineEdit_K28.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K28.setMaxLength(1)
        self.lineEdit_K28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K28)

        self.lineEdit_K26 = QLineEdit(self.centralwidget)
        self.lineEdit_K26.setObjectName(u"lineEdit_K26")
        sizePolicy1.setHeightForWidth(self.lineEdit_K26.sizePolicy().hasHeightForWidth())
        self.lineEdit_K26.setSizePolicy(sizePolicy1)
        self.lineEdit_K26.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K26.setBaseSize(QSize(0, 0))
        self.lineEdit_K26.setFont(font)
        self.lineEdit_K26.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K26.setMaxLength(1)
        self.lineEdit_K26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K26)

        self.lineEdit_K24 = QLineEdit(self.centralwidget)
        self.lineEdit_K24.setObjectName(u"lineEdit_K24")
        sizePolicy1.setHeightForWidth(self.lineEdit_K24.sizePolicy().hasHeightForWidth())
        self.lineEdit_K24.setSizePolicy(sizePolicy1)
        self.lineEdit_K24.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K24.setBaseSize(QSize(0, 0))
        self.lineEdit_K24.setFont(font)
        self.lineEdit_K24.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K24.setMaxLength(1)
        self.lineEdit_K24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K24)

        self.lineEdit_K22 = QLineEdit(self.centralwidget)
        self.lineEdit_K22.setObjectName(u"lineEdit_K22")
        sizePolicy1.setHeightForWidth(self.lineEdit_K22.sizePolicy().hasHeightForWidth())
        self.lineEdit_K22.setSizePolicy(sizePolicy1)
        self.lineEdit_K22.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K22.setBaseSize(QSize(0, 0))
        self.lineEdit_K22.setFont(font)
        self.lineEdit_K22.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K22.setMaxLength(1)
        self.lineEdit_K22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K22)

        self.lineEdit_K20 = QLineEdit(self.centralwidget)
        self.lineEdit_K20.setObjectName(u"lineEdit_K20")
        sizePolicy1.setHeightForWidth(self.lineEdit_K20.sizePolicy().hasHeightForWidth())
        self.lineEdit_K20.setSizePolicy(sizePolicy1)
        self.lineEdit_K20.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K20.setBaseSize(QSize(0, 0))
        self.lineEdit_K20.setFont(font)
        self.lineEdit_K20.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K20.setMaxLength(1)
        self.lineEdit_K20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K20)

        self.lineEdit_K18 = QLineEdit(self.centralwidget)
        self.lineEdit_K18.setObjectName(u"lineEdit_K18")
        sizePolicy1.setHeightForWidth(self.lineEdit_K18.sizePolicy().hasHeightForWidth())
        self.lineEdit_K18.setSizePolicy(sizePolicy1)
        self.lineEdit_K18.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K18.setBaseSize(QSize(0, 0))
        self.lineEdit_K18.setFont(font)
        self.lineEdit_K18.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K18.setMaxLength(1)
        self.lineEdit_K18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K18)

        self.lineEdit_K16 = QLineEdit(self.centralwidget)
        self.lineEdit_K16.setObjectName(u"lineEdit_K16")
        sizePolicy1.setHeightForWidth(self.lineEdit_K16.sizePolicy().hasHeightForWidth())
        self.lineEdit_K16.setSizePolicy(sizePolicy1)
        self.lineEdit_K16.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K16.setBaseSize(QSize(0, 0))
        self.lineEdit_K16.setFont(font)
        self.lineEdit_K16.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K16.setMaxLength(1)
        self.lineEdit_K16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K16)

        self.lineEdit_K14 = QLineEdit(self.centralwidget)
        self.lineEdit_K14.setObjectName(u"lineEdit_K14")
        sizePolicy1.setHeightForWidth(self.lineEdit_K14.sizePolicy().hasHeightForWidth())
        self.lineEdit_K14.setSizePolicy(sizePolicy1)
        self.lineEdit_K14.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K14.setBaseSize(QSize(0, 0))
        self.lineEdit_K14.setFont(font)
        self.lineEdit_K14.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K14.setMaxLength(1)
        self.lineEdit_K14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K14)

        self.lineEdit_K12 = QLineEdit(self.centralwidget)
        self.lineEdit_K12.setObjectName(u"lineEdit_K12")
        sizePolicy1.setHeightForWidth(self.lineEdit_K12.sizePolicy().hasHeightForWidth())
        self.lineEdit_K12.setSizePolicy(sizePolicy1)
        self.lineEdit_K12.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K12.setBaseSize(QSize(0, 0))
        self.lineEdit_K12.setFont(font)
        self.lineEdit_K12.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K12.setMaxLength(1)
        self.lineEdit_K12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K12)

        self.lineEdit_K10 = QLineEdit(self.centralwidget)
        self.lineEdit_K10.setObjectName(u"lineEdit_K10")
        sizePolicy1.setHeightForWidth(self.lineEdit_K10.sizePolicy().hasHeightForWidth())
        self.lineEdit_K10.setSizePolicy(sizePolicy1)
        self.lineEdit_K10.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K10.setBaseSize(QSize(0, 0))
        self.lineEdit_K10.setFont(font)
        self.lineEdit_K10.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K10.setMaxLength(1)
        self.lineEdit_K10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K10)

        self.lineEdit_K8 = QLineEdit(self.centralwidget)
        self.lineEdit_K8.setObjectName(u"lineEdit_K8")
        sizePolicy1.setHeightForWidth(self.lineEdit_K8.sizePolicy().hasHeightForWidth())
        self.lineEdit_K8.setSizePolicy(sizePolicy1)
        self.lineEdit_K8.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K8.setBaseSize(QSize(0, 0))
        self.lineEdit_K8.setFont(font)
        self.lineEdit_K8.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K8.setMaxLength(1)
        self.lineEdit_K8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K8)

        self.lineEdit_K6 = QLineEdit(self.centralwidget)
        self.lineEdit_K6.setObjectName(u"lineEdit_K6")
        sizePolicy1.setHeightForWidth(self.lineEdit_K6.sizePolicy().hasHeightForWidth())
        self.lineEdit_K6.setSizePolicy(sizePolicy1)
        self.lineEdit_K6.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K6.setBaseSize(QSize(0, 0))
        self.lineEdit_K6.setFont(font)
        self.lineEdit_K6.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K6.setMaxLength(1)
        self.lineEdit_K6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K6)

        self.lineEdit_K4 = QLineEdit(self.centralwidget)
        self.lineEdit_K4.setObjectName(u"lineEdit_K4")
        sizePolicy1.setHeightForWidth(self.lineEdit_K4.sizePolicy().hasHeightForWidth())
        self.lineEdit_K4.setSizePolicy(sizePolicy1)
        self.lineEdit_K4.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K4.setBaseSize(QSize(0, 0))
        self.lineEdit_K4.setFont(font)
        self.lineEdit_K4.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K4.setMaxLength(1)
        self.lineEdit_K4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K4)

        self.lineEdit_K2 = QLineEdit(self.centralwidget)
        self.lineEdit_K2.setObjectName(u"lineEdit_K2")
        sizePolicy1.setHeightForWidth(self.lineEdit_K2.sizePolicy().hasHeightForWidth())
        self.lineEdit_K2.setSizePolicy(sizePolicy1)
        self.lineEdit_K2.setMaximumSize(QSize(60, 1000))
        self.lineEdit_K2.setBaseSize(QSize(0, 0))
        self.lineEdit_K2.setFont(font)
        self.lineEdit_K2.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit_K2.setMaxLength(1)
        self.lineEdit_K2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_K2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_ir6 = QLabel(self.centralwidget)
        self.label_ir6.setObjectName(u"label_ir6")
        self.label_ir6.setMaximumSize(QSize(60, 16777215))
        self.label_ir6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_ir6)

        self.label_ir4 = QLabel(self.centralwidget)
        self.label_ir4.setObjectName(u"label_ir4")
        self.label_ir4.setMaximumSize(QSize(60, 16777215))
        self.label_ir4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_ir4)

        self.label_ir2 = QLabel(self.centralwidget)
        self.label_ir2.setObjectName(u"label_ir2")
        self.label_ir2.setMaximumSize(QSize(60, 16777215))
        self.label_ir2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_ir2)

        self.label_k32 = QLabel(self.centralwidget)
        self.label_k32.setObjectName(u"label_k32")
        self.label_k32.setMaximumSize(QSize(60, 16777215))
        self.label_k32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k32)

        self.label_k30 = QLabel(self.centralwidget)
        self.label_k30.setObjectName(u"label_k30")
        self.label_k30.setMaximumSize(QSize(60, 16777215))
        self.label_k30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k30)

        self.label_k28 = QLabel(self.centralwidget)
        self.label_k28.setObjectName(u"label_k28")
        self.label_k28.setMaximumSize(QSize(60, 16777215))
        self.label_k28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k28)

        self.label_k26 = QLabel(self.centralwidget)
        self.label_k26.setObjectName(u"label_k26")
        self.label_k26.setMaximumSize(QSize(60, 16777215))
        self.label_k26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k26)

        self.label_k24 = QLabel(self.centralwidget)
        self.label_k24.setObjectName(u"label_k24")
        self.label_k24.setMaximumSize(QSize(60, 16777215))
        self.label_k24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k24)

        self.label_k22 = QLabel(self.centralwidget)
        self.label_k22.setObjectName(u"label_k22")
        self.label_k22.setMaximumSize(QSize(60, 16777215))
        self.label_k22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k22)

        self.label_k20 = QLabel(self.centralwidget)
        self.label_k20.setObjectName(u"label_k20")
        self.label_k20.setMaximumSize(QSize(60, 16777215))
        self.label_k20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k20)

        self.label_k18 = QLabel(self.centralwidget)
        self.label_k18.setObjectName(u"label_k18")
        self.label_k18.setMaximumSize(QSize(60, 16777215))
        self.label_k18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k18)

        self.label_k16 = QLabel(self.centralwidget)
        self.label_k16.setObjectName(u"label_k16")
        self.label_k16.setMaximumSize(QSize(60, 16777215))
        self.label_k16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k16)

        self.label_k14 = QLabel(self.centralwidget)
        self.label_k14.setObjectName(u"label_k14")
        self.label_k14.setMaximumSize(QSize(60, 16777215))
        self.label_k14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k14)

        self.label_k12 = QLabel(self.centralwidget)
        self.label_k12.setObjectName(u"label_k12")
        self.label_k12.setMaximumSize(QSize(60, 16777215))
        self.label_k12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k12)

        self.label_k10 = QLabel(self.centralwidget)
        self.label_k10.setObjectName(u"label_k10")
        self.label_k10.setMaximumSize(QSize(60, 16777215))
        self.label_k10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k10)

        self.label_k8 = QLabel(self.centralwidget)
        self.label_k8.setObjectName(u"label_k8")
        self.label_k8.setMaximumSize(QSize(60, 16777215))
        self.label_k8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k8)

        self.label_k6 = QLabel(self.centralwidget)
        self.label_k6.setObjectName(u"label_k6")
        self.label_k6.setMaximumSize(QSize(60, 16777215))
        self.label_k6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k6)

        self.label_k4 = QLabel(self.centralwidget)
        self.label_k4.setObjectName(u"label_k4")
        self.label_k4.setMaximumSize(QSize(60, 16777215))
        self.label_k4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k4)

        self.label_k2 = QLabel(self.centralwidget)
        self.label_k2.setObjectName(u"label_k2")
        self.label_k2.setMaximumSize(QSize(60, 16777215))
        self.label_k2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_k2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_log = QLabel(self.centralwidget)
        self.label_log.setObjectName(u"label_log")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_log.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_log)

        self.label_ctrl = QLabel(self.centralwidget)
        self.label_ctrl.setObjectName(u"label_ctrl")
        self.label_ctrl.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_ctrl)

        self.checkBox_IR = QCheckBox(self.centralwidget)
        self.checkBox_IR.setObjectName(u"checkBox_IR")
        font2 = QFont()
        font2.setPointSize(11)
        self.checkBox_IR.setFont(font2)

        self.horizontalLayout_8.addWidget(self.checkBox_IR)

        self.checkBox_Slider = QCheckBox(self.centralwidget)
        self.checkBox_Slider.setObjectName(u"checkBox_Slider")
        self.checkBox_Slider.setFont(font2)

        self.horizontalLayout_8.addWidget(self.checkBox_Slider)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.plainTextEdit_log = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_log.setObjectName(u"plainTextEdit_log")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plainTextEdit_log.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_log.setSizePolicy(sizePolicy2)
        self.plainTextEdit_log.setFont(font1)
        self.plainTextEdit_log.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.plainTextEdit_log)


        self.gridLayout.addLayout(self.verticalLayout_3, 5, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.lineEdit_threshold = QLineEdit(self.centralwidget)
        self.lineEdit_threshold.setObjectName(u"lineEdit_threshold")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_threshold.sizePolicy().hasHeightForWidth())
        self.lineEdit_threshold.setSizePolicy(sizePolicy4)
        self.lineEdit_threshold.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lineEdit_threshold)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.pushButton_FindDevice = QPushButton(self.centralwidget)
        self.pushButton_FindDevice.setObjectName(u"pushButton_FindDevice")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_FindDevice.sizePolicy().hasHeightForWidth())
        self.pushButton_FindDevice.setSizePolicy(sizePolicy5)
        self.pushButton_FindDevice.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton_FindDevice)

        self.pushButton_Read = QPushButton(self.centralwidget)
        self.pushButton_Read.setObjectName(u"pushButton_Read")
        sizePolicy5.setHeightForWidth(self.pushButton_Read.sizePolicy().hasHeightForWidth())
        self.pushButton_Read.setSizePolicy(sizePolicy5)
        self.pushButton_Read.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton_Read)

        self.pushButton_Write = QPushButton(self.centralwidget)
        self.pushButton_Write.setObjectName(u"pushButton_Write")
        sizePolicy5.setHeightForWidth(self.pushButton_Write.sizePolicy().hasHeightForWidth())
        self.pushButton_Write.setSizePolicy(sizePolicy5)
        self.pushButton_Write.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton_Write)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.pushButton_Gloves = QPushButton(self.centralwidget)
        self.pushButton_Gloves.setObjectName(u"pushButton_Gloves")
        sizePolicy5.setHeightForWidth(self.pushButton_Gloves.sizePolicy().hasHeightForWidth())
        self.pushButton_Gloves.setSizePolicy(sizePolicy5)
        self.pushButton_Gloves.setFont(font1)

        self.verticalLayout_4.addWidget(self.pushButton_Gloves)

        self.pushButton_Hands = QPushButton(self.centralwidget)
        self.pushButton_Hands.setObjectName(u"pushButton_Hands")
        sizePolicy5.setHeightForWidth(self.pushButton_Hands.sizePolicy().hasHeightForWidth())
        self.pushButton_Hands.setSizePolicy(sizePolicy5)
        self.pushButton_Hands.setFont(font1)

        self.verticalLayout_4.addWidget(self.pushButton_Hands)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.verticalLayout_5.setStretch(1, 90)

        self.gridLayout.addLayout(self.verticalLayout_5, 5, 1, 1, 1)

        self.Ttile = QLabel(self.centralwidget)
        self.Ttile.setObjectName(u"Ttile")
        font3 = QFont()
        font3.setPointSize(18)
        self.Ttile.setFont(font3)
        self.Ttile.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Ttile, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1270, 23))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_conf = QMenu(self.menubar)
        self.menu_conf.setObjectName(u"menu_conf")
        self.list_conf = QMenu(self.menu_conf)
        self.list_conf.setObjectName(u"list_conf")
        self.del_conf = QMenu(self.menu_conf)
        self.del_conf.setObjectName(u"del_conf")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_conf.menuAction())
        self.menu_file.addAction(self.actionEXIT)
        self.menu_conf.addAction(self.actionnew_config)
        self.menu_conf.addAction(self.list_conf.menuAction())
        self.menu_conf.addAction(self.actionsave_config)
        self.menu_conf.addAction(self.del_conf.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_Read.clicked.connect(MainWindow.on_read)
        self.pushButton_Write.clicked.connect(MainWindow.on_write)
        self.pushButton_FindDevice.clicked.connect(MainWindow.on_check)
        self.actionEXIT.triggered.connect(MainWindow.on_exit)
        self.actionnew_config.triggered.connect(MainWindow.newConf)
        self.actionsave_config.triggered.connect(MainWindow.on_save)
        self.pushButton_Gloves.clicked.connect(MainWindow.on_gloves)
        self.pushButton_Hands.clicked.connect(MainWindow.on_hands)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionEXIT.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.actionnew_config.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u914d\u7f6e", None))
        self.actionsave_config.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u914d\u7f6e", None))
        self.actionlabel_config.setText(QCoreApplication.translate("MainWindow", u"\u6240\u6709\u914d\u7f6e", None))
        self.label_ir5.setText(QCoreApplication.translate("MainWindow", u"IR5", None))
        self.label_ir3.setText(QCoreApplication.translate("MainWindow", u"IR3", None))
        self.label_ir1.setText(QCoreApplication.translate("MainWindow", u"IR1", None))
        self.label_k31.setText(QCoreApplication.translate("MainWindow", u"KEY31", None))
        self.label_k29.setText(QCoreApplication.translate("MainWindow", u"KEY29", None))
        self.label_k27.setText(QCoreApplication.translate("MainWindow", u"KEY27", None))
        self.label_k25.setText(QCoreApplication.translate("MainWindow", u"KEY25", None))
        self.label_k23.setText(QCoreApplication.translate("MainWindow", u"KEY23", None))
        self.label_k21.setText(QCoreApplication.translate("MainWindow", u"KEY21", None))
        self.label_k19.setText(QCoreApplication.translate("MainWindow", u"KEY19", None))
        self.label_k17.setText(QCoreApplication.translate("MainWindow", u"KEY17", None))
        self.label_k15.setText(QCoreApplication.translate("MainWindow", u"KEY15", None))
        self.label_k13.setText(QCoreApplication.translate("MainWindow", u"KEY13", None))
        self.label_k11.setText(QCoreApplication.translate("MainWindow", u"KEY11", None))
        self.label_k9.setText(QCoreApplication.translate("MainWindow", u"KEY9", None))
        self.label_k7.setText(QCoreApplication.translate("MainWindow", u"KEY7", None))
        self.label_k5.setText(QCoreApplication.translate("MainWindow", u"KEY5", None))
        self.label_k3.setText(QCoreApplication.translate("MainWindow", u"KEY3", None))
        self.label_k1.setText(QCoreApplication.translate("MainWindow", u"KEY1", None))
        self.label_ir6.setText(QCoreApplication.translate("MainWindow", u"IR6", None))
        self.label_ir4.setText(QCoreApplication.translate("MainWindow", u"IR4", None))
        self.label_ir2.setText(QCoreApplication.translate("MainWindow", u"IR2", None))
        self.label_k32.setText(QCoreApplication.translate("MainWindow", u"KEY32", None))
        self.label_k30.setText(QCoreApplication.translate("MainWindow", u"KEY30", None))
        self.label_k28.setText(QCoreApplication.translate("MainWindow", u"KEY28", None))
        self.label_k26.setText(QCoreApplication.translate("MainWindow", u"KEY26", None))
        self.label_k24.setText(QCoreApplication.translate("MainWindow", u"KEY24", None))
        self.label_k22.setText(QCoreApplication.translate("MainWindow", u"KEY22", None))
        self.label_k20.setText(QCoreApplication.translate("MainWindow", u"KEY20", None))
        self.label_k18.setText(QCoreApplication.translate("MainWindow", u"KEY18", None))
        self.label_k16.setText(QCoreApplication.translate("MainWindow", u"KEY16", None))
        self.label_k14.setText(QCoreApplication.translate("MainWindow", u"KEY14", None))
        self.label_k12.setText(QCoreApplication.translate("MainWindow", u"KEY12", None))
        self.label_k10.setText(QCoreApplication.translate("MainWindow", u"KEY10", None))
        self.label_k8.setText(QCoreApplication.translate("MainWindow", u"KEY8", None))
        self.label_k6.setText(QCoreApplication.translate("MainWindow", u"KEY6", None))
        self.label_k4.setText(QCoreApplication.translate("MainWindow", u"KEY4", None))
        self.label_k2.setText(QCoreApplication.translate("MainWindow", u"KEY2", None))
        self.label_log.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u65e5\u5fd7\uff1a", None))
        self.label_ctrl.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u63a7\u5236\uff1a", None))
        self.checkBox_IR.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u5f00\u542f\u7ea2\u5916", None))
        self.checkBox_Slider.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u5f00\u542f\u6ed1\u6761", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u89e6\u6478\u89e6\u53d1\u9608\u503c(\u8d8a\u4f4e\u8d8a\u7075\u654f)\uff1a", None))
        self.pushButton_FindDevice.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u627e\u8bbe\u5907", None))
        self.pushButton_Read.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u8bbe\u5907", None))
        self.pushButton_Write.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165\u8bbe\u5907", None))
        self.pushButton_Gloves.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u624b\u5957\u6a21\u5f0f", None))
        self.pushButton_Hands.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u7a7a\u624b\u6a21\u5f0f", None))
        self.Ttile.setText(QCoreApplication.translate("MainWindow", u"ChunithmController\u6539\u952e\u5de5\u5177", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_conf.setTitle(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
        self.list_conf.setTitle(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u5217\u8868", None))
        self.del_conf.setTitle(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u914d\u7f6e", None))
    # retranslateUi

