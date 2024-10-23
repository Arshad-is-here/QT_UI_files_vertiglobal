# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'working.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1042, 627)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 211, 591))
        self.label.setStyleSheet("\n"
"background-color: rgb(61, 130, 219);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 0, 831, 201))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lefteye_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lefteye_label.setObjectName("lefteye_label")
        self.horizontalLayout.addWidget(self.lefteye_label)
        self.right_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.right_label.setObjectName("right_label")
        self.horizontalLayout.addWidget(self.right_label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(220, 210, 601, 181))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.topgraph_1_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.topgraph_1_label.setObjectName("topgraph_1_label")
        self.horizontalLayout_2.addWidget(self.topgraph_1_label)
        self.topgraph2_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.topgraph2_label.setObjectName("topgraph2_label")
        self.horizontalLayout_2.addWidget(self.topgraph2_label)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(220, 390, 601, 181))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bottomgraph1_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.bottomgraph1_label.setObjectName("bottomgraph1_label")
        self.horizontalLayout_3.addWidget(self.bottomgraph1_label)
        self.bottomgraph_2label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.bottomgraph_2label.setObjectName("bottomgraph_2label")
        self.horizontalLayout_3.addWidget(self.bottomgraph_2label)
        self.avatar_label = QtWidgets.QLabel(self.centralwidget)
        self.avatar_label.setGeometry(QtCore.QRect(830, 210, 201, 351))
        self.avatar_label.setObjectName("avatar_label")
        self.Calibrate_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Calibrate_pushButton.setGeometry(QtCore.QRect(30, 190, 151, 41))
        self.Calibrate_pushButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"border-radius:15px;\n"
"  padding: 10px;\n"
"\n"
"")
        self.Calibrate_pushButton.setObjectName("Calibrate_pushButton")
        self.Save_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Save_pushButton.setGeometry(QtCore.QRect(20, 340, 161, 51))
        self.Save_pushButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"border-radius:15px;\n"
"  padding: 10px;\n"
"\n"
"")
        self.Save_pushButton.setObjectName("Save_pushButton")
        self.play_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.play_pushButton.setGeometry(QtCore.QRect(20, 270, 71, 41))
        self.play_pushButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"border-radius:15px;\n"
"  padding: 10px;\n"
"\n"
"button.setStyleSheet(\"qproperty-icon: url(\"F:\\.venv\\The_GUI_dr\\Screenshot 2024-10-07 025553.png\");\");")
        self.play_pushButton.setObjectName("play_pushButton")
        self.stop_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stop_pushButton.setGeometry(QtCore.QRect(120, 270, 71, 41))
        self.stop_pushButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"border-radius:15px;\n"
"  padding: 10px;\n"
"\n"
"button.setStyleSheet(\"qproperty-icon: url(\"F:\\.venv\\The_GUI_dr\\Screenshot 2024-10-07 025553.png\");\");")
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.Home_label = QtWidgets.QLabel(self.centralwidget)
        self.Home_label.setGeometry(QtCore.QRect(50, 500, 31, 41))
        self.Home_label.setStyleSheet("background-image: url(:/newPrefix/Screenshot 2024-10-07 030545.png);")
        self.Home_label.setText("")
        self.Home_label.setObjectName("Home_label")
        self.setting_label = QtWidgets.QLabel(self.centralwidget)
        self.setting_label.setGeometry(QtCore.QRect(130, 500, 31, 41))
        self.setting_label.setStyleSheet("background-image: url(:/newPrefix/Screenshot 2024-10-07 030649.png);")
        self.setting_label.setText("")
        self.setting_label.setObjectName("setting_label")
        self.timer_label = QtWidgets.QLabel(self.centralwidget)
        self.timer_label.setGeometry(QtCore.QRect(20, 30, 161, 121))
        self.timer_label.setObjectName("timer_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1042, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lefteye_label.setText(_translate("MainWindow", "TextLabel"))
        self.right_label.setText(_translate("MainWindow", "TextLabel"))
        self.topgraph_1_label.setText(_translate("MainWindow", "TextLabel"))
        self.topgraph2_label.setText(_translate("MainWindow", "TextLabel"))
        self.bottomgraph1_label.setText(_translate("MainWindow", "TextLabel"))
        self.bottomgraph_2label.setText(_translate("MainWindow", "TextLabel"))
        self.avatar_label.setText(_translate("MainWindow", "TextLabel"))
        self.Calibrate_pushButton.setText(_translate("MainWindow", "Caliberate"))
        self.Save_pushButton.setText(_translate("MainWindow", "Save"))
        self.play_pushButton.setText(_translate("MainWindow", "P"))
        self.stop_pushButton.setText(_translate("MainWindow", "S"))
        self.timer_label.setText(_translate("MainWindow", "TextLabel"))
import this_is_resource_rc
