# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layoutWin.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 888)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(160, 60, 275, 37))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.formLayoutWidget)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 550, 324, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.doubleSpinBox_returns_max = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_returns_max.setObjectName("doubleSpinBox_returns_max")
        self.gridLayout_3.addWidget(self.doubleSpinBox_returns_max, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 1, 1, 1)
        self.doubleSpinBox_maxdrawdown_min = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_maxdrawdown_min.setObjectName("doubleSpinBox_maxdrawdown_min")
        self.gridLayout_3.addWidget(self.doubleSpinBox_maxdrawdown_min, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)
        self.doubleSpinBox_maxdrawdrawdown_max = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_maxdrawdrawdown_max.setObjectName("doubleSpinBox_maxdrawdrawdown_max")
        self.gridLayout_3.addWidget(self.doubleSpinBox_maxdrawdrawdown_max, 2, 2, 1, 1)
        self.doubleSpinBox_sharp_min = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_sharp_min.setObjectName("doubleSpinBox_sharp_min")
        self.gridLayout_3.addWidget(self.doubleSpinBox_sharp_min, 3, 1, 1, 1)
        self.doubleSpinBox_sharp_max = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_sharp_max.setObjectName("doubleSpinBox_sharp_max")
        self.gridLayout_3.addWidget(self.doubleSpinBox_sharp_max, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.doubleSpinBox_returns_min = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_returns_min.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_returns_min.setSizePolicy(sizePolicy)
        self.doubleSpinBox_returns_min.setObjectName("doubleSpinBox_returns_min")
        self.gridLayout_3.addWidget(self.doubleSpinBox_returns_min, 1, 1, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(510, 620, 99, 27))
        self.pushButton_19.setObjectName("pushButton_19")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(160, 120, 148, 97))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(151, 340, 360, 128))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 1, 3, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 2, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 2, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 2, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 2, 3, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 3, 3, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 3, 0, 1, 3)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(491, 110, 239, 101))
        self.widget2.setObjectName("widget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_2.addWidget(self.pushButton_17, 2, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_2.addWidget(self.pushButton_18, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1128, 25))
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
        self.label.setText(_translate("MainWindow", "姓名"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_19.setText(_translate("MainWindow", "PushButton"))
        self.label_2.setText(_translate("MainWindow", "姓名"))
        self.pushButton_2.setText(_translate("MainWindow", "确定"))
        self.pushButton_4.setText(_translate("MainWindow", "8"))
        self.pushButton_5.setText(_translate("MainWindow", "7"))
        self.pushButton_6.setText(_translate("MainWindow", "+"))
        self.pushButton_9.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "5"))
        self.pushButton_8.setText(_translate("MainWindow", "4"))
        self.pushButton_11.setText(_translate("MainWindow", "-"))
        self.pushButton_12.setText(_translate("MainWindow", "3"))
        self.pushButton_10.setText(_translate("MainWindow", "2"))
        self.pushButton_13.setText(_translate("MainWindow", "1"))
        self.pushButton_14.setText(_translate("MainWindow", "*"))
        self.pushButton_16.setText(_translate("MainWindow", "/"))
        self.pushButton_15.setText(_translate("MainWindow", "Calculate"))
        self.pushButton_3.setText(_translate("MainWindow", "9"))
        self.label_3.setText(_translate("MainWindow", "用户"))
        self.label_4.setText(_translate("MainWindow", "密码"))
        self.pushButton_17.setText(_translate("MainWindow", "确定"))
        self.pushButton_18.setText(_translate("MainWindow", "取消"))


class LayoutDemo(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    @QtCore.pyqtSlot()
    def on_pushButton_19_clicked(self):
        print("收益_min: ", self.doubleSpinBox_returns_min.text())
        print("收益_max: ", self.doubleSpinBox_returns_max.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = LayoutDemo()
    ui.show()
    sys.exit(app.exec_())