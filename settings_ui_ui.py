# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Files\PythonFiles\WC\WindowsCleaner\resource\ui\settings_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Settings_UI_Form(object):
    def setupUi(self, Settings_UI_Form):
        Settings_UI_Form.setObjectName("Settings_UI_Form")
        Settings_UI_Form.resize(410, 505)
        self.gridLayout_7 = QtWidgets.QGridLayout(Settings_UI_Form)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.widget_5 = CardWidget(Settings_UI_Form)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.widget_5.setFont(font)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = CaptionLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.comboBox_7 = ComboBox(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_7)
        self.gridLayout_5.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget_5, 2, 1, 1, 1)
        self.widget_4 = CardWidget(Settings_UI_Form)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.widget_4.setFont(font)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_2 = PrimaryPushButton(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_12.addWidget(self.pushButton_2)
        self.label_11 = QtWidgets.QLabel(self.widget_4)
        self.label_11.setMinimumSize(QtCore.QSize(55, 24))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_11.setFont(font)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.gridLayout_4.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget_4, 3, 1, 1, 1)
        self.widget_3 = CardWidget(Settings_UI_Form)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.widget_3.setFont(font)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.AutoRun_2 = CheckBox(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.AutoRun_2.setFont(font)
        self.AutoRun_2.setObjectName("AutoRun_2")
        self.horizontalLayout_7.addWidget(self.AutoRun_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget_3, 4, 1, 1, 1)
        self.widget_2 = CardWidget(Settings_UI_Form)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = CaptionLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.comboBox_5 = ComboBox(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_5)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget_2, 5, 1, 1, 1)
        self.widget = CardWidget(Settings_UI_Form)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = CaptionLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.comboBox_6 = ComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_6)
        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget, 6, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 177, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem5, 7, 1, 1, 1)
        self.widget_6 = CardWidget(Settings_UI_Form)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.widget_6.setFont(font)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = CaptionLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.comboBox_8 = ComboBox(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_8)
        self.gridLayout_6.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget_6, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Settings_UI_Form)
        self.label_6.setMinimumSize(QtCore.QSize(0, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 0, 1, 1, 1)

        self.retranslateUi(Settings_UI_Form)
        QtCore.QMetaObject.connectSlotsByName(Settings_UI_Form)

    def retranslateUi(self, Settings_UI_Form):
        _translate = QtCore.QCoreApplication.translate
        Settings_UI_Form.setWindowTitle(_translate("Settings_UI_Form", "Form"))
        self.label_9.setText(_translate("Settings_UI_Form", "主题"))
        self.comboBox_7.setItemText(0, _translate("Settings_UI_Form", "亮色"))
        self.comboBox_7.setItemText(1, _translate("Settings_UI_Form", "暗色"))
        self.comboBox_7.setItemText(2, _translate("Settings_UI_Form", "跟随系统"))
        self.pushButton_2.setText(_translate("Settings_UI_Form", "选择主题色"))
        self.AutoRun_2.setText(_translate("Settings_UI_Form", "开机自启"))
        self.label_7.setText(_translate("Settings_UI_Form", "关闭选项"))
        self.comboBox_5.setItemText(0, _translate("Settings_UI_Form", "每次询问"))
        self.comboBox_5.setItemText(1, _translate("Settings_UI_Form", "退出程序"))
        self.comboBox_5.setItemText(2, _translate("Settings_UI_Form", "最小化到系统托盘"))
        self.label_8.setText(_translate("Settings_UI_Form", "自动检查更新"))
        self.comboBox_6.setItemText(0, _translate("Settings_UI_Form", "从不"))
        self.comboBox_6.setItemText(1, _translate("Settings_UI_Form", "每次启动时"))
        self.comboBox_6.setItemText(2, _translate("Settings_UI_Form", "每周一次"))
        self.label_10.setText(_translate("Settings_UI_Form", "语言"))
        self.comboBox_8.setItemText(0, _translate("Settings_UI_Form", "简体中文"))
from qfluentwidgets import CaptionLabel, CardWidget, CheckBox, ComboBox, PrimaryPushButton
