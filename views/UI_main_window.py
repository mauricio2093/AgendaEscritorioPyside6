# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)


class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 523)
        MainWindow.setStyleSheet(u"QWidget{\n" "border-radius:12px;""}")
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralWidget_frame = QFrame(MainWindow)
        self.centralWidget_frame.setObjectName(u"centralWidget_frame")
        self.centralWidget_frame.setStyleSheet(u"")
        self.centralWidget_frame.setFrameShape(QFrame.StyledPanel)
        self.centralWidget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.centralWidget_frame)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.centralWidget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"QFrame {\n"
"            background-color: rgb(0, 0, 0);\n"
"}")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setMinimumSize(QSize(0, 30))
        self.content_frame.setCursor(QCursor(Qt.ArrowCursor))
        self.content_frame.setMouseTracking(True)
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_frame)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 10)
        self.top_bar_frame = QFrame(self.content_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setMinimumSize(QSize(0, 80))
        self.top_bar_frame.setMaximumSize(QSize(16777215, 80))
        self.top_bar_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 5px;\n"
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
        self.horizontalSpacer_3 = QSpacerItem(1000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.frame_5.setStyleSheet(u"QFrame{\n"
"       background-color: rgb(85, 0, 255);\n"
"       border-radius: 20;\n"
"       image: url(./assets/icons/discord.svg);\n"
"       padding: 3px;"
"}")
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


        self.verticalLayout_4.addWidget(self.top_bar_frame)

        self.action_bar_frame = QFrame(self.content_frame)
        self.action_bar_frame.setObjectName(u"action_bar_frame")
        self.action_bar_frame.setMinimumSize(QSize(0, 39))
        self.action_bar_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"}")
        self.action_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.action_bar_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.new_recipi_button = QPushButton(self.action_bar_frame)
        self.new_recipi_button.setObjectName(u"new_recipi_button")
        self.new_recipi_button.setMinimumSize(QSize(150, 30))
        self.new_recipi_button.setFont(font2)
        self.new_recipi_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_recipi_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(250, 250, 250);\n"
"	background-color: rgb(255, 17, 80);\n"
"	padding: 1px;\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton::hover{background-color: rgb(255, 103, 0)};")
        icon6 = QIcon()
        icon6.addFile(u"./assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_recipi_button.setIcon(icon6)
        self.new_recipi_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.new_recipi_button)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label_4 = QLabel(self.action_bar_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(30, 30))
        self.label_4.setMaximumSize(QSize(30, 16777215))
        self.label_4.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border: 3px solid rgb(85, 0, 255);\n"
"border-right: 3px solid rgb(53, 53, 53);\n"
"border-bottom-right-radius : 0px;\n"
"border-top-right-radius : 0px;\n"
"color: rgb(194, 194, 194)")
        self.label_4.setPixmap(QPixmap(u"./assets/icons/buscar.svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_4.setMargin(0)
        self.label_4.setIndent(0)

        self.horizontalLayout.addWidget(self.label_4)

        self.search_lineEdit = QLineEdit(self.action_bar_frame)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setMinimumSize(QSize(0, 30))
        self.search_lineEdit.setMaximumSize(QSize(500, 16777215))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        self.search_lineEdit.setFont(font3)
        self.search_lineEdit.setAutoFillBackground(False)
        self.search_lineEdit.setStyleSheet(u"QLineEdit{\n"
"       background-color: rgb(53, 53, 53);\n"
"       border: 3px solid rgb(85, 0, 255);\n"
"       border-left: 3px solid  rgb(53, 53, 53);\n"
"       border-radius: 12px;\n"
"       border-bottom-left-radius : 0px;"
"       border-top-left-radius : 0px;"
"       text-align: left;\n"
"       padding-left: 10px;\n"
"       color: rgb(194, 194, 194)\n"
"}")
        self.search_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.search_lineEdit)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.action_bar_frame)

        self.container_table = QFrame(self.content_frame)
        self.container_table.setObjectName(u"container_table")
        self.container_table.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(220, 220, 220);\n"
"}")
        self.container_table.setFrameShape(QFrame.StyledPanel)
        self.container_table.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.container_table)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tableWidget = QTableWidget(self.container_table)
        self.tableWidget.setObjectName(u"tableWidget")
        palette = QPalette()
        brush = QBrush(QColor(220, 220, 220, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(13, 9, 36, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))# modified
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(227, 227, 227, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(160, 160, 160, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(43, 6, 77, 255))#modified header
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush6 = QBrush(QColor(105, 105, 105, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(255, 17, 80, 255))#modificado señalizacion
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        brush8 = QBrush(QColor(220, 220, 225, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        brush10 = QBrush(QColor(43, 6, 77, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush10)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush11)
        brush12 = QBrush(QColor(255, 255, 220, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush12)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        brush13 = QBrush(QColor(255, 17, 80, 255)) #modified
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        brush14 = QBrush(QColor(43, 6, 77, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        brush15 = QBrush(QColor(220, 220, 220, 255)) #modified
        brush15.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush15)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush12)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush11)
        brush16 = QBrush(QColor(0, 0, 0, 128)) 
        brush16.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        brush17 = QBrush(QColor(247, 247, 247, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush17)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush14)
        brush18 = QBrush(QColor(0, 0, 0, 255))
        brush18.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush18)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush16)
#endif
        self.tableWidget.setPalette(palette)
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(False)
        self.tableWidget.setFont(font4)
        
        self.tableWidget.setAlternatingRowColors(True)
        
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"       color: rgb(220, 220, 220);\n"
"	border-radius: 12px;\n"
"}"
"       QScrollBar:vertical {\n"    
"       border: 1px solid rgb(73, 73, 73);\n"
"       box-shadow: inset 0 0 1rem rgba(255, 255, 255, 0.3);\n"
"       background= rgb(53,53,53);\n"
"       width: 20px;\n"
"       margin: 22px 0 22px 0;\n"

"}"
"       QScrollBar::handle:vertical {\n"
"       background: rgb(73, 73, 73);\n"
"       min-height: 5px;\n"
"       border: 1px solid rgb(85, 0, 255);\n"
"}"
"       QScrollBar::add-line:vertical {\n"
"       border: 1px solid rgb(73, 73, 73);\n"
"       background: rgb(53, 53, 53);\n"
"       height: 20px;\n"
"       subcontrol-position: bottom;\n"
"       subcontrol-origin: margin;\n"
"}"

"       QScrollBar::sub-line:vertical {\n"
"       border: 1px solid rgb(73, 73, 73);\n"
"       background: rgb(53,53,53);\n"
"       height: 20px;\n"
"       subcontrol-position: top;\n"
"       subcontrol-origin: margin;\n"
"}"
"       QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"       width: 3px;\n"
"       height: 3px;\n"
"       background: rgb(85, 0, 255);\n"
"}"

"       QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"       background: none;\n"
"}")

        self.horizontalLayout_9.addWidget(self.tableWidget)

        self.verticalLayout_3.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.centralWidget_frame)
        

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.pushMin_Button.setText("")
        self.pushMax_Button.setText("")
        self.pushClose_Button.setText("")
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Bienvenido a Mauricio Studios.", None))
        self.slogan_label.setText(QCoreApplication.translate("MainWindow", u"Creando proyectos. @Python.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Percepci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Progreso ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Datos", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.new_recipi_button.setText(QCoreApplication.translate("MainWindow", u"Nuevos Datos", None))
        self.label_4.setText("")
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar datos ...", None))
    # retranslateUi

