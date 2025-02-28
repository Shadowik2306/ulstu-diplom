# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DeviceWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SignUp(object):
    def setupUi(self, SignUp):
        if not SignUp.objectName():
            SignUp.setObjectName(u"SignUp")
        SignUp.setEnabled(True)
        SignUp.resize(480, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SignUp.sizePolicy().hasHeightForWidth())
        SignUp.setSizePolicy(sizePolicy)
        SignUp.setMinimumSize(QSize(480, 650))
        SignUp.setMaximumSize(QSize(480, 650))
        SignUp.setAutoFillBackground(False)
        SignUp.setStyleSheet(u"background-color: \"black\"")
        self.verticalLayout = QVBoxLayout(SignUp)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.DataLayout = QVBoxLayout()
        self.DataLayout.setObjectName(u"DataLayout")
        self.DataLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.SignUpLabel = QLabel(SignUp)
        self.SignUpLabel.setObjectName(u"SignUpLabel")
        self.SignUpLabel.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamilies([u"Charter"])
        font.setPointSize(64)
        font.setBold(True)
        self.SignUpLabel.setFont(font)
        self.SignUpLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.DataLayout.addWidget(self.SignUpLabel)


        self.verticalLayout.addLayout(self.DataLayout)

        self.verticalSpacer = QSpacerItem(20, 62, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.FormLayout = QVBoxLayout()
        self.FormLayout.setObjectName(u"FormLayout")
        self.FormLayout.setContentsMargins(0, -1, -1, -1)
        self.InputLayout = QVBoxLayout()
        self.InputLayout.setSpacing(6)
        self.InputLayout.setObjectName(u"InputLayout")
        self.InputLayout.setContentsMargins(50, -1, 50, -1)
        self.EmailLabel = QLabel(SignUp)
        self.EmailLabel.setObjectName(u"EmailLabel")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.EmailLabel.setFont(font1)

        self.InputLayout.addWidget(self.EmailLabel)

        self.EmailLineEdit = QLineEdit(SignUp)
        self.EmailLineEdit.setObjectName(u"EmailLineEdit")
        self.EmailLineEdit.setAutoFillBackground(False)
        self.EmailLineEdit.setStyleSheet(u"background-color: 'white'; \n"
"color: black;\n"
"border-radius: 5px;")

        self.InputLayout.addWidget(self.EmailLineEdit)

        self.LoginLabel = QLabel(SignUp)
        self.LoginLabel.setObjectName(u"LoginLabel")
        self.LoginLabel.setFont(font1)

        self.InputLayout.addWidget(self.LoginLabel)

        self.LoginLineEdit = QLineEdit(SignUp)
        self.LoginLineEdit.setObjectName(u"LoginLineEdit")
        self.LoginLineEdit.setAutoFillBackground(False)
        self.LoginLineEdit.setStyleSheet(u"background-color: 'white'; \n"
"color: black;\n"
"border-radius: 5px;")

        self.InputLayout.addWidget(self.LoginLineEdit)

        self.PasswordLabel = QLabel(SignUp)
        self.PasswordLabel.setObjectName(u"PasswordLabel")
        self.PasswordLabel.setFont(font1)

        self.InputLayout.addWidget(self.PasswordLabel)

        self.PasswordLineEdit = QLineEdit(SignUp)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")
        self.PasswordLineEdit.setAutoFillBackground(False)
        self.PasswordLineEdit.setStyleSheet(u"background-color: 'white'; \n"
"color: black;\n"
"border-radius: 5px;")

        self.InputLayout.addWidget(self.PasswordLineEdit)

        self.RepeatPasswordLabel = QLabel(SignUp)
        self.RepeatPasswordLabel.setObjectName(u"RepeatPasswordLabel")
        self.RepeatPasswordLabel.setFont(font1)

        self.InputLayout.addWidget(self.RepeatPasswordLabel)

        self.RepeatPasswordLineEdit = QLineEdit(SignUp)
        self.RepeatPasswordLineEdit.setObjectName(u"RepeatPasswordLineEdit")
        self.RepeatPasswordLineEdit.setAutoFillBackground(False)
        self.RepeatPasswordLineEdit.setStyleSheet(u"background-color: 'white'; \n"
"color: black;\n"
"border-radius: 5px;")

        self.InputLayout.addWidget(self.RepeatPasswordLineEdit)

        self.PasswordProblemsLabel = QLabel(SignUp)
        self.PasswordProblemsLabel.setObjectName(u"PasswordProblemsLabel")
        self.PasswordProblemsLabel.setStyleSheet(u"color: orange")
        self.PasswordProblemsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.InputLayout.addWidget(self.PasswordProblemsLabel)


        self.FormLayout.addLayout(self.InputLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.FormLayout.addItem(self.verticalSpacer_2)

        self.ButtonLayout = QVBoxLayout()
        self.ButtonLayout.setObjectName(u"ButtonLayout")
        self.ButtonLayout.setContentsMargins(0, -1, -1, -1)
        self.SignUpButton = QPushButton(SignUp)
        self.SignUpButton.setObjectName(u"SignUpButton")
        self.SignUpButton.setStyleSheet(u"background-color: \"#1A1A2E\"")
        self.SignUpButton.setAutoDefault(False)

        self.ButtonLayout.addWidget(self.SignUpButton)

        self.ErorrsLabel = QLabel(SignUp)
        self.ErorrsLabel.setObjectName(u"ErorrsLabel")
        self.ErorrsLabel.setMaximumSize(QSize(16777215, 10))
        self.ErorrsLabel.setStyleSheet(u"color: red")
        self.ErorrsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ButtonLayout.addWidget(self.ErorrsLabel)


        self.FormLayout.addLayout(self.ButtonLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.FormLayout.addItem(self.verticalSpacer_3)

        self.ExtraLayout = QVBoxLayout()
        self.ExtraLayout.setObjectName(u"ExtraLayout")
        self.AlreadyHaveAccountLabel = QLabel(SignUp)
        self.AlreadyHaveAccountLabel.setObjectName(u"AlreadyHaveAccountLabel")
        self.AlreadyHaveAccountLabel.setMaximumSize(QSize(16777215, 20))
        self.AlreadyHaveAccountLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ExtraLayout.addWidget(self.AlreadyHaveAccountLabel)

        self.SignInHyperLabel = QLabel(SignUp)
        self.SignInHyperLabel.setObjectName(u"SignInHyperLabel")
        self.SignInHyperLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.SignInHyperLabel.setOpenExternalLinks(True)
        self.SignInHyperLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.ExtraLayout.addWidget(self.SignInHyperLabel)


        self.FormLayout.addLayout(self.ExtraLayout)

        self.FormLayout.setStretch(0, 8)
        self.FormLayout.setStretch(2, 2)
        self.FormLayout.setStretch(4, 1)

        self.verticalLayout.addLayout(self.FormLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 3)

        self.retranslateUi(SignUp)

        QMetaObject.connectSlotsByName(SignUp)
    # setupUi

    def retranslateUi(self, SignUp):
        SignUp.setWindowTitle(QCoreApplication.translate("SignUp", u"Widget", None))
        self.SignUpLabel.setText(QCoreApplication.translate("SignUp", u"Sign Up", None))
        self.EmailLabel.setText(QCoreApplication.translate("SignUp", u"Email", None))
        self.LoginLabel.setText(QCoreApplication.translate("SignUp", u"Login", None))
        self.PasswordLabel.setText(QCoreApplication.translate("SignUp", u"Password", None))
        self.RepeatPasswordLabel.setText(QCoreApplication.translate("SignUp", u"Repeat Password", None))
        self.PasswordProblemsLabel.setText(QCoreApplication.translate("SignUp", u"PasswordProblems", None))
        self.SignUpButton.setText(QCoreApplication.translate("SignUp", u"Sign Up", None))
        self.ErorrsLabel.setText(QCoreApplication.translate("SignUp", u"ErrorLabel", None))
        self.AlreadyHaveAccountLabel.setText(QCoreApplication.translate("SignUp", u"Already have an account?", None))
        self.SignInHyperLabel.setText(QCoreApplication.translate("SignUp", u"Sign In", None))
    # retranslateUi

