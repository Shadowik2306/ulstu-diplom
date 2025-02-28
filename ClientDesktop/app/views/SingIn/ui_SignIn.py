# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SignIn.ui'
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

class Ui_SignIn(object):
    def setupUi(self, SignIn):
        if not SignIn.objectName():
            SignIn.setObjectName(u"SignIn")
        SignIn.setEnabled(True)
        SignIn.resize(480, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SignIn.sizePolicy().hasHeightForWidth())
        SignIn.setSizePolicy(sizePolicy)
        SignIn.setMinimumSize(QSize(480, 650))
        SignIn.setMaximumSize(QSize(480, 650))
        SignIn.setAutoFillBackground(False)
        SignIn.setStyleSheet(u"background-color: \"black\"")
        self.verticalLayout = QVBoxLayout(SignIn)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.DataLayout = QVBoxLayout()
        self.DataLayout.setObjectName(u"DataLayout")
        self.DataLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.SignUpLabel = QLabel(SignIn)
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
        self.EmailOrLoginLabel = QLabel(SignIn)
        self.EmailOrLoginLabel.setObjectName(u"EmailOrLoginLabel")
        self.EmailOrLoginLabel.setMaximumSize(QSize(16777215, 25))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.EmailOrLoginLabel.setFont(font1)

        self.InputLayout.addWidget(self.EmailOrLoginLabel)

        self.EmailOrLoginLineEdit = QLineEdit(SignIn)
        self.EmailOrLoginLineEdit.setObjectName(u"EmailOrLoginLineEdit")
        self.EmailOrLoginLineEdit.setAutoFillBackground(False)
        self.EmailOrLoginLineEdit.setStyleSheet(u"background-color: 'white'; \n"
"color: black;\n"
"border-radius: 5px;")

        self.InputLayout.addWidget(self.EmailOrLoginLineEdit)

        self.PasswordLabel = QLabel(SignIn)
        self.PasswordLabel.setObjectName(u"PasswordLabel")
        self.PasswordLabel.setMaximumSize(QSize(16777215, 25))
        self.PasswordLabel.setFont(font1)

        self.InputLayout.addWidget(self.PasswordLabel)

        self.PasswordLineEdit = QLineEdit(SignIn)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")
        self.PasswordLineEdit.setAutoFillBackground(False)
        self.PasswordLineEdit.setStyleSheet(u"background-color: 'white'; \n"
"color: black;\n"
"border-radius: 5px;")

        self.InputLayout.addWidget(self.PasswordLineEdit)


        self.FormLayout.addLayout(self.InputLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.FormLayout.addItem(self.verticalSpacer_2)

        self.ButtonLayout = QVBoxLayout()
        self.ButtonLayout.setObjectName(u"ButtonLayout")
        self.ButtonLayout.setContentsMargins(0, -1, -1, -1)
        self.SignUpButton = QPushButton(SignIn)
        self.SignUpButton.setObjectName(u"SignUpButton")
        self.SignUpButton.setStyleSheet(u"background-color: \"#1A1A2E\"")
        self.SignUpButton.setAutoDefault(False)

        self.ButtonLayout.addWidget(self.SignUpButton)

        self.ErorrsLabel = QLabel(SignIn)
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
        self.DontHaveAccountLabel = QLabel(SignIn)
        self.DontHaveAccountLabel.setObjectName(u"DontHaveAccountLabel")
        self.DontHaveAccountLabel.setMaximumSize(QSize(16777215, 20))
        self.DontHaveAccountLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ExtraLayout.addWidget(self.DontHaveAccountLabel)

        self.SignUpHyperLabel = QLabel(SignIn)
        self.SignUpHyperLabel.setObjectName(u"SignUpHyperLabel")
        self.SignUpHyperLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.SignUpHyperLabel.setOpenExternalLinks(True)
        self.SignUpHyperLabel.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.ExtraLayout.addWidget(self.SignUpHyperLabel)


        self.FormLayout.addLayout(self.ExtraLayout)

        self.FormLayout.setStretch(0, 8)
        self.FormLayout.setStretch(2, 2)
        self.FormLayout.setStretch(4, 1)

        self.verticalLayout.addLayout(self.FormLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 3)

        self.retranslateUi(SignIn)

        QMetaObject.connectSlotsByName(SignIn)
    # setupUi

    def retranslateUi(self, SignIn):
        SignIn.setWindowTitle(QCoreApplication.translate("SignIn", u"Widget", None))
        self.SignUpLabel.setText(QCoreApplication.translate("SignIn", u"Sign In", None))
        self.EmailOrLoginLabel.setText(QCoreApplication.translate("SignIn", u"Email or Login", None))
        self.PasswordLabel.setText(QCoreApplication.translate("SignIn", u"Password", None))
        self.SignUpButton.setText(QCoreApplication.translate("SignIn", u"Sign In", None))
        self.ErorrsLabel.setText(QCoreApplication.translate("SignIn", u"ErrorLabel", None))
        self.DontHaveAccountLabel.setText(QCoreApplication.translate("SignIn", u"Don't have an account?", None))
        self.SignUpHyperLabel.setText(QCoreApplication.translate("SignIn", u"SignUp", None))
    # retranslateUi

