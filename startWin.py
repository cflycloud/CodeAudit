import os
import subprocess

from PyQt5.Qsci import QsciScintilla
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QFileSystemModel
from ui.startWidget import Ui_MainWindow
from os.path import split as split_pathname
from tools.text_area import TextArea
from find.find import FindForm
from function.function import functionForm
from config.config import Config
from analysis.analysis import Analysis
from ui.functionWidget import Ui_functionDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    new_tab = pyqtSignal()
    nothing_open = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.slot()
        self.nothing_open.emit()
        self.model = QFileSystemModel()
        # 初始化
        self.splitter_2.setSizes([20, 250, 20])
        self.splitter.setSizes([200, 10])
        self.config = Config()
        self.config_ini = self.config.read_config()

    def slot(self):
        # 槽函数
        self.new_tab.connect(self.enable_eidting)
        self.nothing_open.connect(self.disable_eidting)
        self.Open.triggered.connect(self.open_file)
        self.Save.triggered.connect(self.save_file)
        self.Saveas.triggered.connect(self.saveas_file)
        self.Close.triggered.connect(self.close_tab)
        self.Closeall.triggered.connect(self.clase_all_tab)
        self.Exit.triggered.connect(self.closeEvent)
        self.Undo.triggered.connect(self.unDo)
        self.Copy.triggered.connect(self.copy)
        self.Cut.triggered.connect(self.shearing)
        self.Paste.triggered.connect(self.paste)
        self.Function.triggered.connect(self.manage_risk)
        self.Find.triggered.connect(self.find)
        self.Pie.triggered.connect(self.report)
        self.CMD.triggered.connect(self.terminal)
        self.lineEdit.returnPressed.connect(self.execcmd)
        self.tabWidget.tabCloseRequested.connect(self.close_tab)

    def open_file(self):
        # TODO: file tree and variables
        print("open")
        self.treeWidget.clear()
        isMain = True
        self.treeWidget_1.clear()
        # self.fileCloseAll()
        # self.treeView
        fileName, isOk = QFileDialog.getOpenFileName(self, "选取文件", "./", "C(*.c)")
        path, name = split_pathname(fileName)

        if isOk:
            f = open(fileName, "r")
            text = f.read()
            f.close()
            textEdit = TextArea(name, text, path)
            textEdit.setAutoFillBackground(True)
            self.tabWidget.addTab(textEdit, textEdit.get_name())
            self.tabWidget.setCurrentWidget(textEdit)
            a = Analysis(fileName, self.config_ini)
            func = a.run()
            print(a.filelist)
            for f in a.funlist:
                print(f.filepath)
            print(a.filename)
            print(func)

            if isMain:
                self.model.setRootPath(path)
                self.model.setNameFilterDisables(False)
                self.model.setNameFilters(["*.c", "*.h"])

                self.treeView.setModel(self.model)
                self.treeView.setColumnHidden(1, True)
                self.treeView.setColumnHidden(2, True)
                self.treeView.setColumnHidden(3, True)
                self.treeView.setRootIndex(self.model.index(path))
            self.new_tab.emit()

    def save_file(self):
        textEdit = self.tabWidget.currentWidget()
        if textEdit is None or not isinstance(textEdit, QsciScintilla):
            return True
        try:
            print(textEdit.get_name())
            filename = textEdit.get_path() + '/' + textEdit.get_name()
            f = open(filename, "w")
            f.write(textEdit.text().replace("\r", ''))
            f.close()
            textEdit.modified = False
            return True
        except EnvironmentError as e:
            print(e)
            return False

    def saveas_file(self):
        textEdit = self.tabWidget.currentWidget()
        if textEdit is None or not isinstance(textEdit, QsciScintilla):
            return True
        filename, isOk = QFileDialog.getSaveFileName(self, "另存为", textEdit.get_name(), "C(*.c)")
        if isOk:
            f = open(filename, "w")
            f.write(textEdit.text().replace("\r", ''))
            f.close()
            textEdit.modified = False
            return True

    def close_tab(self):
        textEdit = self.tabWidget.currentWidget()
        if textEdit is None or not isinstance(textEdit, QsciScintilla):
            return
        if textEdit.modified is False:
            self.tabWidget.removeTab(self.tabWidget.currentIndex())
        else:
            result = QMessageBox.question(self,
                                               "Text Editor - Unsaved Changes",
                                               "Save unsaved changes in {0}?".format(textEdit.get_name()),
                                               QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if result == QMessageBox.Yes:
                try:
                    self.save_file()
                except EnvironmentError as e:
                    QMessageBox.warning(self,
                                        "Text Editor -- Save Error",
                                        "Failed to save {0}: {1}".format(textEdit.get_name(), e))
                self.tabWidget.removeTab(self.tabWidget.currentIndex())
            elif result == QMessageBox.No:
                self.tabWidget.removeTab(self.tabWidget.currentIndex())

        if self.tabWidget.count() == 0:
            self.nothing_open.emit()

    def clase_all_tab(self):
        failures = []
        for i in range(self.tabWidget.count()):
            self.close_tab()
        if (failures and QMessageBox.warning(self, "Text Editor -- Save Error",
                                             "Failed to save{0}\nQuit anyway?".format("\n\t".join(failures)),
                                             QMessageBox.Yes | QMessageBox.No) == QMessageBox.No):
            return False
        return True

    # overwrite
    def closeEvent(self, event) -> None:
        if (self.clase_all_tab() is False) or self.is_open_something():
            event.ignore()
            return
        else:
            self.close()

    def is_open_something(self):
        return self.tabWidget.count() > 0

    def unDo(self):
        if self.is_open_something():
            self.tabWidget.currentWidget().undo()

    def copy(self):
        if self.is_open_something():
            self.tabWidget.currentWidget().copy()

    def shearing(self):
        if self.is_open_something():
            self.tabWidget.currentWidget().cut()

    def paste(self):
        if self.is_open_something():
            self.tabWidget.currentWidget().paste()

    def manage_risk(self):
        self.funcwi = functionForm(self)
        self.funcwi.show()

    def find(self):
        self.findwi = FindForm(self)
        self.findwi.show()

    def report(self):
        # TODO: report
        print("report")

    def terminal(self):
        subprocess.Popen(["cmd",'/c','cmd'],creationflags =subprocess.CREATE_NEW_CONSOLE)

    def disable_eidting(self):
        self.Save.setEnabled(False)
        self.Saveas.setEnabled(False)
        self.Close.setEnabled(False)
        self.Closeall.setEnabled(False)
        self.Compile.setEnabled(False)
        self.Run.setEnabled(False)
        self.Pie.setEnabled(False)
        for i in self.Edit.actions():
            i.setEnabled(False)
        self.Find.setEnabled(False)

    def enable_eidting(self):
        self.Save.setEnabled(True)
        self.Saveas.setEnabled(True)
        self.Close.setEnabled(True)
        self.Closeall.setEnabled(True)
        self.Compile.setEnabled(True)
        self.Run.setEnabled(True)
        self.Pie.setEnabled(True)
        for i in self.Edit.actions():
            i.setEnabled(True)
        self.Find.setEnabled(True)

    def execcmd(self):
        # TODO: line edite
        print("run")
        self.tabWidget_2.setCurrentIndex(1)
        cmd = self.lineEdit.text().strip('\r')
        cmd = cmd.strip('\n')
        self.textEdit_2.append(cmd)
        env = os.environ
        print(cmd)
        p = subprocess.Popen(["cmd", '/c', "{:s}".format(cmd)], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             cwd=".")
        (stdout, stderr) = p.communicate()
        print(stdout.decode("gbk"))
        self.textEdit_2.append(stdout.decode("gbk"))
        self.textEdit_2.append(stderr.decode("gbk"))