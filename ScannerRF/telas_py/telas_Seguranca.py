# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telas_Seguranca.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 825)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.menu_icons = QtWidgets.QWidget(self.centralwidget)
        self.menu_icons.setMinimumSize(QtCore.QSize(100, 0))
        self.menu_icons.setStyleSheet("QWidget{\n"
"    background-color:#069E6E;\n"
"}")
        self.menu_icons.setObjectName("menu_icons")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menu_icons)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnHomeLateral = QtWidgets.QPushButton(self.menu_icons)
        self.btnHomeLateral.setMinimumSize(QtCore.QSize(0, 80))
        self.btnHomeLateral.setStyleSheet("QPushButton{\n"
"    background-color:#069E6E;\n"
"    color:#ffffff;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#047b55;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}")
        self.btnHomeLateral.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imagens/imgBtnHome.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHomeLateral.setIcon(icon)
        self.btnHomeLateral.setIconSize(QtCore.QSize(36, 36))
        self.btnHomeLateral.setCheckable(True)
        self.btnHomeLateral.setAutoExclusive(True)
        self.btnHomeLateral.setObjectName("btnHomeLateral")
        self.verticalLayout.addWidget(self.btnHomeLateral)
        self.btnScannerLateral = QtWidgets.QPushButton(self.menu_icons)
        self.btnScannerLateral.setMinimumSize(QtCore.QSize(0, 80))
        self.btnScannerLateral.setStyleSheet("QPushButton{\n"
"    background-color:#069E6E;\n"
"    color:#ffffff;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#047b55;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}")
        self.btnScannerLateral.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imagens/imgBtnRFacial.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnScannerLateral.setIcon(icon1)
        self.btnScannerLateral.setIconSize(QtCore.QSize(36, 36))
        self.btnScannerLateral.setCheckable(True)
        self.btnScannerLateral.setAutoExclusive(True)
        self.btnScannerLateral.setObjectName("btnScannerLateral")
        self.verticalLayout.addWidget(self.btnScannerLateral)
        self.btnEntradasLateral = QtWidgets.QPushButton(self.menu_icons)
        self.btnEntradasLateral.setMinimumSize(QtCore.QSize(0, 80))
        self.btnEntradasLateral.setStyleSheet("QPushButton{\n"
"    background-color:#069E6E;\n"
"    color:#ffffff;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#047b55;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}")
        self.btnEntradasLateral.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imagens/imgBtnEntrada.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEntradasLateral.setIcon(icon2)
        self.btnEntradasLateral.setIconSize(QtCore.QSize(36, 36))
        self.btnEntradasLateral.setCheckable(True)
        self.btnEntradasLateral.setAutoExclusive(True)
        self.btnEntradasLateral.setObjectName("btnEntradasLateral")
        self.verticalLayout.addWidget(self.btnEntradasLateral)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 465, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.btnVoltarLateral = QtWidgets.QPushButton(self.menu_icons)
        self.btnVoltarLateral.setMinimumSize(QtCore.QSize(0, 80))
        self.btnVoltarLateral.setStyleSheet("QPushButton{\n"
"    background-color:#069E6E;\n"
"    color:#ffffff;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#047b55;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:  rgb(2, 45, 29);\n"
"}\n"
"\n"
"")
        self.btnVoltarLateral.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imagens/imgBtnVoltar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVoltarLateral.setIcon(icon3)
        self.btnVoltarLateral.setIconSize(QtCore.QSize(36, 36))
        self.btnVoltarLateral.setObjectName("btnVoltarLateral")
        self.verticalLayout_3.addWidget(self.btnVoltarLateral)
        self.btnDesconectarLateral = QtWidgets.QPushButton(self.menu_icons)
        self.btnDesconectarLateral.setMinimumSize(QtCore.QSize(0, 80))
        self.btnDesconectarLateral.setStyleSheet("QPushButton{\n"
"    background-color:#069E6E;\n"
"    color:#ffffff;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#047b55;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:  rgb(2, 45, 29);\n"
"}\n"
"\n"
"")
        self.btnDesconectarLateral.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imagens/imgBtnDesconectar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDesconectarLateral.setIcon(icon4)
        self.btnDesconectarLateral.setIconSize(QtCore.QSize(34, 34))
        self.btnDesconectarLateral.setObjectName("btnDesconectarLateral")
        self.verticalLayout_3.addWidget(self.btnDesconectarLateral)
        self.gridLayout.addWidget(self.menu_icons, 1, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.125 rgba(0, 135, 92, 255), stop:0.875 rgba(0, 66, 50, 198));")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pg_Home = QtWidgets.QWidget()
        self.pg_Home.setObjectName("pg_Home")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.pg_Home)
        self.gridLayout_6.setContentsMargins(50, 150, 50, 150)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.pg_Home)
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.widget_4 = QtWidgets.QWidget(self.frame_4)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setMinimumSize(QtCore.QSize(0, 90))
        self.label_2.setMaximumSize(QtCore.QSize(700, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(70)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.gridLayout_7.addWidget(self.widget_4, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem3, 3, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.btnDesconectar_PgHome = QtWidgets.QPushButton(self.frame_5)
        self.btnDesconectar_PgHome.setMinimumSize(QtCore.QSize(300, 50))
        self.btnDesconectar_PgHome.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnDesconectar_PgHome.setFont(font)
        self.btnDesconectar_PgHome.setStyleSheet("QPushButton{\n"
"    background-color:#069E6E;\n"
"    color:#ffffff;\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#047b55;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:  rgb(2, 45, 29);\n"
"}\n"
"\n"
"")
        self.btnDesconectar_PgHome.setIcon(icon4)
        self.btnDesconectar_PgHome.setIconSize(QtCore.QSize(36, 36))
        self.btnDesconectar_PgHome.setObjectName("btnDesconectar_PgHome")
        self.gridLayout_9.addWidget(self.btnDesconectar_PgHome, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_5, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem4, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.pg_Home)
        self.pg_Entradas = QtWidgets.QWidget()
        self.pg_Entradas.setObjectName("pg_Entradas")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pg_Entradas)
        self.gridLayout_3.setContentsMargins(50, 50, 50, 50)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.pg_Entradas)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.widget_2 = QtWidgets.QWidget(self.frame_2)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.etyPesquisar_PgEntradas = QtWidgets.QLineEdit(self.frame_2)
        self.etyPesquisar_PgEntradas.setMinimumSize(QtCore.QSize(450, 0))
        self.etyPesquisar_PgEntradas.setMaximumSize(QtCore.QSize(16777215, 30))
        self.etyPesquisar_PgEntradas.setStyleSheet("QLineEdit{\n"
"    background-color:#069E6E;\n"
"    border: 2px solid #069E6E;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"")
        self.etyPesquisar_PgEntradas.setObjectName("etyPesquisar_PgEntradas")
        self.horizontalLayout_2.addWidget(self.etyPesquisar_PgEntradas)
        self.btnPesquisar_PgEntradas = QtWidgets.QPushButton(self.frame_2)
        self.btnPesquisar_PgEntradas.setMinimumSize(QtCore.QSize(60, 30))
        self.btnPesquisar_PgEntradas.setMaximumSize(QtCore.QSize(606, 30))
        self.btnPesquisar_PgEntradas.setStyleSheet("QPushButton{\n"
"    background-color:#047b55;\n"
"    color:#ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(44, 97, 70);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}\n"
"")
        self.btnPesquisar_PgEntradas.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imagens/imgPesquisar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar_PgEntradas.setIcon(icon5)
        self.btnPesquisar_PgEntradas.setIconSize(QtCore.QSize(25, 25))
        self.btnPesquisar_PgEntradas.setObjectName("btnPesquisar_PgEntradas")
        self.horizontalLayout_2.addWidget(self.btnPesquisar_PgEntradas)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem10)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 500))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 650))
        self.tableWidget.setRowCount(20)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_5.addWidget(self.tableWidget)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem11)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.pg_Entradas)
        self.pg_Scanner = QtWidgets.QWidget()
        self.pg_Scanner.setObjectName("pg_Scanner")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.pg_Scanner)
        self.gridLayout_4.setContentsMargins(50, 50, 50, 50)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.pg_Scanner)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.pg_Scanner)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 1, 2, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget.setStyleSheet("QWidget{\n"
" background-color:#ffffff;\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnIconMenu = QtWidgets.QPushButton(self.widget)
        self.btnIconMenu.setMinimumSize(QtCore.QSize(100, 80))
        self.btnIconMenu.setStyleSheet("QPushButton{\n"
"    background-color:#069E6E;\n"
"    color:#ffffff;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#047b55;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:#069E6E;\n"
"}\n"
"\n"
"")
        self.btnIconMenu.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/imagens/imgBtnMenu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIconMenu.setIcon(icon6)
        self.btnIconMenu.setIconSize(QtCore.QSize(30, 32))
        self.btnIconMenu.setCheckable(True)
        self.btnIconMenu.setObjectName("btnIconMenu")
        self.horizontalLayout_3.addWidget(self.btnIconMenu)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.btnScanner = QtWidgets.QPushButton(self.widget)
        self.btnScanner.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnScanner.setFont(font)
        self.btnScanner.setStyleSheet("QPushButton{\n"
"    background-color:#069E6E;\n"
"    color:#ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#047b55;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:  rgb(2, 45, 29);\n"
"}\n"
"\n"
"")
        self.btnScanner.setIcon(icon1)
        self.btnScanner.setIconSize(QtCore.QSize(36, 36))
        self.btnScanner.setObjectName("btnScanner")
        self.horizontalLayout_3.addWidget(self.btnScanner)
        spacerItem13 = QtWidgets.QSpacerItem(114, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(60, 70))
        self.label_4.setMaximumSize(QtCore.QSize(60, 70))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/imagens/imgLogo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem14 = QtWidgets.QSpacerItem(113, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.btnEntradas = QtWidgets.QPushButton(self.widget)
        self.btnEntradas.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnEntradas.setFont(font)
        self.btnEntradas.setStyleSheet("QPushButton{\n"
"    background-color:#069E6E;\n"
"    color:#ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#047b55;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:  rgb(2, 45, 29);\n"
"}\n"
"\n"
"")
        self.btnEntradas.setIcon(icon2)
        self.btnEntradas.setIconSize(QtCore.QSize(36, 36))
        self.btnEntradas.setObjectName("btnEntradas")
        self.horizontalLayout_3.addWidget(self.btnEntradas)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 3)
        self.menu_todo = QtWidgets.QWidget(self.centralwidget)
        self.menu_todo.setMinimumSize(QtCore.QSize(200, 50))
        self.menu_todo.setStyleSheet("QWidget{\n"
"    background-color:#069E6E;\n"
"}")
        self.menu_todo.setObjectName("menu_todo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.menu_todo)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnHomeLAberto = QtWidgets.QPushButton(self.menu_todo)
        self.btnHomeLAberto.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnHomeLAberto.setFont(font)
        self.btnHomeLAberto.setStyleSheet("QPushButton{\n"
"    background-color:#069E6E;\n"
"    color:#ffffff;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#047b55;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}")
        self.btnHomeLAberto.setIcon(icon)
        self.btnHomeLAberto.setIconSize(QtCore.QSize(36, 36))
        self.btnHomeLAberto.setCheckable(True)
        self.btnHomeLAberto.setAutoExclusive(True)
        self.btnHomeLAberto.setObjectName("btnHomeLAberto")
        self.verticalLayout_2.addWidget(self.btnHomeLAberto)
        self.btnScannerLAberto = QtWidgets.QPushButton(self.menu_todo)
        self.btnScannerLAberto.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnScannerLAberto.setFont(font)
        self.btnScannerLAberto.setStyleSheet("QPushButton{\n"
"    background-color:#069E6E;\n"
"    color:#ffffff;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#047b55;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}\n"
"")
        self.btnScannerLAberto.setIcon(icon1)
        self.btnScannerLAberto.setIconSize(QtCore.QSize(36, 36))
        self.btnScannerLAberto.setCheckable(True)
        self.btnScannerLAberto.setAutoExclusive(True)
        self.btnScannerLAberto.setObjectName("btnScannerLAberto")
        self.verticalLayout_2.addWidget(self.btnScannerLAberto)
        self.btnEntradasLAberto = QtWidgets.QPushButton(self.menu_todo)
        self.btnEntradasLAberto.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnEntradasLAberto.setFont(font)
        self.btnEntradasLAberto.setStyleSheet("QPushButton{\n"
"    background-color:#069E6E;\n"
"    color:#ffffff;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#047b55;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}\n"
"\n"
"\n"
"")
        self.btnEntradasLAberto.setIcon(icon2)
        self.btnEntradasLAberto.setIconSize(QtCore.QSize(36, 36))
        self.btnEntradasLAberto.setCheckable(True)
        self.btnEntradasLAberto.setAutoExclusive(True)
        self.btnEntradasLAberto.setObjectName("btnEntradasLAberto")
        self.verticalLayout_2.addWidget(self.btnEntradasLAberto)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem16 = QtWidgets.QSpacerItem(20, 465, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem16)
        self.btnVoltarLAberto = QtWidgets.QPushButton(self.menu_todo)
        self.btnVoltarLAberto.setMinimumSize(QtCore.QSize(0, 80))
        self.btnVoltarLAberto.setStyleSheet("QPushButton{\n"
"    background-color:#069E6E;\n"
"    color:#ffffff;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#047b55;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:  rgb(2, 45, 29);\n"
"}\n"
"\n"
"")
        self.btnVoltarLAberto.setIcon(icon3)
        self.btnVoltarLAberto.setIconSize(QtCore.QSize(36, 36))
        self.btnVoltarLAberto.setObjectName("btnVoltarLAberto")
        self.verticalLayout_4.addWidget(self.btnVoltarLAberto)
        self.btnDesconectarLAberto = QtWidgets.QPushButton(self.menu_todo)
        self.btnDesconectarLAberto.setMinimumSize(QtCore.QSize(0, 80))
        self.btnDesconectarLAberto.setStyleSheet("QPushButton{\n"
"    background-color:#069E6E;\n"
"    color:#ffffff;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#047b55;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 45, 29);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:  rgb(2, 45, 29);\n"
"}\n"
"\n"
"")
        self.btnDesconectarLAberto.setIcon(icon4)
        self.btnDesconectarLAberto.setIconSize(QtCore.QSize(32, 32))
        self.btnDesconectarLAberto.setObjectName("btnDesconectarLAberto")
        self.verticalLayout_4.addWidget(self.btnDesconectarLAberto)
        self.gridLayout.addWidget(self.menu_todo, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.btnIconMenu.toggled['bool'].connect(self.menu_icons.setVisible) # type: ignore
        self.btnIconMenu.toggled['bool'].connect(self.menu_todo.setHidden) # type: ignore
        self.btnHomeLateral.toggled['bool'].connect(self.btnHomeLAberto.setChecked) # type: ignore
        self.btnScannerLateral.toggled['bool'].connect(self.btnScannerLAberto.setChecked) # type: ignore
        self.btnEntradasLateral.toggled['bool'].connect(self.btnEntradasLAberto.setChecked) # type: ignore
        self.btnHomeLAberto.toggled['bool'].connect(self.btnHomeLateral.setChecked) # type: ignore
        self.btnScannerLAberto.toggled['bool'].connect(self.btnScannerLateral.setChecked) # type: ignore
        self.btnEntradasLAberto.toggled['bool'].connect(self.btnEntradasLateral.setChecked) # type: ignore
        self.btnDesconectarLAberto.clicked.connect(MainWindow.close) # type: ignore
        self.btnDesconectarLateral.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Segurança | Sistema de Reconhecimento Facial"))
        self.label_2.setText(_translate("MainWindow", "Olá, Nome"))
        self.btnDesconectar_PgHome.setText(_translate("MainWindow", " Desconectar"))
        self.label_3.setText(_translate("MainWindow", "HISTÓRICO DE ENTRADAS"))
        self.etyPesquisar_PgEntradas.setPlaceholderText(_translate("MainWindow", "Pesquisar pelos critérios de status “No horário”, “Atrasado” ou “Limite excedido”."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "RM"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Período"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Horário"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Status"))
        self.btnScanner.setText(_translate("MainWindow", "Scanner"))
        self.btnEntradas.setText(_translate("MainWindow", "Entradas"))
        self.btnHomeLAberto.setText(_translate("MainWindow", "Início"))
        self.btnScannerLAberto.setText(_translate("MainWindow", "Scanner"))
        self.btnEntradasLAberto.setText(_translate("MainWindow", "Entradas"))
        self.btnVoltarLAberto.setText(_translate("MainWindow", " Voltar"))
        self.btnDesconectarLAberto.setText(_translate("MainWindow", " Desconectar"))
import imagens.imagens_usadas_rc
