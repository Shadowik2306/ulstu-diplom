# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MidiChannelWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MidiChannelWidget(object):
    def setupUi(self, DeviceWidget):
        if not DeviceWidget.objectName():
            DeviceWidget.setObjectName(u"DeviceWidget")
        DeviceWidget.setEnabled(True)
        DeviceWidget.resize(270, 364)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DeviceWidget.sizePolicy().hasHeightForWidth())
        DeviceWidget.setSizePolicy(sizePolicy)
        DeviceWidget.setMinimumSize(QSize(270, 360))
        DeviceWidget.setMaximumSize(QSize(360, 16777215))
        DeviceWidget.setAutoFillBackground(False)
        DeviceWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(DeviceWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.border = QFrame(DeviceWidget)
        self.border.setObjectName(u"border")
        self.border.setStyleSheet(u"background-color: rgb(125, 128, 128)")
        self.border.setFrameShape(QFrame.Shape.StyledPanel)
        self.border.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.border)
#ifndef Q_OS_MAC
        self.horizontalLayout_2.setSpacing(-1)
#endif
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalFrame = QFrame(self.border)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.WidgetNameLabel = QLabel(self.verticalFrame)
        self.WidgetNameLabel.setObjectName(u"WidgetNameLabel")
        self.WidgetNameLabel.setMaximumSize(QSize(16777215, 19))
        self.WidgetNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.WidgetNameLabel)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PresetNameLabel = QLabel(self.verticalFrame)
        self.PresetNameLabel.setObjectName(u"PresetNameLabel")

        self.horizontalLayout.addWidget(self.PresetNameLabel)

        self.RemovePresetButton = QPushButton(self.verticalFrame)
        self.RemovePresetButton.setObjectName(u"RemovePresetButton")

        self.horizontalLayout.addWidget(self.RemovePresetButton)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.verticalFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_4.addWidget(self.label_2)

        self.DevicesBox = QComboBox(self.verticalFrame)
        self.DevicesBox.addItem("")
        self.DevicesBox.addItem("")
        self.DevicesBox.setObjectName(u"DevicesBox")

        self.verticalLayout_4.addWidget(self.DevicesBox)

        self.comboBox = QComboBox(self.verticalFrame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_4.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.verticalFrame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.VolumeSlider = QSlider(self.verticalFrame)
        self.VolumeSlider.setObjectName(u"VolumeSlider")
        self.VolumeSlider.setMaximum(100)
        self.VolumeSlider.setValue(70)
        self.VolumeSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_6.addWidget(self.VolumeSlider)


        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.MuteButton = QPushButton(self.verticalFrame)
        self.MuteButton.setObjectName(u"MuteButton")

        self.verticalLayout_5.addWidget(self.MuteButton)

        self.EnableButton = QPushButton(self.verticalFrame)
        self.EnableButton.setObjectName(u"EnableButton")

        self.verticalLayout_5.addWidget(self.EnableButton)

        self.pushButton = QPushButton(self.verticalFrame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 5)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 2)

        self.horizontalLayout_2.addWidget(self.verticalFrame)


        self.verticalLayout.addWidget(self.border)


        self.retranslateUi(DeviceWidget)

        QMetaObject.connectSlotsByName(DeviceWidget)
    # setupUi

    def retranslateUi(self, DeviceWidget):
        DeviceWidget.setWindowTitle(QCoreApplication.translate("DeviceWidget", u"Widget", None))
        self.WidgetNameLabel.setText(QCoreApplication.translate("DeviceWidget", u"InputName", None))
        self.PresetNameLabel.setText(QCoreApplication.translate("DeviceWidget", u"PresetName", None))
        self.RemovePresetButton.setText(QCoreApplication.translate("DeviceWidget", u"X", None))
        self.label_2.setText(QCoreApplication.translate("DeviceWidget", u"MIDI From", None))
        self.DevicesBox.setItemText(0, QCoreApplication.translate("DeviceWidget", u"No Device", None))
        self.DevicesBox.setItemText(1, QCoreApplication.translate("DeviceWidget", u"Computer Keyboard", None))

        self.DevicesBox.setPlaceholderText(QCoreApplication.translate("DeviceWidget", u"Devices", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("DeviceWidget", u"All Channels", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("DeviceWidget", u"Ch 1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("DeviceWidget", u"Ch 2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("DeviceWidget", u"Ch 3", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("DeviceWidget", u"Channels", None))
        self.label_3.setText(QCoreApplication.translate("DeviceWidget", u"Volume", None))
        self.MuteButton.setText(QCoreApplication.translate("DeviceWidget", u"Mute", None))
        self.EnableButton.setText(QCoreApplication.translate("DeviceWidget", u"Enable", None))
        self.pushButton.setText(QCoreApplication.translate("DeviceWidget", u"Note OFF disabled", None))
    # retranslateUi

