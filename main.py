import sys

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    with open("themes/MaterialDark.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
