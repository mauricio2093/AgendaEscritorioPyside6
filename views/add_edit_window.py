# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_edit_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class AddEditWindow(object):
        def setupUi(self, AddEditWindow):
                if not AddEditWindow.objectName():
                        AddEditWindow.setObjectName(u"AddEditWindow")
                AddEditWindow.resize(1023, 550)
                AddEditWindow.setStyleSheet(u"border-radius:12px;")
                self.horizontalLayout = QHBoxLayout(AddEditWindow)
                self.horizontalLayout.setSpacing(0)
                self.horizontalLayout.setObjectName(u"horizontalLayout")
                self.horizontalLayout.setContentsMargins(0, 9, 0, 0)
                self.central_widget_frame = QFrame(AddEditWindow)
                self.central_widget_frame.setObjectName(u"central_widget_frame")
                self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
                self.central_widget_frame.setFrameShadow(QFrame.Raised)
                self.shadow_layout = QVBoxLayout(self.central_widget_frame)
                self.shadow_layout.setSpacing(0)
                self.shadow_layout.setObjectName(u"shadow_layout")
                self.shadow_layout.setContentsMargins(10, 10, 10, 10)
                self.background_frame = QFrame(self.central_widget_frame)
                self.background_frame.setObjectName(u"background_frame")
                self.background_frame.setStyleSheet(u"background-color: rgb(20,20,20);")
                self.background_frame.setFrameShape(QFrame.StyledPanel)
                self.background_frame.setFrameShadow(QFrame.Raised)
                self.verticalLayout_2 = QVBoxLayout(self.background_frame)
                self.verticalLayout_2.setObjectName(u"verticalLayout_2")
                self.top_bar_frame = QFrame(self.background_frame)
                self.top_bar_frame.setObjectName(u"top_bar_frame")
                self.top_bar_frame.setMinimumSize(QSize(0, 80))
                self.top_bar_frame.setMaximumSize(QSize(16777215, 80))
                self.top_bar_frame.setStyleSheet(u"QFrame {\n"
        "	background-color: rgb(13, 9, 36);\n"
        "	border-radius: 12px;\n"
"}")
                self.top_bar_frame.setFrameShape(QFrame.NoFrame)
                self.top_bar_frame.setFrameShadow(QFrame.Raised)
                self.verticalLayout_5 = QVBoxLayout(self.top_bar_frame)
                self.verticalLayout_5.setSpacing(0)
                self.verticalLayout_5.setObjectName(u"verticalLayout_5")
                self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
                self.titleBar = QFrame(self.top_bar_frame)
                self.titleBar.setObjectName(u"titleBar")
                self.titleBar.setMaximumSize(QSize(16777215, 30))
                self.titleBar.setStyleSheet(u"background-color: rgb(13, 9, 36);")
                self.titleBar.setFrameShape(QFrame.NoFrame)
                self.titleBar.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_7 = QHBoxLayout(self.titleBar)
                self.horizontalLayout_7.setSpacing(0)
                self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
                self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
                self.horizontalSpacer_3 = QSpacerItem(500, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

                self.actionButtonsBar = QFrame(self.titleBar)
                self.actionButtonsBar.setObjectName(u"actionButtonsBar")
                self.actionButtonsBar.setMinimumSize(QSize(100, 0))
                self.actionButtonsBar.setMaximumSize(QSize(100, 16777215))
                self.actionButtonsBar.setStyleSheet(u"")
                self.actionButtonsBar.setFrameShape(QFrame.StyledPanel)
                self.actionButtonsBar.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_8 = QHBoxLayout(self.actionButtonsBar)
                self.horizontalLayout_8.setSpacing(0)
                self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
                self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
                self.pushMin_Button = QPushButton(self.actionButtonsBar)
                self.pushMin_Button.setObjectName(u"pushMin_Button")
                self.pushMin_Button.setMinimumSize(QSize(30, 30))
                self.pushMin_Button.setMaximumSize(QSize(30, 30))
                self.pushMin_Button.setCursor(QCursor(Qt.PointingHandCursor))
                self.pushMin_Button.setStyleSheet(u"QPushButton {\n"
        "	border: none;\n"
        "	background-color: rgb(13, 9, 36);\n"
        "	border-radius: 15;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(124, 124, 124);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
                icon = QIcon()
                icon.addFile(u"./assets/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.pushMin_Button.setIcon(icon)
                self.pushMin_Button.setIconSize(QSize(17, 17))

                self.horizontalLayout_8.addWidget(self.pushMin_Button)

                self.pushMax_Button = QPushButton(self.actionButtonsBar)
                self.pushMax_Button.setObjectName(u"pushMax_Button")
                self.pushMax_Button.setMinimumSize(QSize(30, 30))
                self.pushMax_Button.setMaximumSize(QSize(30, 30))
                self.pushMax_Button.setCursor(QCursor(Qt.PointingHandCursor))
                self.pushMax_Button.setStyleSheet(u"QPushButton {\n"
        "	border: none;\n"
        "	background-color: rgb(13, 9, 36);\n"
        "	border-radius: 15;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(124, 124, 124);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
                icon1 = QIcon()
                icon1.addFile(u"./assets/icons/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.pushMax_Button.setIcon(icon1)
                self.pushMax_Button.setIconSize(QSize(17, 17))

                self.horizontalLayout_8.addWidget(self.pushMax_Button)

                self.pushClose_Button = QPushButton(self.actionButtonsBar)
                self.pushClose_Button.setObjectName(u"pushClose_Button")
                self.pushClose_Button.setMinimumSize(QSize(30, 30))
                self.pushClose_Button.setMaximumSize(QSize(30, 30))
                self.pushClose_Button.setCursor(QCursor(Qt.PointingHandCursor))
                self.pushClose_Button.setStyleSheet(u"QPushButton {\n"
        "	border: none;\n"
        "	background-color: rgb(13, 9, 36);\n"
        "	border-radius: 15;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(124, 124, 124);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0) ;\n"
"}")
                icon2 = QIcon()
                icon2.addFile(u"./assets/icons/close.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.pushClose_Button.setIcon(icon2)
                self.pushClose_Button.setIconSize(QSize(17, 17))

                self.horizontalLayout_8.addWidget(self.pushClose_Button)


                self.horizontalLayout_7.addWidget(self.actionButtonsBar)


                self.verticalLayout_5.addWidget(self.titleBar)

                self.actionBar = QFrame(self.top_bar_frame)
                self.actionBar.setObjectName(u"actionBar")
                self.actionBar.setStyleSheet(u"QFrame {\n"
        "	background-color: rgb(13, 9, 36);\n"
"}\n"
"\n"
"QSpacer {\n"
"	background-color: rgb(13, 9, 36);\n"
"}")
                self.actionBar.setFrameShape(QFrame.NoFrame)
                self.actionBar.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_2 = QHBoxLayout(self.actionBar)
                self.horizontalLayout_2.setSpacing(0)
                self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.frame_6 = QFrame(self.actionBar)
                self.frame_6.setObjectName(u"frame_6")
                self.frame_6.setMinimumSize(QSize(250, 0))
                self.frame_6.setMaximumSize(QSize(250, 16777215))
                self.frame_6.setStyleSheet(u"background-color: rgb(13, 9, 36);")
                self.frame_6.setFrameShape(QFrame.NoFrame)
                self.frame_6.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
                self.horizontalLayout_4.setSpacing(5)
                self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
                self.horizontalLayout_4.setContentsMargins(5, 0, 5, 15)
                self.frame_5 = QFrame(self.frame_6)
                self.frame_5.setObjectName(u"frame_5")
                self.frame_5.setMinimumSize(QSize(40, 40))
                self.frame_5.setMaximumSize(QSize(40, 40))
                self.frame_5.setStyleSheet(u"background-color: rgb(85, 0, 255);\n"
"border-radius: 20;\n"
"image: url(./assets/icons/discord.svg);\n"
"padding: 3px;")
                self.frame_5.setFrameShape(QFrame.NoFrame)
                self.frame_5.setFrameShadow(QFrame.Raised)

                self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignVCenter)

                self.frame_9 = QFrame(self.frame_6)
                self.frame_9.setObjectName(u"frame_9")
                self.frame_9.setMinimumSize(QSize(200, 0))
                self.frame_9.setMaximumSize(QSize(200, 16777215))
                self.frame_9.setStyleSheet(u"background-color: rgb(13, 9, 36);")
                self.frame_9.setFrameShape(QFrame.NoFrame)
                self.frame_9.setFrameShadow(QFrame.Raised)
                self.verticalLayout_8 = QVBoxLayout(self.frame_9)
                self.verticalLayout_8.setSpacing(0)
                self.verticalLayout_8.setObjectName(u"verticalLayout_8")
                self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
                self.name_label = QLabel(self.frame_9)
                self.name_label.setObjectName(u"name_label")
                font = QFont()
                font.setPointSize(10)
                font.setBold(True)
                self.name_label.setFont(font)
                self.name_label.setStyleSheet(u"color: rgb(168, 168, 168);")

                self.verticalLayout_8.addWidget(self.name_label)

                self.slogan_label = QLabel(self.frame_9)
                self.slogan_label.setObjectName(u"slogan_label")
                font1 = QFont()
                font1.setPointSize(8)
                font1.setBold(True)
                self.slogan_label.setFont(font1)
                self.slogan_label.setStyleSheet(u"color: rgb(134, 134, 134);")

                self.verticalLayout_8.addWidget(self.slogan_label)


                self.horizontalLayout_4.addWidget(self.frame_9, 0, Qt.AlignVCenter)


                self.horizontalLayout_2.addWidget(self.frame_6, 0, Qt.AlignTop)

                self.horizontalSpacer = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.horizontalLayout_2.addItem(self.horizontalSpacer)

                self.nav_bar_frame = QFrame(self.actionBar)
                self.nav_bar_frame.setObjectName(u"nav_bar_frame")
                self.nav_bar_frame.setMinimumSize(QSize(250, 0))
                self.nav_bar_frame.setMaximumSize(QSize(250, 16777215))
                self.nav_bar_frame.setCursor(QCursor(Qt.PointingHandCursor))
                self.nav_bar_frame.setStyleSheet(u"background-color: rgb(13, 9, 36);")
                self.nav_bar_frame.setFrameShape(QFrame.NoFrame)
                self.nav_bar_frame.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_3 = QHBoxLayout(self.nav_bar_frame)
                self.horizontalLayout_3.setSpacing(0)
                self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
                self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
                self.label = QLabel(self.nav_bar_frame)
                self.label.setObjectName(u"label")
                self.label.setEnabled(True)
                font2 = QFont()
                font2.setPointSize(11)
                font2.setBold(True)
                self.label.setFont(font2)
                self.label.setCursor(QCursor(Qt.PointingHandCursor))
                self.label.setMouseTracking(True)
                self.label.setFocusPolicy(Qt.NoFocus)
                self.label.setStyleSheet(u"QLabel {\n"
        "	color: rgb(220, 220, 220);\n"
        "	cursor: pointer;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: rgb(255, 103, 0);\n"
"}")

                self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignVCenter)

                self.label_2 = QLabel(self.nav_bar_frame)
                self.label_2.setObjectName(u"label_2")
                self.label_2.setFont(font2)
                self.label_2.setCursor(QCursor(Qt.PointingHandCursor))
                self.label_2.setStyleSheet(u"QLabel {\n"
        "	color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: rgb(255, 103, 0);\n"
"}")

                self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignRight)

                self.label_3 = QLabel(self.nav_bar_frame)
                self.label_3.setObjectName(u"label_3")
                self.label_3.setFont(font2)
                self.label_3.setCursor(QCursor(Qt.PointingHandCursor))
                self.label_3.setStyleSheet(u"QLabel {\n"
        "	color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: rgb(255, 103, 0);\n"
"}")

                self.horizontalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter)


                self.horizontalLayout_2.addWidget(self.nav_bar_frame)

                self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

                self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

                self.actionItems = QFrame(self.actionBar)
                self.actionItems.setObjectName(u"actionItems")
                self.actionItems.setMinimumSize(QSize(120, 0))
                self.actionItems.setMaximumSize(QSize(120, 16777215))
                self.actionItems.setStyleSheet(u"background-color: rgb(13, 9, 36);")
                self.actionItems.setFrameShape(QFrame.NoFrame)
                self.actionItems.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_6 = QHBoxLayout(self.actionItems)
                self.horizontalLayout_6.setSpacing(5)
                self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
                self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
                self.pushButton = QPushButton(self.actionItems)
                self.pushButton.setObjectName(u"pushButton")
                self.pushButton.setMinimumSize(QSize(36, 36))
                self.pushButton.setMaximumSize(QSize(36, 36))
                self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
                self.pushButton.setStyleSheet(u"QPushButton {\n"
        "	border: none;\n"
        "	background-color: rgb(13, 9, 36);\n"
        "	border-radius: 18;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
                icon3 = QIcon()
                icon3.addFile(u"./assets/icons/chart.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.pushButton.setIcon(icon3)
                self.pushButton.setIconSize(QSize(20, 20))

                self.horizontalLayout_6.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

                self.pushButton_2 = QPushButton(self.actionItems)
                self.pushButton_2.setObjectName(u"pushButton_2")
                self.pushButton_2.setMinimumSize(QSize(36, 36))
                self.pushButton_2.setMaximumSize(QSize(36, 36))
                self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
                self.pushButton_2.setStyleSheet(u"QPushButton {\n"
        "	border: none;\n"
        "	background-color: rgb(13, 9, 36);\n"
        "	border-radius: 18;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
                icon4 = QIcon()
                icon4.addFile(u"./assets/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.pushButton_2.setIcon(icon4)
                self.pushButton_2.setIconSize(QSize(20, 20))

                self.horizontalLayout_6.addWidget(self.pushButton_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

                self.pushButton_3 = QPushButton(self.actionItems)
                self.pushButton_3.setObjectName(u"pushButton_3")
                self.pushButton_3.setMinimumSize(QSize(36, 36))
                self.pushButton_3.setMaximumSize(QSize(36, 36))
                self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
                self.pushButton_3.setStyleSheet(u"QPushButton {\n"
        "	border: none;\n"
        "	background-color: rgb(13, 9, 36);\n"
        "	border-radius: 18;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
                icon5 = QIcon()
                icon5.addFile(u"./assets/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.pushButton_3.setIcon(icon5)
                self.pushButton_3.setIconSize(QSize(20, 20))

                self.horizontalLayout_6.addWidget(self.pushButton_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


                self.horizontalLayout_2.addWidget(self.actionItems)


                self.verticalLayout_5.addWidget(self.actionBar)


                self.verticalLayout_2.addWidget(self.top_bar_frame)

                self.content_frame = QFrame(self.background_frame)
                self.content_frame.setObjectName(u"content_frame")
                self.content_frame.setStyleSheet(u"QFrame{\n"
        "	background-color: rgb(13, 9, 36);\n"
        "	border-radius: 12px;\n"
"}")
                self.content_frame.setFrameShape(QFrame.StyledPanel)
                self.content_frame.setFrameShadow(QFrame.Raised)
                self.label_4 = QLabel(self.content_frame)
                self.label_4.setObjectName(u"label_4")
                self.label_4.setGeometry(QRect(20, 0, 61, 16))
                self.label_4.setFont(font2)
                self.label_4.setStyleSheet(u"QLabel{\n"
        "	color: rgb(220,220,220);\n"
"}")
                self.title_line_edit = QLineEdit(self.content_frame)
                self.title_line_edit.setObjectName(u"title_line_edit")
                self.title_line_edit.setGeometry(QRect(10, 20, 291, 30))
                self.title_line_edit.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"border: 3px solid rgb(85, 0, 255);\n"
"border-radius: 25;;\n"
"color: rgb(194, 194, 194)\n"
"")
                self.label_5 = QLabel(self.content_frame)
                self.label_5.setObjectName(u"label_5")
                self.label_5.setGeometry(QRect(10, 56, 91, 20))
                self.label_5.setFont(font2)
                self.label_5.setStyleSheet(u"QLabel{\n"
        "	color: rgb(220,220,220);\n"
"}")
                self.category_comboBox = QComboBox(self.content_frame)
                self.category_comboBox.setObjectName(u"category_comboBox")
                self.category_comboBox.setGeometry(QRect(10, 80, 291, 31))
                self.category_comboBox.setCursor(QCursor(Qt.PointingHandCursor))
                self.category_comboBox.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"border: 3px solid rgb(85, 0, 255);\n"
"border-radius: 5px;\n"
"pading:10px;"
"cursor: pointer;"
"color: rgb(194, 194, 194);")
                self.label_6 = QLabel(self.content_frame)
                self.label_6.setObjectName(u"label_6")
                self.label_6.setGeometry(QRect(10, 120, 131, 16))
                self.label_6.setFont(font2)
                self.label_6.setStyleSheet(u"QLabel{\n"
        "	color: rgb(220,220,220);\n"
"}")
                self.url_line_edit = QLineEdit(self.content_frame)
                self.url_line_edit.setObjectName(u"url_line_edit")
                self.url_line_edit.setGeometry(QRect(10, 140, 291, 30))
                self.url_line_edit.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"border: 3px solid rgb(85, 0, 255);\n"
"border-radius: 25;;\n"
"color: rgb(194, 194, 194)\n"
"")
                self.label_7 = QLabel(self.content_frame)
                self.label_7.setObjectName(u"label_7")
                self.label_7.setGeometry(QRect(10, 180, 101, 16))
                self.label_7.setFont(font2)
                self.label_7.setStyleSheet(u"QLabel{\n"
        "	color: rgb(220,220,220);\n"
"}")
                self.budget_line_edit = QLineEdit(self.content_frame)
                self.budget_line_edit.setObjectName(u"budget_line_edit")
                self.budget_line_edit.setGeometry(QRect(10, 200, 291, 30))
                self.budget_line_edit.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"border: 3px solid rgb(85, 0, 255);\n"
"border-radius: 25;;\n"
"color: rgb(194, 194, 194)\n"
"")
                self.label_8 = QLabel(self.content_frame)
                self.label_8.setObjectName(u"label_8")
                self.label_8.setGeometry(QRect(10, 240, 171, 16))
                self.label_8.setFont(font2)
                self.label_8.setStyleSheet(u"QLabel{\n"
"	color: rgb(220,220,220);\n"
"}")
                self.image_path_line_edit = QLineEdit(self.content_frame)
                self.image_path_line_edit.setObjectName(u"image_path_line_edit")
                self.image_path_line_edit.setGeometry(QRect(10, 260, 221, 30))
                self.image_path_line_edit.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"border: 3px solid rgb(85, 0, 255);\n"
"border-radius: 25;;\n"
"color: rgb(194, 194, 194)\n"
"")
                self.select_img = QToolButton(self.content_frame)
                self.select_img.setObjectName(u"select_img")
                self.select_img.setGeometry(QRect(250, 260, 31, 31))
                self.select_img.setCursor(QCursor(Qt.PointingHandCursor))
                self.select_img.setStyleSheet(u"border-left: 0.5px solid rgb(73, 73, 73);\n"
"border-right: 1.5px solid rgb(53, 53, 53);\n"
"border-top: 0.5px solid rgb(73, 73, 73);\n"
"border-bottom: 1.5px solid rgb(53, 53, 53);\n"
"border-radius: 2.5px;")
                icon6 = QIcon()
                icon6.addFile(u"./assets/icons/open-file.png", QSize(), QIcon.Normal, QIcon.Off)
                self.select_img.setIcon(icon6)
                self.select_img.setIconSize(QSize(50, 50))
                self.add_edit_button = QPushButton(self.content_frame)
                self.add_edit_button.setObjectName(u"add_edit_button")
                self.add_edit_button.setGeometry(QRect(50, 320, 221, 31))
                self.add_edit_button.setFont(font2)
                self.add_edit_button.setCursor(QCursor(Qt.PointingHandCursor))
                self.add_edit_button.setStyleSheet(u"QPushButton{\n"
        "	color: rgb(250, 250, 250);\n"
        "	background-color: rgb(7, 255, 119);;\n"
        "	padding: 1px;\n"
        "	border-radius: 8px;\n"
"}\n"
"QPushButton::hover{background-color: rgb(0, 170, 0) };")
                icon7 = QIcon()
                icon7.addFile(u"./assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
                self.add_edit_button.setIcon(icon7)
                self.add_edit_button.setIconSize(QSize(20, 20))
                self.cancel_button = QPushButton(self.content_frame)
                self.cancel_button.setObjectName(u"cancel_button")
                self.cancel_button.setGeometry(QRect(50, 360, 221, 31))
                self.cancel_button.setFont(font2)
                self.cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
                self.cancel_button.setStyleSheet(u"QPushButton{\n"
        "	color: rgb(250, 250, 250);\n"
        "	background-color: rgb(85, 0, 255);\n"
        "	padding: 1px;\n"
        "	border-radius: 8px;\n"
"}\n"
"QPushButton::hover{background-color: rgb(255, 103, 0) };")
                icon8 = QIcon()
                icon8.addFile(u"./assets/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
                self.cancel_button.setIcon(icon8)
                self.cancel_button.setIconSize(QSize(20, 20))
                self.label_9 = QLabel(self.content_frame)
                self.label_9.setObjectName(u"label_9")
                self.label_9.setGeometry(QRect(320, 0, 121, 16))
                self.label_9.setFont(font2)
                self.label_9.setStyleSheet(u"QLabel{\n"
        "	color: rgb(220,220,220);\n"
"}")
                self.ingredients_text_edit = QPlainTextEdit(self.content_frame)
                self.ingredients_text_edit.setObjectName(u"ingredients_text_edit")
                self.ingredients_text_edit.setGeometry(QRect(320, 30, 311, 371))
                self.ingredients_text_edit.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"border: 3px solid rgb(85, 0, 255);\n"
"border-radius: 25;;\n"
"color: rgb(194, 194, 194);\n"
"padding:10px;\n"
"")
                self.direction_text_edit = QPlainTextEdit(self.content_frame)
                self.direction_text_edit.setObjectName(u"direction_text_edit")
                self.direction_text_edit.setGeometry(QRect(650, 30, 311, 371))
                self.direction_text_edit.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"border: 3px solid rgb(85, 0, 255);\n"
"border-radius: 25;;\n"
"color: rgb(194, 194, 194);\n"
"padding:10px;\n"
"")
                self.label_10 = QLabel(self.content_frame)
                self.label_10.setObjectName(u"label_10")
                self.label_10.setGeometry(QRect(650, 0, 121, 16))
                self.label_10.setFont(font2)
                self.label_10.setStyleSheet(u"QLabel{\n"
"	        color: rgb(220,220,220);\n"
"}")

                self.verticalLayout_2.addWidget(self.content_frame)


                self.shadow_layout.addWidget(self.background_frame)


                self.horizontalLayout.addWidget(self.central_widget_frame)


                self.retranslateUi(AddEditWindow)

                QMetaObject.connectSlotsByName(AddEditWindow)
    # setupUi

        def retranslateUi(self, AddEditWindow):
                AddEditWindow.setWindowTitle(QCoreApplication.translate("AddEditWindow", u"Form", None))
                self.pushMin_Button.setText("")
                self.pushMax_Button.setText("")
                self.pushClose_Button.setText("")
                self.name_label.setText(QCoreApplication.translate("AddEditWindow", u"Bienvenido a Mauricio Studios.", None))
                self.slogan_label.setText(QCoreApplication.translate("AddEditWindow", u"Creando proyectos. @Python.", None))
                self.label.setText(QCoreApplication.translate("AddEditWindow", u"Percepci\u00f3n", None))
                self.label_2.setText(QCoreApplication.translate("AddEditWindow", u"Progreso ", None))
                self.label_3.setText(QCoreApplication.translate("AddEditWindow", u"Datos", None))
                self.pushButton.setText("")
                self.pushButton_2.setText("")
                self.pushButton_3.setText("")
                self.label_4.setText(QCoreApplication.translate("AddEditWindow", u"Titulo", None))
                self.label_5.setText(QCoreApplication.translate("AddEditWindow", u"Categor\u00eda", None))
                self.category_comboBox.setPlaceholderText(QCoreApplication.translate("AddEditWindow", u"Selecciona una categor\u00eda ...", None))
                self.label_6.setText(QCoreApplication.translate("AddEditWindow", u"URL de una Gu\u00eda", None))
                self.label_7.setText(QCoreApplication.translate("AddEditWindow", u"Presupuesto", None))
                self.label_8.setText(QCoreApplication.translate("AddEditWindow", u"Seleccione una imagen", None))
                self.select_img.setText(QCoreApplication.translate("AddEditWindow", u"...", None))
                self.add_edit_button.setText(QCoreApplication.translate("AddEditWindow", u"Agregar", None))
                self.cancel_button.setText(QCoreApplication.translate("AddEditWindow", u"Cancelar", None))
                self.label_9.setText(QCoreApplication.translate("AddEditWindow", u"Comentarios", None))
                self.label_10.setText(QCoreApplication.translate("AddEditWindow", u"Pasos de realizaci\u00f3n", None))
        # retranslateUi

