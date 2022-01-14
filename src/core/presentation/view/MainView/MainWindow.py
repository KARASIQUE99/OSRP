from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('core\\presentation\\view\\MainView\\Ui_MainWindow.ui', self)  # Load the .ui file

        #self.statusBar().showMessage('Ready')

        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.setStatusTip('Exit application')
        self.exit_action.triggered.connect(self.close)

