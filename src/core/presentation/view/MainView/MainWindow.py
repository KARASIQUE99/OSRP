from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('core\\presentation\\view\\MainView\\Ui_MainWindow.ui', self)  # Load the .ui file