import sys
from PySide6.QtWidgets import QApplication, QWidget

from ui_SignUp import Ui_SignUp


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SignUp()
        self.ui.setupUi(self)
        self.setWindowTitle("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
