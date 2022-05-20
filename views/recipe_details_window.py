# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_details_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)


class DetailWidget(object):
    def setupUi(self, DetailWidget):
        if not DetailWidget.objectName():
            DetailWidget.setObjectName(u"DetailWidget")
        DetailWidget.resize(909, 488)
        DetailWidget.setStyleSheet(u"border-radius: 12px;")
        self.verticalLayout = QVBoxLayout(DetailWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(DetailWidget)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(10, 10, 10);")
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
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 150))
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 12px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.recipe_pic_label = QLabel(self.frame)
        self.recipe_pic_label.setObjectName(u"recipe_pic_label")
        self.recipe_pic_label.setMaximumSize(QSize(170, 170))
        self.recipe_pic_label.setStyleSheet(u"border: 1px solid rgb(34, 24, 97);")

        self.horizontalLayout.addWidget(self.recipe_pic_label)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	border: 1px solid rgb(34, 24, 97);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.recipe_title_label = QLabel(self.frame_3)
        self.recipe_title_label.setObjectName(u"recipe_title_label")
        self.recipe_title_label.setGeometry(QRect(60, 10, 541, 21))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.recipe_title_label.setFont(font3)
        self.recipe_title_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(220, 220, 220);\n"
"	border: 1px solid rgb(13, 9, 36);\n"
"}")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 50, 81, 21))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	color: rgb(220, 220, 220);\n"
"    border: 1px solid rgb(13, 9, 36);\n"
"}")
        self.recipe_category_label = QLabel(self.frame_3)
        self.recipe_category_label.setObjectName(u"recipe_category_label")
        self.recipe_category_label.setGeometry(QRect(190, 50, 221, 21))
        self.recipe_category_label.setFont(font2)
        self.recipe_category_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(220, 220, 220);\n"
"	border: 1px solid rgb(13, 9, 36);\n"
"}")
        self.recipe_url_label = QLabel(self.frame_3)
        self.recipe_url_label.setObjectName(u"recipe_url_label")
        self.recipe_url_label.setGeometry(QRect(190, 80, 241, 21))
        self.recipe_url_label.setFont(font2)
        self.recipe_url_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(220, 220, 220);\n"
"	border: 1px solid rgb(13, 9, 36);\n"
"}")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 80, 81, 21))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"QLabel {\n"
"	color: rgb(220, 220, 220);\n"
"	border: 1px solid rgb(13, 9, 36);\n"
"}")
        self.recipe_budget_label = QLabel(self.frame_3)
        self.recipe_budget_label.setObjectName(u"recipe_budget_label")
        self.recipe_budget_label.setGeometry(QRect(190, 106, 251, 20))
        self.recipe_budget_label.setFont(font2)
        self.recipe_budget_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(220, 220, 220);\n"
"	border: 1px solid rgb(13, 9, 36);\n"
"}")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 106, 101, 20))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"QLabel {\n"
"	color: rgb(220, 220, 220);\n"
"	border: 1px solid rgb(13, 9, 36);\n"
"}")

        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.content_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 12px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.recipe_title_label_2 = QLabel(self.frame_2)
        self.recipe_title_label_2.setObjectName(u"recipe_title_label_2")
        self.recipe_title_label_2.setFont(font3)
        self.recipe_title_label_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(220, 220, 220);\n"
"}")
        self.recipe_title_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.recipe_title_label_2)

        self.ingredient_TextEdit = QPlainTextEdit(self.frame_2)
        self.ingredient_TextEdit.setObjectName(u"ingredient_TextEdit")
        self.ingredient_TextEdit.setStyleSheet(u"border: 1px solid rgb(34, 24, 97);\n"
"color: rgb(220,220,220);")

        self.verticalLayout_4.addWidget(self.ingredient_TextEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.recipe_title_label_3 = QLabel(self.frame_2)
        self.recipe_title_label_3.setObjectName(u"recipe_title_label_3")
        self.recipe_title_label_3.setFont(font3)
        self.recipe_title_label_3.setStyleSheet(u"QLabel {\n"
"	color: rgb(220, 220, 220);\n"
"}")
        self.recipe_title_label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.recipe_title_label_3)

        self.direction_TextEdit = QPlainTextEdit(self.frame_2)
        self.direction_TextEdit.setObjectName(u"direction_TextEdit")
        self.direction_TextEdit.setStyleSheet(u"border: 1px solid rgb(34, 24, 97);\n"
"color: rgb(220, 220, 220);")

        self.verticalLayout_6.addWidget(self.direction_TextEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(DetailWidget)

        QMetaObject.connectSlotsByName(DetailWidget)
    # setupUi

    def retranslateUi(self, DetailWidget):
        DetailWidget.setWindowTitle(QCoreApplication.translate("DetailWidget", u"Form", None))
        self.pushMin_Button.setText("")
        self.pushMax_Button.setText("")
        self.pushClose_Button.setText("")
        self.name_label.setText(QCoreApplication.translate("DetailWidget", u"Bienvenido a Mauricio Studios.", None))
        self.slogan_label.setText(QCoreApplication.translate("DetailWidget", u"Creando proyectos. @Python.", None))
        self.label.setText(QCoreApplication.translate("DetailWidget", u"Percepci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("DetailWidget", u"Progreso ", None))
        self.label_3.setText(QCoreApplication.translate("DetailWidget", u"Datos", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.recipe_pic_label.setText("")
        self.recipe_title_label.setText(QCoreApplication.translate("DetailWidget", u"Titulo", None))
        self.label_4.setText(QCoreApplication.translate("DetailWidget", u"Categoria :", None))
        self.recipe_category_label.setText(QCoreApplication.translate("DetailWidget", u"Categoria", None))
        self.recipe_url_label.setText(QCoreApplication.translate("DetailWidget", u"URL", None))
        self.label_5.setText(QCoreApplication.translate("DetailWidget", u"URL :", None))
        self.recipe_budget_label.setText(QCoreApplication.translate("DetailWidget", u"Presupuesto", None))
        self.label_6.setText(QCoreApplication.translate("DetailWidget", u"Presupuesto :", None))
        self.recipe_title_label_2.setText(QCoreApplication.translate("DetailWidget", u"Comentarios", None))
        self.recipe_title_label_3.setText(QCoreApplication.translate("DetailWidget", u"Proceso de realizaci\u00f3n", None))
    # retranslateUi

