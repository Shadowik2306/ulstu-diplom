from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow, QStatusBar, QMenuBar

from src.config import settings
from src.views.MusicWindow.MusicWindow import MusicWindow
from src.views.SingInWindow.sign_in import SignInWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("TINKLE APP")
        self.setCentralWidget(MusicWindow())

        log_out = QtGui.QAction('Log out', self)  # this displays on my system
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&System')
        fileMenu.addAction(log_out)
        log_out.triggered.connect(self.log_out)

        if not settings.jwt_secret_key:
            self.log_out()


    def log_out(self):
        settings.remove_jwt()

        sign_in_window = SignInWindow()
        sign_in_window.exec()

        if not settings.jwt_secret_key:
            self.close()
            return

        self.setCentralWidget(MusicWindow())