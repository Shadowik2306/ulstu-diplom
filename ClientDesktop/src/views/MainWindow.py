from PySide6.QtWidgets import QMainWindow, QStatusBar, QMenuBar

from src.config import settings
from src.views.MusicWindow.MusicWindow import MusicWindow
from src.views.SingInWindow.sign_in import SignInWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        while settings.jwt_secret_key is None:
            sign_in_window = SignInWindow()
            sign_in_window.exec()

        self.setCentralWidget(MusicWindow())
        self.setWindowTitle("TINKLE APP")

        menu_bar = QMenuBar(self)
        main_menu = menu_bar.addMenu(" &Log out")
        self.setMenuBar(menu_bar)
        settings.remove_jwt()

    def log_out(self):
        settings.remove_jwt()