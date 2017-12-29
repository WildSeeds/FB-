# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from 一键重启.一键重启2 import baseconnect
from 一键重启.userinfo import dictuser


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.label.setObjectName("label")
        self.severbox = QtWidgets.QComboBox(self.centralwidget)
        self.severbox.setGeometry(QtCore.QRect(90, 20, 121, 21))
        self.severbox.setObjectName("severbox")
        self.severbox.addItem("")
        self.severbox.addItem("")
        self.severbox.addItem("")
        self.severbox.addItem("")
        self.severbox.addItem("")
        self.severbox.addItem("")
        self.severbox.addItem("")
        self.severbox.addItem("")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 130, 101, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.oraclelisten = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oraclelisten.sizePolicy().hasHeightForWidth())
        self.oraclelisten.setSizePolicy(sizePolicy)
        self.oraclelisten.setObjectName("oraclelisten")
        self.verticalLayout.addWidget(self.oraclelisten)
        self.oracle = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oracle.sizePolicy().hasHeightForWidth())
        self.oracle.setSizePolicy(sizePolicy)
        self.oracle.setObjectName("oracle")
        self.verticalLayout.addWidget(self.oracle)
        self.tomcat = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tomcat.sizePolicy().hasHeightForWidth())
        self.tomcat.setSizePolicy(sizePolicy)
        self.tomcat.setObjectName("tomcat")
        self.verticalLayout.addWidget(self.tomcat)
        self.fb = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fb.sizePolicy().hasHeightForWidth())
        self.fb.setSizePolicy(sizePolicy)
        self.fb.setObjectName("fb")
        self.verticalLayout.addWidget(self.fb)
        self.tq = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tq.sizePolicy().hasHeightForWidth())
        self.tq.setSizePolicy(sizePolicy)
        self.tq.setObjectName("tq")
        self.verticalLayout.addWidget(self.tq)
        self.tqmc = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tqmc.sizePolicy().hasHeightForWidth())
        self.tqmc.setSizePolicy(sizePolicy)
        self.tqmc.setObjectName("tqmc")
        self.verticalLayout.addWidget(self.tqmc)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 80, 461, 461))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 190, 77, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stopbutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.stopbutton.setObjectName("stopbutton")
        self.verticalLayout_2.addWidget(self.stopbutton)
        self.startbutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.startbutton.setObjectName("startbutton")
        self.verticalLayout_2.addWidget(self.startbutton)
        self.rebootbutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.rebootbutton.setObjectName("rebootbutton")
        self.verticalLayout_2.addWidget(self.rebootbutton)
        self.statusbutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.statusbutton.setObjectName("statusbutton")
        self.verticalLayout_2.addWidget(self.statusbutton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 23))
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
        self.label.setText(_translate("MainWindow", "选择服务器"))
        self.severbox.setItemText(0, _translate("MainWindow", "请选择服务器"))
        self.severbox.setItemText(1, _translate("MainWindow", "192.168.70.237"))
        self.severbox.setItemText(2, _translate("MainWindow", "10.20.27.114"))
        self.severbox.setItemText(3, _translate("MainWindow", "10.20.27.63"))
        self.severbox.setItemText(4, _translate("MainWindow", "10.20.27.179"))
        self.severbox.setItemText(5, _translate("MainWindow", "10.20.27.64"))
        self.severbox.setItemText(6, _translate("MainWindow", "10.20.25.124"))
        self.severbox.setItemText(7, _translate("MainWindow", "10.20.36.70"))
        self.oraclelisten.setText(_translate("MainWindow", "oracle监听"))
        self.oracle.setText(_translate("MainWindow", "oracle服务"))
        self.tomcat.setText(_translate("MainWindow", "tomcat服务"))
        self.fb.setText(_translate("MainWindow", "投后中间件"))
        self.tq.setText(_translate("MainWindow", "投前中间件"))
        self.tqmc.setText(_translate("MainWindow", "投前消息中心"))
        self.stopbutton.setText(_translate("MainWindow", "停止"))
        self.startbutton.setText(_translate("MainWindow", "启用"))
        self.rebootbutton.setText(_translate("MainWindow", "重启"))
        self.statusbutton.setText(_translate("MainWindow", "状态查询"))
        self.stopbutton.clicked.connect(self.stopfb)
        self.startbutton.clicked.connect(self.startfb)
        self.rebootbutton.clicked.connect(self.rebootfb)
        self.statusbutton.clicked.connect(self.statusfb)
    def test(self):
        self.textEdit.setText('Text')
    def stopfb(self):
        self.textEdit.clear()
        flag = 0
        if self.oraclelisten.isChecked():
            flag =1
            self._singlestop('oraclelisten')
        if self.oracle.isChecked():
            flag = 1
            self._singlestop('oracle')
        if self.fb.isChecked():
            flag = 1
            self._singlestop('fb')
        if self.tq.isChecked():
            flag = 1
            self._singlestop('tq')
        if self.tqmc.isChecked():
            flag = 1
            self._singlestop('tqmc')
        if self.tomcat.isChecked():
            flag = 1
            self._singlestop('tomcat')
        if  flag == 0:
            self.textEdit.append('请选择要停止的服务')
    def _singlestop(self,name):
        ip = self.severbox.currentText()
        if  ip=='请选择服务器':
            self.textEdit.append('请选择对应服务器IP')
            return
        fbinfo = dictuser[name]
        # print(fbinfo)
        fbobj = baseconnect(ip, fbinfo[1], fbinfo[2], fbinfo[3], fbinfo[4], fbinfo[5], fbinfo[6], fbinfo[7])
        if fbobj.connect():
            try:
                self.textEdit.append(fbobj.stop())
                fbobj.close()
            except Exception as e:
                fbobj.close()
                self.textEdit.append(e)
        else:
            self.textEdit.append('连接失败')
    def startfb(self):
        self.textEdit.clear()
        try:
            flag = 0
            if self.oraclelisten.isChecked():
                flag = 1
                self._singlestart('oraclelisten')
            if self.oracle.isChecked():
                flag = 1
                self._singlestart('oracle')
            if self.fb.isChecked():
                flag = 1
                self._singlestart('fb')
            if self.tq.isChecked():
                flag = 1
                self._singlestart('tq')
            if self.tqmc.isChecked():
                flag = 1
                self._singlestart('tqmc')
            if self.tomcat.isChecked():
                flag = 1
                self._singlestart('tomcat')
            if not flag:
                self.textEdit.append('请选择要启动的服务')
        except Exception as e:
            self.textEdit.append(e)
    def _singlestart(self,name):
        ip = self.severbox.currentText()
        if  ip=='请选择服务器':
            self.textEdit.append('请选择对应服务器IP')
            return
        fbinfo = dictuser[name]
        # print(fbinfo)
        fbobj = baseconnect(ip, fbinfo[1], fbinfo[2], fbinfo[3], fbinfo[4], fbinfo[5], fbinfo[6], fbinfo[7])
        if fbobj.connect():
            try:
                a = fbobj.startup()
                self.textEdit.append(a)
                fbobj.close()
            except Exception as e:
                fbobj.close()
                self.textEdit.append(e)
        else:
            self.textEdit.append('连接失败')
    def rebootfb(self):
        self.textEdit.clear()
        try:
            flag = 0
            if self.oraclelisten.isChecked():
                flag = 1
                self._singlesreboot('oraclelisten')
            if self.oracle.isChecked():
                flag = 1
                self._singlesreboot('oracle')
            if self.fb.isChecked():
                flag = 1
                self._singlesreboot('fb')
            if self.tq.isChecked():
                flag = 1
                self._singlesreboot('tq')
            if self.tqmc.isChecked():
                flag = 1
                self._singlesreboot('tqmc')
            if self.tomcat.isChecked():
                flag = 1
                self._singlesreboot('tomcat')
            if not flag:
                self.textEdit.append('请选择要启动的服务')
        except Exception as e:
            self.textEdit.append(e)
    def _singlesreboot(self, name):
        ip = self.severbox.currentText()
        if ip == '请选择服务器':
            self.textEdit.append('请选择对应服务器IP')
            return
        fbinfo = dictuser[name]
        # print(fbinfo)
        fbobj = baseconnect(ip, fbinfo[1], fbinfo[2], fbinfo[3], fbinfo[4], fbinfo[5], fbinfo[6], fbinfo[7])
        if fbobj.connect():
            try:
                self.textEdit.append(fbobj.stop())
                self.textEdit.append(fbobj.startup())
                fbobj.close()
            except Exception as e:
                fbobj.close()
                self.textEdit.append(e)
        else:
            self.textEdit.append('连接失败')

    def statusfb(self):
        self.textEdit.clear()
        try:
            flag = 0
            if self.oraclelisten.isChecked():
                flag = 1
                self._singlestatus('oraclelisten')
            if self.oracle.isChecked():
                flag = 1
                self._singlestatus('oracle')
            if self.fb.isChecked():
                flag = 1
                self._singlestatus('fb')
            if self.tq.isChecked():
                flag = 1
                self._singlestatus('tq')
            if self.tqmc.isChecked():
                flag = 1
                self._singlestatus('tqmc')
            if self.tomcat.isChecked():
                flag = 1
                self._singlestatus('tomcat')
            if  flag ==0:
                self.textEdit.append('请选择要启动的服务')
        except Exception as e:
            print(e)
            self.textEdit.append(e)
    def _singlestatus(self,name):
        ip = self.severbox.currentText()
        if ip == '请选择服务器':
            self.textEdit.append('请选择对应服务器IP')
            return
        fbinfo = dictuser[name]
        # print(fbinfo)
        fbobj = baseconnect(ip, fbinfo[1], fbinfo[2], fbinfo[3], fbinfo[4], fbinfo[5], fbinfo[6], fbinfo[7])
        if fbobj.connect():
            try:
                self.textEdit.append(fbobj.getstatus())
                fbobj.close()
            except Exception as e:
                fbobj.close()
                self.textEdit.append(e)
        else:
            self.textEdit.append('连接失败')
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    mainwindow = QtWidgets.QMainWindow()
    ex.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
