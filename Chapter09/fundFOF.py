# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fundFOF.ui'
#
# Created by: PySide6 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 535))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_parameter_tree = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_parameter_tree.sizePolicy().hasHeightForWidth())
        self.widget_parameter_tree.setSizePolicy(sizePolicy)
        self.widget_parameter_tree.setMinimumSize(QtCore.QSize(100, 0))
        self.widget_parameter_tree.setObjectName("widget_parameter_tree")
        self.horizontalLayout_2.addWidget(self.widget_parameter_tree)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.QWebEngineView_ProductVsHs300 = QWebEngineView(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QWebEngineView_ProductVsHs300.sizePolicy().hasHeightForWidth())
        self.QWebEngineView_ProductVsHs300.setSizePolicy(sizePolicy)
        self.QWebEngineView_ProductVsHs300.setMinimumSize(QtCore.QSize(0, 100))
        self.QWebEngineView_ProductVsHs300.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.QWebEngineView_ProductVsHs300.setObjectName("QWebEngineView_ProductVsHs300")
        self.verticalLayout_3.addWidget(self.QWebEngineView_ProductVsHs300)
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setMinimumSize(QtCore.QSize(200, 200))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.QWebEngineview_MonthReturn = QWebEngineView(self.tab)
        self.QWebEngineview_MonthReturn.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.QWebEngineview_MonthReturn.setObjectName("QWebEngineview_MonthReturn")
        self.verticalLayout_2.addWidget(self.QWebEngineview_MonthReturn)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.QWebEngineView_PeriodReturn = QWebEngineView(self.tab_2)
        self.QWebEngineView_PeriodReturn.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.QWebEngineView_PeriodReturn.setObjectName("QWebEngineView_PeriodReturn")
        self.horizontalLayout.addWidget(self.QWebEngineView_PeriodReturn)
        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.QWebEngineView_LagestBack = QWebEngineView(self.tab_3)
        self.QWebEngineView_LagestBack.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.QWebEngineView_LagestBack.setObjectName("QWebEngineView_LagestBack")
        self.verticalLayout.addWidget(self.QWebEngineView_LagestBack)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基金量化投研系统v0.11"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "月度收益"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "区间收益"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "回撤情况"))

from PySide6.QtWebEngineWidgets import QWebEngineView
