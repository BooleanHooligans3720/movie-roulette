# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from modules import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-position: centered;\n"
"       background-image: url(:/images/images/images/SpinWheel.png);\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-tags.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"\n"
"background-image: url(:/icons/images/icons/cil-magnifying-glass.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        #self.toggleLeftBox = QPushButton(self.bottomMenu)
        #self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        #sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        #self.toggleLeftBox.setSizePolicy(sizePolicy)
        #self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        #self.toggleLeftBox.setFont(font)
        #self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        #self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        #self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        #self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        #self.extraLeftBox = QFrame(self.bgApp)
        #self.extraLeftBox.setObjectName(u"extraLeftBox")
        #self.extraLeftBox.setMinimumSize(QSize(0, 0))
        #self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        #self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        #self.extraLeftBox.setFrameShadow(QFrame.Raised)
        #self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        #self.extraColumLayout.setSpacing(0)
        #self.extraColumLayout.setObjectName(u"extraColumLayout")
        #self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        #self.extraTopBg = QFrame(self.extraLeftBox)
        #self.extraTopBg.setObjectName(u"extraTopBg")
        #self.extraTopBg.setMinimumSize(QSize(0, 50))
        #self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        #self.extraTopBg.setFrameShape(QFrame.NoFrame)
        #self.extraTopBg.setFrameShadow(QFrame.Raised)
        #self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        #self.verticalLayout_5.setSpacing(0)
        #self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        #self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        #self.extraTopLayout = QGridLayout()
        #self.extraTopLayout.setObjectName(u"extraTopLayout")
        #self.extraTopLayout.setHorizontalSpacing(10)
        #self.extraTopLayout.setVerticalSpacing(0)
        #self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        #self.extraIcon = QFrame(self.extraTopBg)
        #self.extraIcon.setObjectName(u"extraIcon")
        #self.extraIcon.setMinimumSize(QSize(20, 0))
        #self.extraIcon.setMaximumSize(QSize(20, 20))
        #self.extraIcon.setFrameShape(QFrame.NoFrame)
        #self.extraIcon.setFrameShadow(QFrame.Raised)

        #self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        #self.extraLabel = QLabel(self.extraTopBg)
        #self.extraLabel.setObjectName(u"extraLabel")
        #self.extraLabel.setMinimumSize(QSize(150, 0))

        #self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        #self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        #self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        #self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        #self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        #self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        #self.extraCloseColumnBtn.setIcon(icon)
        #self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        #self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


#        self.verticalLayout_5.addLayout(self.extraTopLayout)


 #       self.extraColumLayout.addWidget(self.extraTopBg)

  #      self.extraContent = QFrame(self.extraLeftBox)
  #      self.extraContent.setObjectName(u"extraContent")
   #     self.extraContent.setFrameShape(QFrame.NoFrame)
    #    self.extraContent.setFrameShadow(QFrame.Raised)
     #   self.verticalLayout_12 = QVBoxLayout(self.extraContent)
      #  self.verticalLayout_12.setSpacing(0)
       # self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        #self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        #self.extraTopMenu = QFrame(self.extraContent)
        #self.extraTopMenu.setObjectName(u"extraTopMenu")
        #self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        #self.extraTopMenu.setFrameShadow(QFrame.Raised)
        #self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        #self.verticalLayout_11.setSpacing(0)
        #self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        #self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        #self.btn_share = QPushButton(self.extraTopMenu)
        #self.btn_share.setObjectName(u"btn_share")
        #sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        #self.btn_share.setSizePolicy(sizePolicy)
        #self.btn_share.setMinimumSize(QSize(0, 45))
        #self.btn_share.setFont(font)
        #self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        #self.btn_share.setLayoutDirection(Qt.LeftToRight)
        #self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        #self.verticalLayout_11.addWidget(self.btn_share)

        #self.btn_adjustments = QPushButton(self.extraTopMenu)
        #self.btn_adjustments.setObjectName(u"btn_adjustments")
        #sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        #self.btn_adjustments.setSizePolicy(sizePolicy)
        #self.btn_adjustments.setMinimumSize(QSize(0, 45))
        #self.btn_adjustments.setFont(font)
        #self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        #self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        #self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        #self.verticalLayout_11.addWidget(self.btn_adjustments)

        #self.btn_more = QPushButton(self.extraTopMenu)
        #self.btn_more.setObjectName(u"btn_more")
        #sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        #self.btn_more.setSizePolicy(sizePolicy)
        #self.btn_more.setMinimumSize(QSize(0, 45))
        #self.btn_more.setFont(font)
        #self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        #self.btn_more.setLayoutDirection(Qt.LeftToRight)
        #self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        #self.verticalLayout_11.addWidget(self.btn_more)


        #self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        #self.extraCenter = QFrame(self.extraContent)
        #self.extraCenter.setObjectName(u"extraCenter")
        #self.extraCenter.setFrameShape(QFrame.NoFrame)
        #self.extraCenter.setFrameShadow(QFrame.Raised)
        #self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        #self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        #self.textEdit = QTextEdit(self.extraCenter)
        #self.textEdit.setObjectName(u"textEdit")
        #self.textEdit.setMinimumSize(QSize(222, 0))
        #self.textEdit.setStyleSheet(u"background: transparent;")
        #self.textEdit.setFrameShape(QFrame.NoFrame)
        #self.textEdit.setReadOnly(True)

        #self.verticalLayout_10.addWidget(self.textEdit)


        #self.verticalLayout_12.addWidget(self.extraCenter)

        #self.extraBottom = QFrame(self.extraContent)
        #self.extraBottom.setObjectName(u"extraBottom")
        #self.extraBottom.setFrameShape(QFrame.NoFrame)
        #self.extraBottom.setFrameShadow(QFrame.Raised)

        #self.verticalLayout_12.addWidget(self.extraBottom)


        #self.extraColumLayout.addWidget(self.extraContent)


        #self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        #self.settingsTopBtn = QPushButton(self.rightButtons)
        #self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        #self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        #self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        #self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        #icon1 = QIcon()
        #icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        #self.settingsTopBtn.setIcon(icon1)
        #self.settingsTopBtn.setIconSize(QSize(20, 20))

 #       self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setLayoutDirection(Qt.LeftToRight)
        self.home.setAutoFillBackground(False)
        self.home.setStyleSheet(u"")
        self.btn_spin = QPushButton(self.home)
        self.btn_spin.setObjectName(u"btn_spin")
        self.btn_spin.setEnabled(True)
        self.btn_spin.setGeometry(QRect(210, 10, 760, 585))
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_spin.sizePolicy().hasHeightForWidth())
        self.btn_spin.setSizePolicy(sizePolicy3)
        self.btn_spin.setMinimumSize(QSize(760, 585))
        self.btn_spin.setMaximumSize(QSize(760, 585))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(36)
        font3.setBold(True)
        font3.setItalic(False)
        self.btn_spin.setFont(font3)
        self.btn_spin.setAutoFillBackground(False)
        self.btn_spin.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);\n"
