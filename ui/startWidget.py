# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1242, 710)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.treeView = QtWidgets.QTreeView(self.splitter_2)
        self.treeView.setObjectName("treeView")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(9)
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(9)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        self.horizontalLayout.addWidget(self.treeWidget)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(9)
        self.tab_2.setFont(font)
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_2.addWidget(self.textEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.treeWidget_1 = QtWidgets.QTreeWidget(self.splitter_2)
        self.treeWidget_1.setObjectName("treeWidget_1")
        self.treeWidget_1.header().setDefaultSectionSize(110)
        self.treeWidget_1.header().setHighlightSections(False)
        self.treeWidget_1.header().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1242, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.File = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.File.setFont(font)
        self.File.setObjectName("File")
        self.Edit = QtWidgets.QMenu(self.menubar)
        self.Edit.setObjectName("Edit")
        self.Window = QtWidgets.QMenu(self.menubar)
        self.Window.setObjectName("Window")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.New = QtWidgets.QAction(MainWindow)
        self.New.setObjectName("New")
        self.Open = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/open-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Open.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(9)
        self.Open.setFont(font)
        self.Open.setObjectName("Open")
        self.Opendir = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(9)
        self.Opendir.setFont(font)
        self.Opendir.setObjectName("Opendir")
        self.Save = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Save.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(9)
        self.Save.setFont(font)
        self.Save.setObjectName("Save")
        self.Saveas = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/saveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Saveas.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(9)
        self.Saveas.setFont(font)
        self.Saveas.setObjectName("Saveas")
        self.Undo = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/img/chexiao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Undo.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(9)
        self.Undo.setFont(font)
        self.Undo.setObjectName("Undo")
        self.Copy = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/img/fuzhi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Copy.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(9)
        self.Copy.setFont(font)
        self.Copy.setObjectName("Copy")
        self.Cut = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/img/jianqie.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Cut.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(9)
        self.Cut.setFont(font)
        self.Cut.setObjectName("Cut")
        self.Paste = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/img/niantie.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Paste.setIcon(icon6)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(9)
        self.Paste.setFont(font)
        self.Paste.setObjectName("Paste")
        self.Function = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/img/fengxian.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Function.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(9)
        self.Function.setFont(font)
        self.Function.setObjectName("Function")
        self.Find = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/img/chazhao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Find.setIcon(icon8)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        self.Find.setFont(font)
        self.Find.setObjectName("Find")
        self.Goto = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        self.Goto.setFont(font)
        self.Goto.setObjectName("Goto")
        self.Close = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/img/img/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Close.setIcon(icon9)
        self.Close.setObjectName("Close")
        self.Closeall = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/img/img/closeall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Closeall.setIcon(icon10)
        self.Closeall.setObjectName("Closeall")
        self.Exit = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/img/img/exit-full.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit.setIcon(icon11)
        self.Exit.setObjectName("Exit")
        self.Pie = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/img/img/baogao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pie.setIcon(icon12)
        self.Pie.setObjectName("Pie")
        self.Compile = QtWidgets.QAction(MainWindow)
        self.Compile.setObjectName("Compile")
        self.Run = QtWidgets.QAction(MainWindow)
        self.Run.setObjectName("Run")
        self.CMD = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/img/img/zhongduan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CMD.setIcon(icon13)
        self.CMD.setObjectName("CMD")
        self.File.addAction(self.Open)
        self.File.addAction(self.Save)
        self.File.addAction(self.Saveas)
        self.File.addSeparator()
        self.File.addAction(self.Close)
        self.File.addAction(self.Closeall)
        self.File.addAction(self.Exit)
        self.Edit.addAction(self.Undo)
        self.Edit.addAction(self.Copy)
        self.Edit.addAction(self.Cut)
        self.Edit.addAction(self.Paste)
        self.Edit.addAction(self.Goto)
        self.Window.addAction(self.Function)
        self.Window.addAction(self.Find)
        self.Window.addAction(self.Pie)
        self.Window.addAction(self.CMD)
        self.menu.addAction(self.Compile)
        self.menu.addAction(self.Run)
        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Edit.menuAction())
        self.menubar.addAction(self.Window.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "文件名"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "行数"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "名称"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "风险水平"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "解决方式"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "输出"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "终端"))
        self.treeWidget_1.headerItem().setText(0, _translate("MainWindow", "函数和变量"))
        self.treeWidget_1.headerItem().setText(1, _translate("MainWindow", "行"))
        self.treeWidget_1.headerItem().setText(2, _translate("MainWindow", "类型"))
        self.File.setTitle(_translate("MainWindow", "文件"))
        self.Edit.setTitle(_translate("MainWindow", "编辑"))
        self.Window.setTitle(_translate("MainWindow", "窗口"))
        self.menu.setTitle(_translate("MainWindow", "调试"))
        self.New.setText(_translate("MainWindow", "新建"))
        self.New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.Open.setText(_translate("MainWindow", "打开文件"))
        self.Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.Opendir.setText(_translate("MainWindow", "打开文件夹"))
        self.Opendir.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.Save.setText(_translate("MainWindow", "保存"))
        self.Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.Saveas.setText(_translate("MainWindow", "另存为"))
        self.Saveas.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.Undo.setText(_translate("MainWindow", "撤销"))
        self.Undo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.Copy.setText(_translate("MainWindow", "复制"))
        self.Copy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.Cut.setText(_translate("MainWindow", "剪切"))
        self.Cut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.Paste.setText(_translate("MainWindow", "粘贴"))
        self.Paste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.Function.setText(_translate("MainWindow", "风险函数管理"))
        self.Find.setText(_translate("MainWindow", "查找和替换"))
        self.Find.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.Goto.setText(_translate("MainWindow", "转到定义"))
        self.Close.setText(_translate("MainWindow", "关闭标签"))
        self.Closeall.setText(_translate("MainWindow", "关闭所有标签"))
        self.Exit.setText(_translate("MainWindow", "退出"))
        self.Pie.setText(_translate("MainWindow", "生成报告"))
        self.Compile.setText(_translate("MainWindow", "编译"))
        self.Run.setText(_translate("MainWindow", "运行"))
        self.CMD.setText(_translate("MainWindow", "终端"))
from ui.resource import icon_rc
