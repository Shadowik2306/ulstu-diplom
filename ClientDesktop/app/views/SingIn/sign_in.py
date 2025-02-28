import sys
from PySide6.QtWidgets import QApplication, QWidget

from app.views.SingIn.ui_SignIn import Ui_SignIn


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SignIn()
        self.ui.setupUi(self)
        self.setWindowTitle("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