"font: 700 36pt \"Segoe UI\";\n"
"background-image: url(:/images/images/images/SpinWheel.gif);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"\n"
"")
        
        self.stackedWidget.addWidget(self.home)
        self.LoadingScreen = QWidget()
        self.LoadingScreen.setObjectName(u"LoadingScreen")
        self.LoadingScreen.setEnabled(True)
        self.ClearListSure = QPushButton(self.LoadingScreen)
        self.ClearListSure.setObjectName(u"ClearListSure")
        self.ClearListSure.setGeometry(QRect(350, 180, 491, 241))
        self.ClearListSure.setAutoFillBackground(False)
        self.ClearListSure.setStyleSheet(u"font: 700 15pt \"Consolas\";\n"
"border-color: rgb(36, 40, 47);\n"
"background-color: rgb(36, 40, 47);\n"
"\n"
"")



        self.stackedWidget.addWidget(self.LoadingScreen)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        sizePolicy3.setHeightForWidth(self.row_1.sizePolicy().hasHeightForWidth())
        self.row_1.setSizePolicy(sizePolicy3)
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.Filters = QLabel(self.frame_title_wid_1)
        self.Filters.setObjectName(u"Filters")
        self.Filters.setMinimumSize(QSize(1100, 25))
        self.Filters.setMaximumSize(QSize(16777215, 25))
        font4 = QFont()
        font4.setFamilies([u"Consolas"])
        font4.setPointSize(24)
        font4.setBold(True)
        font4.setItalic(False)
        self.Filters.setFont(font4)
        self.Filters.setStyleSheet(u"font: 700 24pt \"Consolas\";")
        self.Filters.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.Filters)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_content_wid_1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 1141, 61))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Genre_2 = QLabel(self.layoutWidget)
        self.Genre_2.setObjectName(u"Genre_2")
        self.Genre_2.setStyleSheet(u"font: 700 20pt \"Consolas\";")
        self.Genre_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.Genre_2)

        self.Popularity = QLabel(self.layoutWidget)
        self.Popularity.setObjectName(u"Popularity")
        self.Popularity.setStyleSheet(u"font: 700 20pt \"Consolas\";")
        self.Popularity.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.Popularity)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.row_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(780, 60, 171, 31))
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setStyleSheet(u"font: 700 20pt \"Consolas\";")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.layoutWidget1 = QWidget(self.row_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(720, 97, 291, 48))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_8, 0, 1, 1, 1)

        self.horizontalSlider_3 = QSlider(self.layoutWidget1)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider_3, 1, 0, 1, 1)

        self.horizontalSlider_4 = QSlider(self.layoutWidget1)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider_4, 1, 1, 1, 1)

        self.label_9 = QLabel(self.row_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(720, 160, 291, 31))
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setStyleSheet(u"font: 700 20pt \"Consolas\";")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.layoutWidget_2 = QWidget(self.row_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(720, 210, 291, 48))
        self.gridLayout_4 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_11 = QLabel(self.layoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_11, 0, 1, 1, 1)

        self.horizontalSlider_5 = QSlider(self.layoutWidget_2)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalSlider_5, 1, 0, 1, 1)

        self.horizontalSlider_6 = QSlider(self.layoutWidget_2)
        self.horizontalSlider_6.setObjectName(u"horizontalSlider_6")
        self.horizontalSlider_6.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalSlider_6, 1, 1, 1, 1)

        self.layoutWidget2 = QWidget(self.row_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(171, -1, 331, 251))
        self.gridLayout = QGridLayout(self.layoutWidget2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Action = QCheckBox(self.layoutWidget2)
        self.Action.setObjectName(u"Action")
        sizePolicy3.setHeightForWidth(self.Action.sizePolicy().hasHeightForWidth())
        self.Action.setSizePolicy(sizePolicy3)
        self.Action.setMinimumSize(QSize(150, 0))
        self.Action.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Action, 0, 0, 1, 1)

        self.Adventure = QCheckBox(self.layoutWidget2)
        self.Adventure.setObjectName(u"Adventure")
        sizePolicy3.setHeightForWidth(self.Adventure.sizePolicy().hasHeightForWidth())
        self.Adventure.setSizePolicy(sizePolicy3)
        self.Adventure.setMinimumSize(QSize(150, 0))
        self.Adventure.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Adventure, 0, 1, 1, 1)

        self.Animation = QCheckBox(self.layoutWidget2)
        self.Animation.setObjectName(u"Animation")
        self.Animation.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Animation, 1, 0, 1, 1)

        self.Comedy = QCheckBox(self.layoutWidget2)
        self.Comedy.setObjectName(u"Comedy")
        self.Comedy.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Comedy, 1, 1, 1, 1)

        self.Crime = QCheckBox(self.layoutWidget2)
        self.Crime.setObjectName(u"Crime")
        self.Crime.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Crime, 2, 0, 1, 1)

        self.Documentary = QCheckBox(self.layoutWidget2)
        self.Documentary.setObjectName(u"Documentary")
        self.Documentary.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Documentary, 2, 1, 1, 1)

        self.Drama = QCheckBox(self.layoutWidget2)
        self.Drama.setObjectName(u"Drama")
        self.Drama.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Drama, 3, 0, 1, 1)

        self.Family = QCheckBox(self.layoutWidget2)
        self.Family.setObjectName(u"Family")
        self.Family.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Family, 3, 1, 1, 1)

        self.Fantasy = QCheckBox(self.layoutWidget2)
        self.Fantasy.setObjectName(u"Fantasy")
        self.Fantasy.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Fantasy, 4, 0, 1, 1)

        self.History = QCheckBox(self.layoutWidget2)
        self.History.setObjectName(u"History")
        self.History.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.History, 4, 1, 1, 1)

        self.Horror = QCheckBox(self.layoutWidget2)
        self.Horror.setObjectName(u"Horror")
        self.Horror.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Horror, 5, 0, 1, 1)

        self.Music = QCheckBox(self.layoutWidget2)
        self.Music.setObjectName(u"Music")
        self.Music.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Music, 5, 1, 1, 1)

        self.Mystery = QCheckBox(self.layoutWidget2)
        self.Mystery.setObjectName(u"Mystery")
        self.Mystery.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Mystery, 6, 0, 1, 1)

        self.Romance = QCheckBox(self.layoutWidget2)
        self.Romance.setObjectName(u"Romance")
        self.Romance.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Romance, 6, 1, 1, 1)

        self.SciFi = QCheckBox(self.layoutWidget2)
        self.SciFi.setObjectName(u"SciFi")
        self.SciFi.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.SciFi, 7, 0, 1, 1)

        self.Thriller = QCheckBox(self.layoutWidget2)
        self.Thriller.setObjectName(u"Thriller")
        self.Thriller.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Thriller, 7, 1, 1, 1)

        self.War = QCheckBox(self.layoutWidget2)
        self.War.setObjectName(u"War")
        self.War.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.War, 8, 0, 1, 1)

        self.Western = QCheckBox(self.layoutWidget2)
        self.Western.setObjectName(u"Western")
        self.Western.setStyleSheet(u"font: 700 9pt \"Consolas\";")

        self.gridLayout.addWidget(self.Western, 8, 1, 1, 1)

        self.layoutWidget3 = QWidget(self.row_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(720, 0, 291, 48))
        self.gridLayout_2 = QGridLayout(self.layoutWidget3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)

        self.horizontalSlider = QSlider(self.layoutWidget3)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 1, 0, 1, 1)

        self.horizontalSlider_2 = QSlider(self.layoutWidget3)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_2, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.row_2)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 317, 1160, 277))
        self.label.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(self.new_page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 1160, 591))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.resultTitle = QLabel(self.frame)
        self.resultTitle.setObjectName(u"resultTitle")
        self.resultTitle.setGeometry(QRect(280, 10, 581, 31))
        self.resultTitle.setStyleSheet(u"font: 700 24pt \"Consolas\";")
        self.Name = QLabel(self.frame)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(340, 158, 341, 131))
        sizePolicy3.setHeightForWidth(self.Name.sizePolicy().hasHeightForWidth())
        self.Name.setSizePolicy(sizePolicy3)
        self.Name.setMinimumSize(QSize(160, 50))
        self.Name.setMaximumSize(QSize(1000, 1000))
        self.Name.setStyleSheet(u"font: 700 20pt \"Consolas\";")
        self.Name.setWordWrap(True)
        self.Rating = QLabel(self.frame)
        self.Rating.setObjectName(u"Rating")
        self.Rating.setGeometry(QRect(699, 199, 151, 81))
        sizePolicy3.setHeightForWidth(self.Rating.sizePolicy().hasHeightForWidth())
        self.Rating.setSizePolicy(sizePolicy3)
        self.Rating.setMinimumSize(QSize(110, 50))
        self.Rating.setMaximumSize(QSize(1000, 1000))
        self.Rating.setStyleSheet(u"font: 700 14pt \"Consolas\";")
        self.Rating.setAlignment(Qt.AlignCenter)
        self.Runtime = QLabel(self.frame)
        self.Runtime.setObjectName(u"Runtime")
        self.Runtime.setGeometry(QRect(860, 199, 151, 81))
        sizePolicy3.setHeightForWidth(self.Runtime.sizePolicy().hasHeightForWidth())
        self.Runtime.setSizePolicy(sizePolicy3)
        self.Runtime.setMinimumSize(QSize(110, 50))
        self.Runtime.setMaximumSize(QSize(1000, 1000))
        self.Runtime.setStyleSheet(u"font: 700 14pt \"Consolas\";")
        self.Runtime.setAlignment(Qt.AlignCenter)
        self.Poster = QLabel(self.frame)
        self.Poster.setObjectName(u"Poster")
        self.Poster.setGeometry(QRect(49, 59, 200, 320))
        self.Poster.setMinimumSize(QSize(200, 320))
        self.Poster.setMaximumSize(QSize(200, 320))
        self.Poster.setStyleSheet(u"background-image: url(:/images/images/images/transparent.png);")
        self.Poster.setScaledContents(True)
        self.Description = QLabel(self.new_page)
        self.Description.setObjectName(u"Description")
        self.Description.setGeometry(QRect(40, 350, 631, 241))
        sizePolicy3.setHeightForWidth(self.Description.sizePolicy().hasHeightForWidth())
        self.Description.setSizePolicy(sizePolicy3)
        self.Description.setMaximumSize(QSize(900, 300))
        self.Description.setStyleSheet(u"font: 700 14pt \"Consolas\";")
        self.Description.setWordWrap(True)
        self.Genre = QLabel(self.new_page)
        self.Genre.setObjectName(u"Genre")
        self.Genre.setGeometry(QRect(709, 290, 151, 81))
        sizePolicy3.setHeightForWidth(self.Genre.sizePolicy().hasHeightForWidth())
        self.Genre.setSizePolicy(sizePolicy3)
        self.Genre.setMinimumSize(QSize(110, 50))
        self.Genre.setMaximumSize(QSize(1000, 1000))
        self.Genre.setStyleSheet(u"font: 700 14pt \"Consolas\";")
        self.Genre.setAlignment(Qt.AlignCenter)
        self.UserScore = QLabel(self.new_page)
        self.UserScore.setObjectName(u"UserScore")
        self.UserScore.setGeometry(QRect(870, 290, 151, 81))
        sizePolicy3.setHeightForWidth(self.UserScore.sizePolicy().hasHeightForWidth())
        self.UserScore.setSizePolicy(sizePolicy3)
        self.UserScore.setMinimumSize(QSize(110, 50))
        self.UserScore.setMaximumSize(QSize(1000, 1000))
        self.UserScore.setStyleSheet(u"font: 700 14pt \"Consolas\";")
        self.UserScore.setAlignment(Qt.AlignCenter)
        self.rollAgain = QPushButton(self.new_page)
        self.rollAgain.setObjectName(u"rollAgain")
        self.rollAgain.setGeometry(QRect(790, 390, 130, 30))
        sizePolicy3.setHeightForWidth(self.rollAgain.sizePolicy().hasHeightForWidth())
        self.rollAgain.setSizePolicy(sizePolicy3)
        self.rollAgain.setMinimumSize(QSize(130, 30))
        self.rollAgain.setMaximumSize(QSize(130, 30))
        self.rollAgain.setStyleSheet(u"font: 700 14pt \"Consolas\";")
        self.stackedWidget.addWidget(self.new_page)
        self.SearchMoviePage = QWidget()
        self.SearchMoviePage.setObjectName(u"SearchMoviePage")
        self.SearchMoviePage.setMinimumSize(QSize(1178, 603))
        self.verticalLayout_22 = QVBoxLayout(self.SearchMoviePage)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.SearchBoxArea = QWidget(self.SearchMoviePage)
        self.SearchBoxArea.setObjectName(u"SearchBoxArea")
        self.SearchBoxArea.setMinimumSize(QSize(0, 50))
        self.SearchBoxArea.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_7 = QHBoxLayout(self.SearchBoxArea)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.searchBar = QLineEdit(self.SearchBoxArea)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_7.addWidget(self.searchBar, 0, Qt.AlignTop)

        self.btn_SearchMovie = QPushButton(self.SearchBoxArea)
        self.btn_SearchMovie.setObjectName(u"btn_SearchMovie")
        self.btn_SearchMovie.setMinimumSize(QSize(0, 40))
        self.btn_SearchMovie.setStyleSheet(u"background-color: rgb(44, 49, 58);")

        self.horizontalLayout_7.addWidget(self.btn_SearchMovie, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_22.addWidget(self.SearchBoxArea)

        self.scrollArea_2 = QScrollArea(self.SearchMoviePage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy4)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setHidden(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setEnabled(True)
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1150, 2352))
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.SearchMovieWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget.setObjectName(u"SearchMovieWidget")
        self.SearchMovieWidget.setEnabled(True)
        self.SearchMovieWidget.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.SearchMovieWidget.setHidden(True)
        self.horizontalLayout_8 = QHBoxLayout(self.SearchMovieWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.posterWidget = QWidget(self.SearchMovieWidget)
        self.posterWidget.setObjectName(u"posterWidget")
        self.posterWidget.setMinimumSize(QSize(95, 128))
        self.posterWidget.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_26 = QHBoxLayout(self.posterWidget)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.posterLabel = QLabel(self.posterWidget)
        self.posterLabel.setObjectName(u"posterLabel")
        self.posterLabel.setAutoFillBackground(False)
        self.posterLabel.setStyleSheet(u"background-image: url(:/images/images/images/transparent.png);")
        self.posterLabel.setPixmap(QPixmap(u":/images/images/images/No_Image_Available.jpg"))
        self.posterLabel.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.posterLabel)


        self.horizontalLayout_8.addWidget(self.posterWidget, 0, Qt.AlignLeft)

        self.TitleWidget = QWidget(self.SearchMovieWidget)
        self.TitleWidget.setObjectName(u"TitleWidget")
        sizePolicy4.setHeightForWidth(self.TitleWidget.sizePolicy().hasHeightForWidth())
        self.TitleWidget.setSizePolicy(sizePolicy4)
        self.TitleWidget.setMinimumSize(QSize(800, 0))
        self.TitleWidget.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_24 = QVBoxLayout(self.TitleWidget)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.Title = QLabel(self.TitleWidget)
        self.Title.setObjectName(u"Title")
        self.Title.setStyleSheet(u"")
        self.Title.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.Title)

        self.Details = QLabel(self.TitleWidget)
        self.Details.setObjectName(u"Details")
        self.Details.setEnabled(True)
        self.Details.setMinimumSize(QSize(777, 0))
        self.Details.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.Details)


        self.horizontalLayout_8.addWidget(self.TitleWidget)

        self.addMovieButton = QPushButton(self.SearchMovieWidget)
        self.addMovieButton.setObjectName(u"addMovieButton")
        self.addMovieButton.setMinimumSize(QSize(200, 0))
        self.addMovieButton.setMaximumSize(QSize(200, 75))
        self.addMovieButton.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_8.addWidget(self.addMovieButton)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget)

        self.SearchMovieWidget_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget_2.setObjectName(u"SearchMovieWidget_2")
        self.SearchMovieWidget_2.setEnabled(True)
        self.SearchMovieWidget_2.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget_2.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget_2.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.SearchMovieWidget_2.setHidden(True)
        self.horizontalLayout_10 = QHBoxLayout(self.SearchMovieWidget_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.posterWidget_2 = QWidget(self.SearchMovieWidget_2)
        self.posterWidget_2.setObjectName(u"posterWidget_2")
        self.posterWidget_2.setMinimumSize(QSize(95, 128))
        self.posterWidget_2.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_27 = QHBoxLayout(self.posterWidget_2)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.posterLabel_2 = QLabel(self.posterWidget_2)
        self.posterLabel_2.setObjectName(u"posterLabel_2")

        self.horizontalLayout_27.addWidget(self.posterLabel_2)


        self.horizontalLayout_10.addWidget(self.posterWidget_2)

        self.TitleWidget_2 = QWidget(self.SearchMovieWidget_2)
        self.TitleWidget_2.setObjectName(u"TitleWidget_2")
        self.TitleWidget_2.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget_2.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_25 = QVBoxLayout(self.TitleWidget_2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.Title_2 = QLabel(self.TitleWidget_2)
        self.Title_2.setObjectName(u"Title_2")
        self.Title_2.setStyleSheet(u"")
        self.Title_2.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.Title_2)

        self.Details_2 = QLabel(self.TitleWidget_2)
        self.Details_2.setObjectName(u"Details_2")
        self.Details_2.setEnabled(True)
        self.Details_2.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.Details_2)


        self.horizontalLayout_10.addWidget(self.TitleWidget_2)

        self.addMovieButton_2 = QPushButton(self.SearchMovieWidget_2)
        self.addMovieButton_2.setObjectName(u"addMovieButton_2")
        self.addMovieButton_2.setMaximumSize(QSize(200, 75))
        self.addMovieButton_2.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_10.addWidget(self.addMovieButton_2)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget_2)

        self.SearchMovieWidget_3 = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget_3.setObjectName(u"SearchMovieWidget_3")
        self.SearchMovieWidget_3.setEnabled(True)
        self.SearchMovieWidget_3.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget_3.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget_3.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.SearchMovieWidget_3.setHidden(True)
        self.horizontalLayout_13 = QHBoxLayout(self.SearchMovieWidget_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.posterWidget_3 = QWidget(self.SearchMovieWidget_3)
        self.posterWidget_3.setObjectName(u"posterWidget_3")
        self.posterWidget_3.setMinimumSize(QSize(95, 128))
        self.posterWidget_3.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_28 = QHBoxLayout(self.posterWidget_3)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.posterLabel_3 = QLabel(self.posterWidget_3)
        self.posterLabel_3.setObjectName(u"posterLabel_3")

        self.horizontalLayout_28.addWidget(self.posterLabel_3)


        self.horizontalLayout_13.addWidget(self.posterWidget_3)

        self.TitleWidget_3 = QWidget(self.SearchMovieWidget_3)
        self.TitleWidget_3.setObjectName(u"TitleWidget_3")
        self.TitleWidget_3.setMinimumSize(QSize(800, 0))
        self.TitleWidget_3.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget_3.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_26 = QVBoxLayout(self.TitleWidget_3)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.Title_3 = QLabel(self.TitleWidget_3)
        self.Title_3.setObjectName(u"Title_3")
        self.Title_3.setStyleSheet(u"")
        self.Title_3.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.Title_3)

        self.Details_3 = QLabel(self.TitleWidget_3)
        self.Details_3.setObjectName(u"Details_3")
        self.Details_3.setEnabled(True)
        self.Details_3.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.Details_3)


        self.horizontalLayout_13.addWidget(self.TitleWidget_3)

        self.addMovieButton_3 = QPushButton(self.SearchMovieWidget_3)
        self.addMovieButton_3.setObjectName(u"addMovieButton_3")
        self.addMovieButton_3.setMaximumSize(QSize(200, 75))
        self.addMovieButton_3.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_13.addWidget(self.addMovieButton_3)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget_3)

        self.SearchMovieWidget_4 = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget_4.setObjectName(u"SearchMovieWidget_4")
        self.SearchMovieWidget_4.setEnabled(True)
        self.SearchMovieWidget_4.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget_4.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget_4.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.SearchMovieWidget_4.setHidden(True)
        self.horizontalLayout_14 = QHBoxLayout(self.SearchMovieWidget_4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.posterWidget_4 = QWidget(self.SearchMovieWidget_4)
        self.posterWidget_4.setObjectName(u"posterWidget_4")
        self.posterWidget_4.setMinimumSize(QSize(95, 128))
        self.posterWidget_4.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_29 = QHBoxLayout(self.posterWidget_4)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.posterLabel_4 = QLabel(self.posterWidget_4)
        self.posterLabel_4.setObjectName(u"posterLabel_4")
        self.posterLabel_4.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.posterLabel_4)


        self.horizontalLayout_14.addWidget(self.posterWidget_4)

        self.TitleWidget_4 = QWidget(self.SearchMovieWidget_4)
        self.TitleWidget_4.setObjectName(u"TitleWidget_4")
        self.TitleWidget_4.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget_4.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_27 = QVBoxLayout(self.TitleWidget_4)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.Title_4 = QLabel(self.TitleWidget_4)
        self.Title_4.setObjectName(u"Title_4")
        self.Title_4.setStyleSheet(u"")
        self.Title_4.setWordWrap(True)

        self.verticalLayout_27.addWidget(self.Title_4)

        self.Details_4 = QLabel(self.TitleWidget_4)
        self.Details_4.setObjectName(u"Details_4")
        self.Details_4.setEnabled(True)
        self.Details_4.setWordWrap(True)

        self.verticalLayout_27.addWidget(self.Details_4)


        self.horizontalLayout_14.addWidget(self.TitleWidget_4)

        self.addMovieButton_4 = QPushButton(self.SearchMovieWidget_4)
        self.addMovieButton_4.setObjectName(u"addMovieButton_4")
        self.addMovieButton_4.setMaximumSize(QSize(200, 75))
        self.addMovieButton_4.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_14.addWidget(self.addMovieButton_4)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget_4)

        self.SearchMovieWidget_5 = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget_5.setObjectName(u"SearchMovieWidget_5")
        self.SearchMovieWidget_5.setEnabled(True)
        self.SearchMovieWidget_5.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget_5.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget_5.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.SearchMovieWidget_5.setHidden(True)
        self.horizontalLayout_15 = QHBoxLayout(self.SearchMovieWidget_5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.posterWidget_5 = QWidget(self.SearchMovieWidget_5)
        self.posterWidget_5.setObjectName(u"posterWidget_5")
        self.posterWidget_5.setMinimumSize(QSize(95, 128))
        self.posterWidget_5.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_30 = QHBoxLayout(self.posterWidget_5)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.posterLabel_5 = QLabel(self.posterWidget_5)
        self.posterLabel_5.setObjectName(u"posterLabel_5")
        self.posterLabel_5.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.posterLabel_5)


        self.horizontalLayout_15.addWidget(self.posterWidget_5)

        self.TitleWidget_5 = QWidget(self.SearchMovieWidget_5)
        self.TitleWidget_5.setObjectName(u"TitleWidget_5")
        self.TitleWidget_5.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget_5.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_28 = QVBoxLayout(self.TitleWidget_5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.Title_5 = QLabel(self.TitleWidget_5)
        self.Title_5.setObjectName(u"Title_5")
        self.Title_5.setStyleSheet(u"")
        self.Title_5.setWordWrap(True)

        self.verticalLayout_28.addWidget(self.Title_5)

        self.Details_5 = QLabel(self.TitleWidget_5)
        self.Details_5.setObjectName(u"Details_5")
        self.Details_5.setEnabled(True)
        self.Details_5.setWordWrap(True)

        self.verticalLayout_28.addWidget(self.Details_5)


        self.horizontalLayout_15.addWidget(self.TitleWidget_5)

        self.addMovieButton_5 = QPushButton(self.SearchMovieWidget_5)
        self.addMovieButton_5.setObjectName(u"addMovieButton_5")
        self.addMovieButton_5.setMaximumSize(QSize(200, 75))
        self.addMovieButton_5.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_15.addWidget(self.addMovieButton_5)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget_5)

        self.SearchMovieWidget_6 = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget_6.setObjectName(u"SearchMovieWidget_6")
        self.SearchMovieWidget_6.setEnabled(True)
        self.SearchMovieWidget_6.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget_6.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget_6.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.SearchMovieWidget_6.setHidden(True)
        self.horizontalLayout_16 = QHBoxLayout(self.SearchMovieWidget_6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.posterWidget_6 = QWidget(self.SearchMovieWidget_6)
        self.posterWidget_6.setObjectName(u"posterWidget_6")
        self.posterWidget_6.setMinimumSize(QSize(95, 128))
        self.posterWidget_6.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_31 = QHBoxLayout(self.posterWidget_6)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.posterLabel_6 = QLabel(self.posterWidget_6)
        self.posterLabel_6.setObjectName(u"posterLabel_6")
        self.posterLabel_6.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.posterLabel_6)


        self.horizontalLayout_16.addWidget(self.posterWidget_6)

        self.TitleWidget_6 = QWidget(self.SearchMovieWidget_6)
        self.TitleWidget_6.setObjectName(u"TitleWidget_6")
        self.TitleWidget_6.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget_6.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_29 = QVBoxLayout(self.TitleWidget_6)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.Title_6 = QLabel(self.TitleWidget_6)
        self.Title_6.setObjectName(u"Title_6")
        self.Title_6.setStyleSheet(u"")
        self.Title_6.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.Title_6)

        self.Details_6 = QLabel(self.TitleWidget_6)
        self.Details_6.setObjectName(u"Details_6")
        self.Details_6.setEnabled(True)
        self.Details_6.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.Details_6)


        self.horizontalLayout_16.addWidget(self.TitleWidget_6)

        self.addMovieButton_6 = QPushButton(self.SearchMovieWidget_6)
        self.addMovieButton_6.setObjectName(u"addMovieButton_6")
        self.addMovieButton_6.setMaximumSize(QSize(200, 75))
        self.addMovieButton_6.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_16.addWidget(self.addMovieButton_6)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget_6)

        self.SearchMovieWidget_7 = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget_7.setObjectName(u"SearchMovieWidget_7")
        self.SearchMovieWidget_7.setEnabled(True)
        self.SearchMovieWidget_7.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget_7.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget_7.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.SearchMovieWidget_7.setHidden(True)
        self.horizontalLayout_17 = QHBoxLayout(self.SearchMovieWidget_7)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.posterWidget_7 = QWidget(self.SearchMovieWidget_7)
        self.posterWidget_7.setObjectName(u"posterWidget_7")
        self.posterWidget_7.setMinimumSize(QSize(95, 128))
        self.posterWidget_7.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_32 = QHBoxLayout(self.posterWidget_7)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.posterLabel_7 = QLabel(self.posterWidget_7)
        self.posterLabel_7.setObjectName(u"posterLabel_7")
        self.posterLabel_7.setScaledContents(True)

        self.horizontalLayout_32.addWidget(self.posterLabel_7)


        self.horizontalLayout_17.addWidget(self.posterWidget_7)

        self.TitleWidget_7 = QWidget(self.SearchMovieWidget_7)
        self.TitleWidget_7.setObjectName(u"TitleWidget_7")
        self.TitleWidget_7.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget_7.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_30 = QVBoxLayout(self.TitleWidget_7)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.Title_7 = QLabel(self.TitleWidget_7)
        self.Title_7.setObjectName(u"Title_7")
        self.Title_7.setStyleSheet(u"")
        self.Title_7.setWordWrap(True)

        self.verticalLayout_30.addWidget(self.Title_7)

        self.Details_7 = QLabel(self.TitleWidget_7)
        self.Details_7.setObjectName(u"Details_7")
        self.Details_7.setEnabled(True)
        self.Details_7.setWordWrap(True)

        self.verticalLayout_30.addWidget(self.Details_7)


        self.horizontalLayout_17.addWidget(self.TitleWidget_7)

        self.addMovieButton_7 = QPushButton(self.SearchMovieWidget_7)
        self.addMovieButton_7.setObjectName(u"addMovieButton_7")
        self.addMovieButton_7.setMaximumSize(QSize(200, 75))
        self.addMovieButton_7.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_17.addWidget(self.addMovieButton_7)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget_7)

        self.SearchMovieWidget_8 = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget_8.setObjectName(u"SearchMovieWidget_8")
        self.SearchMovieWidget_8.setEnabled(True)
        self.SearchMovieWidget_8.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget_8.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget_8.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.SearchMovieWidget_8.setHidden(True)
        self.horizontalLayout_18 = QHBoxLayout(self.SearchMovieWidget_8)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.posterWidget_8 = QWidget(self.SearchMovieWidget_8)
        self.posterWidget_8.setObjectName(u"posterWidget_8")
        self.posterWidget_8.setMinimumSize(QSize(95, 128))
        self.posterWidget_8.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_33 = QHBoxLayout(self.posterWidget_8)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.posterLabel_8 = QLabel(self.posterWidget_8)
        self.posterLabel_8.setObjectName(u"posterLabel_8")
        self.posterLabel_8.setScaledContents(True)

        self.horizontalLayout_33.addWidget(self.posterLabel_8)


        self.horizontalLayout_18.addWidget(self.posterWidget_8)

        self.TitleWidget_8 = QWidget(self.SearchMovieWidget_8)
        self.TitleWidget_8.setObjectName(u"TitleWidget_8")
        self.TitleWidget_8.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget_8.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_31 = QVBoxLayout(self.TitleWidget_8)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.Title_8 = QLabel(self.TitleWidget_8)
        self.Title_8.setObjectName(u"Title_8")
        self.Title_8.setStyleSheet(u"")
        self.Title_8.setWordWrap(True)

        self.verticalLayout_31.addWidget(self.Title_8)

        self.Details_8 = QLabel(self.TitleWidget_8)
        self.Details_8.setObjectName(u"Details_8")
        self.Details_8.setEnabled(True)
        self.Details_8.setWordWrap(True)

        self.verticalLayout_31.addWidget(self.Details_8)


        self.horizontalLayout_18.addWidget(self.TitleWidget_8)

        self.addMovieButton_8 = QPushButton(self.SearchMovieWidget_8)
        self.addMovieButton_8.setObjectName(u"addMovieButton_8")
        self.addMovieButton_8.setMaximumSize(QSize(200, 75))
        self.addMovieButton_8.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_18.addWidget(self.addMovieButton_8)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget_8)

        self.SearchMovieWidget_9 = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget_9.setObjectName(u"SearchMovieWidget_9")
        self.SearchMovieWidget_9.setEnabled(True)
        self.SearchMovieWidget_9.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget_9.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget_9.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.SearchMovieWidget_9.setHidden(True)
        self.horizontalLayout_19 = QHBoxLayout(self.SearchMovieWidget_9)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.posterWidget_9 = QWidget(self.SearchMovieWidget_9)
        self.posterWidget_9.setObjectName(u"posterWidget_9")
        self.posterWidget_9.setMinimumSize(QSize(95, 128))
        self.posterWidget_9.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_34 = QHBoxLayout(self.posterWidget_9)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.posterLabel_9 = QLabel(self.posterWidget_9)
        self.posterLabel_9.setObjectName(u"posterLabel_9")
        self.posterLabel_9.setScaledContents(True)

        self.horizontalLayout_34.addWidget(self.posterLabel_9)


        self.horizontalLayout_19.addWidget(self.posterWidget_9)

        self.TitleWidget_9 = QWidget(self.SearchMovieWidget_9)
        self.TitleWidget_9.setObjectName(u"TitleWidget_9")
        self.TitleWidget_9.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget_9.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_32 = QVBoxLayout(self.TitleWidget_9)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.Title_9 = QLabel(self.TitleWidget_9)
        self.Title_9.setObjectName(u"Title_9")
        self.Title_9.setStyleSheet(u"")
        self.Title_9.setWordWrap(True)

        self.verticalLayout_32.addWidget(self.Title_9)

        self.Details_9 = QLabel(self.TitleWidget_9)
        self.Details_9.setObjectName(u"Details_9")
        self.Details_9.setEnabled(True)
        self.Details_9.setWordWrap(True)

        self.verticalLayout_32.addWidget(self.Details_9)


        self.horizontalLayout_19.addWidget(self.TitleWidget_9)

        self.addMovieButton_9 = QPushButton(self.SearchMovieWidget_9)
        self.addMovieButton_9.setObjectName(u"addMovieButton_9")
        self.addMovieButton_9.setMaximumSize(QSize(200, 75))
        self.addMovieButton_9.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_19.addWidget(self.addMovieButton_9)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget_9)

        self.SearchMovieWidget_10 = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget_10.setObjectName(u"SearchMovieWidget_10")
        self.SearchMovieWidget_10.setEnabled(True)
        self.SearchMovieWidget_10.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget_10.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget_10.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.SearchMovieWidget_10.setHidden(True)
        self.horizontalLayout_20 = QHBoxLayout(self.SearchMovieWidget_10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.posterWidget_10 = QWidget(self.SearchMovieWidget_10)
        self.posterWidget_10.setObjectName(u"posterWidget_10")
        self.posterWidget_10.setMinimumSize(QSize(95, 128))
        self.posterWidget_10.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_35 = QHBoxLayout(self.posterWidget_10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.posterLabel_10 = QLabel(self.posterWidget_10)
        self.posterLabel_10.setObjectName(u"posterLabel_10")

        self.horizontalLayout_35.addWidget(self.posterLabel_10)


        self.horizontalLayout_20.addWidget(self.posterWidget_10)

        self.TitleWidget_10 = QWidget(self.SearchMovieWidget_10)
        self.TitleWidget_10.setObjectName(u"TitleWidget_10")
        self.TitleWidget_10.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget_10.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_33 = QVBoxLayout(self.TitleWidget_10)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.Title_10 = QLabel(self.TitleWidget_10)
        self.Title_10.setObjectName(u"Title_10")
        self.Title_10.setStyleSheet(u"")
        self.Title_10.setWordWrap(True)

        self.verticalLayout_33.addWidget(self.Title_10)

        self.Details_10 = QLabel(self.TitleWidget_10)
        self.Details_10.setObjectName(u"Details_10")
        self.Details_10.setEnabled(False)
        self.Details_10.setWordWrap(True)

        self.verticalLayout_33.addWidget(self.Details_10)


        self.horizontalLayout_20.addWidget(self.TitleWidget_10)

        self.addMovieButton_10 = QPushButton(self.SearchMovieWidget_10)
        self.addMovieButton_10.setObjectName(u"addMovieButton_10")
        self.addMovieButton_10.setMaximumSize(QSize(200, 75))
        self.addMovieButton_10.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_20.addWidget(self.addMovieButton_10)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget_10)

        self.SearchMovieWidget_11 = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget_11.setObjectName(u"SearchMovieWidget_11")
        self.SearchMovieWidget_11.setEnabled(True)
        self.SearchMovieWidget_11.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget_11.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget_11.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.SearchMovieWidget_11.setHidden(True)
        self.horizontalLayout_21 = QHBoxLayout(self.SearchMovieWidget_11)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.posterWidget_11 = QWidget(self.SearchMovieWidget_11)
        self.posterWidget_11.setObjectName(u"posterWidget_11")
        self.posterWidget_11.setMinimumSize(QSize(95, 128))
        self.posterWidget_11.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_36 = QHBoxLayout(self.posterWidget_11)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.posterLabel_11 = QLabel(self.posterWidget_11)
        self.posterLabel_11.setObjectName(u"posterLabel_11")

        self.horizontalLayout_36.addWidget(self.posterLabel_11)


        self.horizontalLayout_21.addWidget(self.posterWidget_11)

        self.TitleWidget_11 = QWidget(self.SearchMovieWidget_11)
        self.TitleWidget_11.setObjectName(u"TitleWidget_11")
        self.TitleWidget_11.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget_11.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_34 = QVBoxLayout(self.TitleWidget_11)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.Title_11 = QLabel(self.TitleWidget_11)
        self.Title_11.setObjectName(u"Title_11")
        self.Title_11.setStyleSheet(u"")
        self.Title_11.setWordWrap(True)

        self.verticalLayout_34.addWidget(self.Title_11)

        self.Details_11 = QLabel(self.TitleWidget_11)
        self.Details_11.setObjectName(u"Details_11")
        self.Details_11.setEnabled(True)
        self.Details_11.setWordWrap(True)

        self.verticalLayout_34.addWidget(self.Details_11)


        self.horizontalLayout_21.addWidget(self.TitleWidget_11)

        self.addMovieButton_11 = QPushButton(self.SearchMovieWidget_11)
        self.addMovieButton_11.setObjectName(u"addMovieButton_11")
        self.addMovieButton_11.setMaximumSize(QSize(200, 75))
        self.addMovieButton_11.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_21.addWidget(self.addMovieButton_11)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget_11)

        self.SearchMovieWidget_12 = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget_12.setObjectName(u"SearchMovieWidget_12")
        self.SearchMovieWidget_12.setEnabled(True)
        self.SearchMovieWidget_12.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget_12.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget_12.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.SearchMovieWidget_12.setHidden(True)
        self.horizontalLayout_22 = QHBoxLayout(self.SearchMovieWidget_12)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.posterWidget_12 = QWidget(self.SearchMovieWidget_12)
        self.posterWidget_12.setObjectName(u"posterWidget_12")
        self.posterWidget_12.setMinimumSize(QSize(95, 128))
        self.posterWidget_12.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_37 = QHBoxLayout(self.posterWidget_12)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.posterLabel_12 = QLabel(self.posterWidget_12)
        self.posterLabel_12.setObjectName(u"posterLabel_12")

        self.horizontalLayout_37.addWidget(self.posterLabel_12)


        self.horizontalLayout_22.addWidget(self.posterWidget_12)

        self.TitleWidget_12 = QWidget(self.SearchMovieWidget_12)
        self.TitleWidget_12.setObjectName(u"TitleWidget_12")
        self.TitleWidget_12.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget_12.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_35 = QVBoxLayout(self.TitleWidget_12)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.Title_12 = QLabel(self.TitleWidget_12)
        self.Title_12.setObjectName(u"Title_12")
        self.Title_12.setStyleSheet(u"")
        self.Title_12.setWordWrap(True)

        self.verticalLayout_35.addWidget(self.Title_12)

        self.Details_12 = QLabel(self.TitleWidget_12)
        self.Details_12.setObjectName(u"Details_12")
        self.Details_12.setEnabled(True)
        self.Details_12.setWordWrap(True)

        self.verticalLayout_35.addWidget(self.Details_12)


        self.horizontalLayout_22.addWidget(self.TitleWidget_12)

        self.addMovieButton_12 = QPushButton(self.SearchMovieWidget_12)
        self.addMovieButton_12.setObjectName(u"addMovieButton_12")
        self.addMovieButton_12.setMaximumSize(QSize(200, 75))
        self.addMovieButton_12.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_22.addWidget(self.addMovieButton_12)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget_12)

        self.SearchMovieWidget_13 = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget_13.setObjectName(u"SearchMovieWidget_13")
        self.SearchMovieWidget_13.setEnabled(True)
        self.SearchMovieWidget_13.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget_13.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget_13.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.horizontalLayout_23 = QHBoxLayout(self.SearchMovieWidget_13)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.posterWidget_13 = QWidget(self.SearchMovieWidget_13)
        self.posterWidget_13.setObjectName(u"posterWidget_13")
        self.posterWidget_13.setMinimumSize(QSize(95, 128))
        self.posterWidget_13.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_38 = QHBoxLayout(self.posterWidget_13)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.posterLabel_13 = QLabel(self.posterWidget_13)
        self.posterLabel_13.setObjectName(u"posterLabel_13")
        self.posterLabel_13.setScaledContents(True)

        self.horizontalLayout_38.addWidget(self.posterLabel_13)


        self.horizontalLayout_23.addWidget(self.posterWidget_13)

        self.TitleWidget_13 = QWidget(self.SearchMovieWidget_13)
        self.TitleWidget_13.setObjectName(u"TitleWidget_13")
        self.TitleWidget_13.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget_13.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_36 = QVBoxLayout(self.TitleWidget_13)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.Title_13 = QLabel(self.TitleWidget_13)
        self.Title_13.setObjectName(u"Title_13")
        self.Title_13.setStyleSheet(u"")
        self.Title_13.setWordWrap(True)

        self.verticalLayout_36.addWidget(self.Title_13)

        self.Details_13 = QLabel(self.TitleWidget_13)
        self.Details_13.setObjectName(u"Details_13")
        self.Details_13.setEnabled(True)
        self.Details_13.setWordWrap(True)

        self.verticalLayout_36.addWidget(self.Details_13)


        self.horizontalLayout_23.addWidget(self.TitleWidget_13)

        self.addMovieButton_13 = QPushButton(self.SearchMovieWidget_13)
        self.addMovieButton_13.setObjectName(u"addMovieButton_13")
        self.addMovieButton_13.setMaximumSize(QSize(200, 75))
        self.addMovieButton_13.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_23.addWidget(self.addMovieButton_13)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget_13)

        self.SearchMovieWidget_14 = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget_14.setObjectName(u"SearchMovieWidget_14")
        self.SearchMovieWidget_14.setEnabled(True)
        self.SearchMovieWidget_14.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget_14.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget_14.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.SearchMovieWidget_14.setHidden(True)
        self.horizontalLayout_24 = QHBoxLayout(self.SearchMovieWidget_14)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.posterWidget_14 = QWidget(self.SearchMovieWidget_14)
        self.posterWidget_14.setObjectName(u"posterWidget_14")
        self.posterWidget_14.setMinimumSize(QSize(95, 128))
        self.posterWidget_14.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_39 = QHBoxLayout(self.posterWidget_14)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.posterLabel_14 = QLabel(self.posterWidget_14)
        self.posterLabel_14.setObjectName(u"posterLabel_14")
        self.posterLabel_14.setScaledContents(True)

        self.horizontalLayout_39.addWidget(self.posterLabel_14)


        self.horizontalLayout_24.addWidget(self.posterWidget_14)

        self.TitleWidget_14 = QWidget(self.SearchMovieWidget_14)
        self.TitleWidget_14.setObjectName(u"TitleWidget_14")
        self.TitleWidget_14.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget_14.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_37 = QVBoxLayout(self.TitleWidget_14)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.Title_14 = QLabel(self.TitleWidget_14)
        self.Title_14.setObjectName(u"Title_14")
        self.Title_14.setStyleSheet(u"")
        self.Title_14.setWordWrap(True)

        self.verticalLayout_37.addWidget(self.Title_14)

        self.Details_14 = QLabel(self.TitleWidget_14)
        self.Details_14.setObjectName(u"Details_14")
        self.Details_14.setEnabled(True)
        self.Details_14.setWordWrap(True)

        self.verticalLayout_37.addWidget(self.Details_14)


        self.horizontalLayout_24.addWidget(self.TitleWidget_14)

        self.addMovieButton_14 = QPushButton(self.SearchMovieWidget_14)
        self.addMovieButton_14.setObjectName(u"addMovieButton_14")
        self.addMovieButton_14.setMaximumSize(QSize(200, 75))
        self.addMovieButton_14.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_24.addWidget(self.addMovieButton_14)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget_14)

        self.SearchMovieWidget_15 = QWidget(self.scrollAreaWidgetContents_2)
        self.SearchMovieWidget_15.setObjectName(u"SearchMovieWidget_15")
        self.SearchMovieWidget_15.setEnabled(True)
        self.SearchMovieWidget_15.setMinimumSize(QSize(0, 150))
        self.SearchMovieWidget_15.setMaximumSize(QSize(16777215, 150))
        self.SearchMovieWidget_15.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.SearchMovieWidget_15.setHidden(True)
        self.horizontalLayout_25 = QHBoxLayout(self.SearchMovieWidget_15)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.posterWidget_15 = QWidget(self.SearchMovieWidget_15)
        self.posterWidget_15.setObjectName(u"posterWidget_15")
        self.posterWidget_15.setMinimumSize(QSize(95, 128))
        self.posterWidget_15.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_40 = QHBoxLayout(self.posterWidget_15)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.posterLabel_15 = QLabel(self.posterWidget_15)
        self.posterLabel_15.setObjectName(u"posterLabel_15")
        self.posterLabel_15.setScaledContents(True)

        self.horizontalLayout_40.addWidget(self.posterLabel_15)


        self.horizontalLayout_25.addWidget(self.posterWidget_15)

        self.TitleWidget_15 = QWidget(self.SearchMovieWidget_15)
        self.TitleWidget_15.setObjectName(u"TitleWidget_15")
        self.TitleWidget_15.setMaximumSize(QSize(800, 16777215))
        self.TitleWidget_15.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.verticalLayout_38 = QVBoxLayout(self.TitleWidget_15)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.Title_15 = QLabel(self.TitleWidget_15)
        self.Title_15.setObjectName(u"Title_15")
        self.Title_15.setStyleSheet(u"")
        self.Title_15.setWordWrap(True)

        self.verticalLayout_38.addWidget(self.Title_15)

        self.Details_15 = QLabel(self.TitleWidget_15)
        self.Details_15.setObjectName(u"Details_15")
        self.Details_15.setEnabled(True)
        self.Details_15.setWordWrap(True)

        self.verticalLayout_38.addWidget(self.Details_15)


        self.horizontalLayout_25.addWidget(self.TitleWidget_15)

        self.addMovieButton_15 = QPushButton(self.SearchMovieWidget_15)
        self.addMovieButton_15.setObjectName(u"addMovieButton_15")
        self.addMovieButton_15.setMaximumSize(QSize(200, 75))
        self.addMovieButton_15.setStyleSheet(u"background-color: rgb(48, 53, 63);")

        self.horizontalLayout_25.addWidget(self.addMovieButton_15)


        self.verticalLayout_23.addWidget(self.SearchMovieWidget_15)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_22.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.SearchMoviePage)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.CreditLogoLabel = QLabel(self.bottomBar)
        self.CreditLogoLabel.setObjectName(u"CreditLogoLabel")
        sizePolicy4.setHeightForWidth(self.CreditLogoLabel.sizePolicy().hasHeightForWidth())
        self.CreditLogoLabel.setSizePolicy(sizePolicy4)
        self.CreditLogoLabel.setPixmap(QPixmap(u":/icons/images/icons/tmdb_icon.png"))
        self.CreditLogoLabel.setScaledContents(False)

        self.horizontalLayout_5.addWidget(self.CreditLogoLabel, 0, Qt.AlignRight|Qt.AlignBottom)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Movie Roulette", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Time to get you a movie", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Filters", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Clear List", None))
        #self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        #self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
       # self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        #self.extraCloseColumnBtn.setText("")
        #self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        #self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        #self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        '''self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))'''
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"PyDracula APP - Theme with colors based on Dracula for Python.", None))
#if QT_CONFIG(tooltip)
        #self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
       # self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.ClearListSure.setText(QCoreApplication.translate("MainWindow", u"Are you sure you want to clear your list?", None))
        self.btn_spin.setText(QCoreApplication.translate("MainWindow", u"Spin The Wheel", None))
        self.Filters.setText(QCoreApplication.translate("MainWindow", u"Filters", None))
        self.Genre_2.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        self.Popularity.setText(QCoreApplication.translate("MainWindow", u"Popularity", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Runtime", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Release Date (Year)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.Action.setText(QCoreApplication.translate("MainWindow", u"Action", None))
        self.Adventure.setText(QCoreApplication.translate("MainWindow", u"Adventure", None))
        self.Animation.setText(QCoreApplication.translate("MainWindow", u"Animation", None))
        self.Comedy.setText(QCoreApplication.translate("MainWindow", u"Comedy", None))
        self.Crime.setText(QCoreApplication.translate("MainWindow", u"Crime", None))
        self.Documentary.setText(QCoreApplication.translate("MainWindow", u"Documentary", None))
        self.Drama.setText(QCoreApplication.translate("MainWindow", u"Drama", None))
        self.Family.setText(QCoreApplication.translate("MainWindow", u"Family", None))
        self.Fantasy.setText(QCoreApplication.translate("MainWindow", u"Fantasy", None))
        self.History.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.Horror.setText(QCoreApplication.translate("MainWindow", u"Horror", None))
        self.Music.setText(QCoreApplication.translate("MainWindow", u"Music", None))
        self.Mystery.setText(QCoreApplication.translate("MainWindow", u"Mystery", None))
        self.Romance.setText(QCoreApplication.translate("MainWindow", u"Romance", None))
        self.SciFi.setText(QCoreApplication.translate("MainWindow", u"Sci Fi", None))
        self.Thriller.setText(QCoreApplication.translate("MainWindow", u"Thriller", None))
        self.War.setText(QCoreApplication.translate("MainWindow", u"War", None))
        self.Western.setText(QCoreApplication.translate("MainWindow", u"Western", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label.setText("")
        self.resultTitle.setText(QCoreApplication.translate("MainWindow", u"And Your Movie For Tonight Is...", None))
        self.Name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Rating.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Runtime.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Poster.setText("")
        self.Description.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Genre.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.UserScore.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.rollAgain.setText(QCoreApplication.translate("MainWindow", u"Roll Again?", None))
        self.btn_SearchMovie.setText(QCoreApplication.translate("MainWindow", u"Search Movie", None))
        self.posterLabel.setText("")
        self.Title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.posterLabel_2.setText("")
        self.Title_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton_2.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.posterLabel_3.setText("")
        self.Title_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton_3.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.posterLabel_4.setText("")
        self.Title_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton_4.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.posterLabel_5.setText("")
        self.Title_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton_5.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.posterLabel_6.setText("")
        self.Title_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton_6.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.posterLabel_7.setText("")
        self.Title_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton_7.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.posterLabel_8.setText("")
        self.Title_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton_8.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.posterLabel_9.setText("")
        self.Title_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton_9.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.posterLabel_10.setText("")
        self.Title_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton_10.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.posterLabel_11.setText("")
        self.Title_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton_11.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.posterLabel_12.setText("")
        self.Title_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton_12.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.posterLabel_13.setText("")
        self.Title_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton_13.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.posterLabel_14.setText("")
        self.Title_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton_14.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.posterLabel_15.setText("")
        self.Title_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Details_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.addMovieButton_15.setText(QCoreApplication.translate("MainWindow", u"Add Movie", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"This product uses the TMDB API but is not endorsed or certified by TMDB.", None))
        self.CreditLogoLabel.setText("")
    # retranslateUi

