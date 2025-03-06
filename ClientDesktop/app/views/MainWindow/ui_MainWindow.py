# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(830, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(830, 400))
        MainWindow.setMaximumSize(QSize(830, 400))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: \"black\"")
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SoundsWidget = QListWidget(MainWindow)
        QListWidgetItem(self.SoundsWidget)
        QListWidgetItem(self.SoundsWidget)
        self.SoundsWidget.setObjectName(u"SoundsWidget")

        self.verticalLayout_3.addWidget(self.SoundsWidget)

        self.addPresetButton = QPushButton(MainWindow)
        self.addPresetButton.setObjectName(u"addPresetButton")

        self.verticalLayout_3.addWidget(self.addPresetButton)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ComputerKeyboardButton = QPushButton(MainWindow)
        self.ComputerKeyboardButton.setObjectName(u"ComputerKeyboardButton")

        self.verticalLayout_4.addWidget(self.ComputerKeyboardButton)

        self.channels_layout = QHBoxLayout()
        self.channels_layout.setObjectName(u"channels_layout")

        self.verticalLayout_4.addLayout(self.channels_layout)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Widget", None))

        __sortingEnabled = self.SoundsWidget.isSortingEnabled()
        self.SoundsWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.SoundsWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Test Music 1", None));
        ___qlistwidgetitem1 = self.SoundsWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Test Music 2", None));
        self.SoundsWidget.setSortingEnabled(__sortingEnabled)

        self.addPresetButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.ComputerKeyboardButton.setText(QCoreApplication.translate("MainWindow", u"Computer Keyboard", None))
    # retranslateUi

