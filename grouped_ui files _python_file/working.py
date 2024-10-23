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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(220, 0, 811, 581))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lefteye_label = QtWidgets.QLabel(self.widget)
        self.lefteye_label.setObjectName("lefteye_label")
        self.horizontalLayout.addWidget(self.lefteye_label)
        self.right_label = QtWidgets.QLabel(self.widget)
        self.right_label.setObjectName("right_label")
        self.horizontalLayout.addWidget(self.right_label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.topgraph_1_label = QtWidgets.QLabel(self.widget)
        self.topgraph_1_label.setObjectName("topgraph_1_label")
        self.horizontalLayout_2.addWidget(self.topgraph_1_label)
        self.topgraph2_label = QtWidgets.QLabel(self.widget)
        self.topgraph2_label.setObjectName("topgraph2_label")
        self.horizontalLayout_2.addWidget(self.topgraph2_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bottomgraph1_label = QtWidgets.QLabel(self.widget)
        self.bottomgraph1_label.setObjectName("bottomgraph1_label")
        self.horizontalLayout_3.addWidget(self.bottomgraph1_label)
        self.bottomgraph_2label = QtWidgets.QLabel(self.widget)
        self.bottomgraph_2label.setObjectName("bottomgraph_2label")
        self.horizontalLayout_3.addWidget(self.bottomgraph_2label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.avatar_label = QtWidgets.QLabel(self.widget)
        self.avatar_label.setObjectName("avatar_label")
        self.gridLayout.addWidget(self.avatar_label, 1, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 30, 181, 521))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.timer_label = QtWidgets.QLabel(self.widget1)
        self.timer_label.setObjectName("timer_label")
        self.verticalLayout_3.addWidget(self.timer_label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Calibrate_pushButton = QtWidgets.QPushButton(self.widget1)
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
        self.verticalLayout_2.addWidget(self.Calibrate_pushButton)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.play_pushButton = QtWidgets.QPushButton(self.widget1)
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
        self.horizontalLayout_4.addWidget(self.play_pushButton)
        self.stop_pushButton = QtWidgets.QPushButton(self.widget1)
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
        self.horizontalLayout_4.addWidget(self.stop_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.Save_pushButton = QtWidgets.QPushButton(self.widget1)
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
        self.verticalLayout.addWidget(self.Save_pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Home_label = QtWidgets.QLabel(self.widget1)
        self.Home_label.setStyleSheet("background-image: url(:/newPrefix/Screenshot 2024-10-07 030545.png);")
        self.Home_label.setText("")
        self.Home_label.setObjectName("Home_label")
        self.horizontalLayout_5.addWidget(self.Home_label)
        self.setting_label = QtWidgets.QLabel(self.widget1)
        self.setting_label.setStyleSheet("background-image: url(:/newPrefix/Screenshot 2024-10-07 030649.png);")
        self.setting_label.setText("")
        self.setting_label.setObjectName("setting_label")
        self.horizontalLayout_5.addWidget(self.setting_label)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.label.raise_()
        self.avatar_label.raise_()
        self.Calibrate_pushButton.raise_()
        self.Save_pushButton.raise_()
        self.play_pushButton.raise_()
        self.stop_pushButton.raise_()
        self.Home_label.raise_()
        self.timer_label.raise_()
        self.setting_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1042, 21))
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
        self.timer_label.setText(_translate("MainWindow", "TextLabel"))
        self.Calibrate_pushButton.setText(_translate("MainWindow", "Caliberate"))
        self.play_pushButton.setText(_translate("MainWindow", "P"))
        self.stop_pushButton.setText(_translate("MainWindow", "S"))
        self.Save_pushButton.setText(_translate("MainWindow", "Save"))
import this_is_resource_rc
