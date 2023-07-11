from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet
from startWin import MainWindow

if __name__ == '__main__':

    app = QApplication([])
    app.setWindowIcon(QIcon("ui/resource/img/Audit.png"))
    window = MainWindow()
    # apply_stylesheet(app, theme='light_blue.xml', invert_secondary=True,css_file='ui/style.css')
    apply_stylesheet(app, theme='light_blue.xml', invert_secondary=True, css_file='ui/style.css')
    window.show()
    app.exec_()