import sys

import requests
from PySide6.QtWidgets import QApplication, QWidget, QDialog

from src.config import settings
from src.views.SingInWindow.ui_SignIn import Ui_SignIn


class SignInWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SignIn()
        self.ui.setupUi(self)
        self.setWindowTitle("")

        self.ui.ErorrsLabel.setText("")
        self.res = ""
        self.ui.SignUpButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        response = requests.post(
            settings.server_url + "/auth/sing_in",
            json={
                "email": self.ui.EmailOrLoginLineEdit.text(),
                "password": self.ui.PasswordLineEdit.text()
            },
        )

        if response.status_code != 200:
            self.ui.ErorrsLabel.setText(f"Error: {response.status_code}")

        res = response.json()
        settings.set_jwt(res['access_token'])
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.show()
    sys.exit(app.exec())