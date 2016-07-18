# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Mon Jul 18 16:29:31 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1083, 734)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/icons/favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 136, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 136, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 136, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 136, 136))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.splitter.setPalette(palette)
        self.splitter.setStyleSheet(_fromUtf8("QSplitter::handle {\n"
"    background: rgb(175, 175, 175);\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background: rgb(106, 106, 106)\n"
"}\n"
"\n"
"QSplitter::handle:pressed {\n"
"    image: rgb(71, 255, 39);\n"
"}\n"
"\n"
"#handle_left_arrow, #handle_right_arrow{\n"
"    color: rgb(175, 175, 175);\n"
"}\n"
""))
        self.splitter.setFrameShape(QtGui.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtGui.QFrame.Plain)
        self.splitter.setMidLineWidth(2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(2)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.button_bar = QtGui.QFrame(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_bar.sizePolicy().hasHeightForWidth())
        self.button_bar.setSizePolicy(sizePolicy)
        self.button_bar.setMinimumSize(QtCore.QSize(0, 50))
        self.button_bar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.button_bar.setStyleSheet(_fromUtf8("#button_bar{\n"
"    border: 1px solid grey;\n"
"    border-radius: 2px; \n"
"    background: rgb(225, 225, 225);\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: 1px solid grey;\n"
"    border-radius: 2px; \n"
"    background: rgb(245, 245, 245);\n"
"}\n"
"\n"
"#context_button_group>QPushButton{\n"
"    border: none;\n"
"}\n"
"\n"
"#context_button_group{\n"
"    border: 1px solid grey;\n"
"    border-radius: 2px;\n"
"    background: rgb(245, 245, 245);\n"
"}\n"
"\n"
"QPushButton:hover, #context_button_group>QPushButton:hover{\n"
"    border: 1px solid rgb(112, 111, 142);\n"
"    background: rgb(235, 235, 250)\n"
"}\n"
""))
        self.button_bar.setFrameShape(QtGui.QFrame.Box)
        self.button_bar.setFrameShadow(QtGui.QFrame.Sunken)
        self.button_bar.setObjectName(_fromUtf8("button_bar"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.button_bar)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.new_button = QtGui.QPushButton(self.button_bar)
        self.new_button.setMinimumSize(QtCore.QSize(0, 0))
        self.new_button.setMaximumSize(QtCore.QSize(30, 30))
        self.new_button.setAutoFillBackground(False)
        self.new_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/icons/new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_button.setIcon(icon1)
        self.new_button.setIconSize(QtCore.QSize(20, 20))
        self.new_button.setObjectName(_fromUtf8("new_button"))
        self.horizontalLayout.addWidget(self.new_button)
        self.open_button = QtGui.QPushButton(self.button_bar)
        self.open_button.setMinimumSize(QtCore.QSize(28, 0))
        self.open_button.setMaximumSize(QtCore.QSize(30, 30))
        self.open_button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/icons/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_button.setIcon(icon2)
        self.open_button.setIconSize(QtCore.QSize(26, 19))
        self.open_button.setObjectName(_fromUtf8("open_button"))
        self.horizontalLayout.addWidget(self.open_button)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.context_button_group = QtGui.QGroupBox(self.button_bar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.context_button_group.sizePolicy().hasHeightForWidth())
        self.context_button_group.setSizePolicy(sizePolicy)
        self.context_button_group.setMinimumSize(QtCore.QSize(325, 35))
        self.context_button_group.setTitle(_fromUtf8(""))
        self.context_button_group.setObjectName(_fromUtf8("context_button_group"))
        self.plus_button = QtGui.QPushButton(self.context_button_group)
        self.plus_button.setGeometry(QtCore.QRect(10, 5, 25, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.plus_button.setPalette(palette)
        self.plus_button.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/icons/plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plus_button.setIcon(icon3)
        self.plus_button.setIconSize(QtCore.QSize(21, 21))
        self.plus_button.setObjectName(_fromUtf8("plus_button"))
        self.minus_button = QtGui.QPushButton(self.context_button_group)
        self.minus_button.setGeometry(QtCore.QRect(70, 5, 25, 25))
        self.minus_button.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/icons/minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minus_button.setIcon(icon4)
        self.minus_button.setIconSize(QtCore.QSize(21, 21))
        self.minus_button.setObjectName(_fromUtf8("minus_button"))
        self.edit_button = QtGui.QPushButton(self.context_button_group)
        self.edit_button.setGeometry(QtCore.QRect(180, 5, 25, 25))
        self.edit_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_button.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.edit_button.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/icons/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_button.setIcon(icon5)
        self.edit_button.setIconSize(QtCore.QSize(21, 21))
        self.edit_button.setObjectName(_fromUtf8("edit_button"))
        self.reset_button = QtGui.QPushButton(self.context_button_group)
        self.reset_button.setGeometry(QtCore.QRect(150, 5, 25, 25))
        self.reset_button.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/icons/reset.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_button.setIcon(icon6)
        self.reset_button.setIconSize(QtCore.QSize(21, 21))
        self.reset_button.setObjectName(_fromUtf8("reset_button"))
        self.lock_button = QtGui.QPushButton(self.context_button_group)
        self.lock_button.setGeometry(QtCore.QRect(290, 5, 25, 25))
        self.lock_button.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/icons/unlocked-yellow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/icons/locked-yellow.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.lock_button.setIcon(icon7)
        self.lock_button.setIconSize(QtCore.QSize(19, 19))
        self.lock_button.setCheckable(True)
        self.lock_button.setObjectName(_fromUtf8("lock_button"))
        self.copy_button = QtGui.QPushButton(self.context_button_group)
        self.copy_button.setGeometry(QtCore.QRect(40, 5, 25, 25))
        self.copy_button.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/icons/copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_button.setIcon(icon8)
        self.copy_button.setIconSize(QtCore.QSize(21, 21))
        self.copy_button.setObjectName(_fromUtf8("copy_button"))
        self.clean_button = QtGui.QPushButton(self.context_button_group)
        self.clean_button.setGeometry(QtCore.QRect(240, 5, 25, 25))
        self.clean_button.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/icons/clean.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clean_button.setIcon(icon9)
        self.clean_button.setIconSize(QtCore.QSize(22, 21))
        self.clean_button.setObjectName(_fromUtf8("clean_button"))
        self.context_open_button = QtGui.QPushButton(self.context_button_group)
        self.context_open_button.setGeometry(QtCore.QRect(210, 5, 25, 25))
        self.context_open_button.setMinimumSize(QtCore.QSize(0, 0))
        self.context_open_button.setMaximumSize(QtCore.QSize(30, 30))
        self.context_open_button.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/icons/open-context.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.context_open_button.setIcon(icon10)
        self.context_open_button.setIconSize(QtCore.QSize(21, 21))
        self.context_open_button.setObjectName(_fromUtf8("context_open_button"))
        self.line = QtGui.QFrame(self.context_button_group)
        self.line.setGeometry(QtCore.QRect(100, 0, 16, 33))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.context_button_group)
        self.line_2.setGeometry(QtCore.QRect(270, 0, 16, 33))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.status_button = QtGui.QPushButton(self.context_button_group)
        self.status_button.setGeometry(QtCore.QRect(120, 5, 25, 25))
        self.status_button.setMaximumSize(QtCore.QSize(25, 25))
        self.status_button.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/buttons/icons/reload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.status_button.setIcon(icon11)
        self.status_button.setIconSize(QtCore.QSize(20, 20))
        self.status_button.setObjectName(_fromUtf8("status_button"))
        self.horizontalLayout.addWidget(self.context_button_group)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.scenario_choice_button = QtGui.QPushButton(self.button_bar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scenario_choice_button.sizePolicy().hasHeightForWidth())
        self.scenario_choice_button.setSizePolicy(sizePolicy)
        self.scenario_choice_button.setMinimumSize(QtCore.QSize(100, 45))
        self.scenario_choice_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scenario_choice_button.setObjectName(_fromUtf8("scenario_choice_button"))
        self.horizontalLayout.addWidget(self.scenario_choice_button)
        self.verticalLayout_3.addWidget(self.button_bar)
        self.qtreeview = QtGui.QTreeView(self.layoutWidget)
        self.qtreeview.setEnabled(True)
        self.qtreeview.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 241, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.qtreeview.setPalette(palette)
        self.qtreeview.setExpandsOnDoubleClick(True)
        self.qtreeview.setObjectName(_fromUtf8("qtreeview"))
        self.qtreeview.header().setMinimumSectionSize(50)
        self.verticalLayout_3.addWidget(self.qtreeview)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.handle_left_arrow = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.handle_left_arrow.sizePolicy().hasHeightForWidth())
        self.handle_left_arrow.setSizePolicy(sizePolicy)
        self.handle_left_arrow.setObjectName(_fromUtf8("handle_left_arrow"))
        self.horizontalLayout_3.addWidget(self.handle_left_arrow)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.handle_right_arrow = QtGui.QLabel(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.handle_right_arrow.sizePolicy().hasHeightForWidth())
        self.handle_right_arrow.setSizePolicy(sizePolicy)
        self.handle_right_arrow.setObjectName(_fromUtf8("handle_right_arrow"))
        self.horizontalLayout_2.addWidget(self.handle_right_arrow)
        self.details_layout = QtGui.QVBoxLayout()
        self.details_layout.setObjectName(_fromUtf8("details_layout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.details_layout.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.details_layout)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1083, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuDatei = QtGui.QMenu(self.menubar)
        self.menuDatei.setObjectName(_fromUtf8("menuDatei"))
        self.menuProjekt = QtGui.QMenu(self.menubar)
        self.menuProjekt.setObjectName(_fromUtf8("menuProjekt"))
        self.menuZuletzt_benutzt = QtGui.QMenu(self.menuProjekt)
        self.menuZuletzt_benutzt.setObjectName(_fromUtf8("menuZuletzt_benutzt"))
        self.menuSzenario = QtGui.QMenu(self.menubar)
        self.menuSzenario.setObjectName(_fromUtf8("menuSzenario"))
        self.menuL_ufe = QtGui.QMenu(self.menubar)
        self.menuL_ufe.setObjectName(_fromUtf8("menuL_ufe"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionBeenden = QtGui.QAction(MainWindow)
        self.actionBeenden.setObjectName(_fromUtf8("actionBeenden"))
        self.actionProjekt_ffnen = QtGui.QAction(MainWindow)
        self.actionProjekt_ffnen.setObjectName(_fromUtf8("actionProjekt_ffnen"))
        self.actionProjekt_speichern = QtGui.QAction(MainWindow)
        self.actionProjekt_speichern.setObjectName(_fromUtf8("actionProjekt_speichern"))
        self.actionNeues_Projekt = QtGui.QAction(MainWindow)
        self.actionNeues_Projekt.setObjectName(_fromUtf8("actionNeues_Projekt"))
        self.actionNeues_Szenario = QtGui.QAction(MainWindow)
        self.actionNeues_Szenario.setObjectName(_fromUtf8("actionNeues_Szenario"))
        self.actionEinstellungen = QtGui.QAction(MainWindow)
        self.actionEinstellungen.setObjectName(_fromUtf8("actionEinstellungen"))
        self.actionInfo = QtGui.QAction(MainWindow)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.actionSzenario_duplizieren = QtGui.QAction(MainWindow)
        self.actionSzenario_duplizieren.setObjectName(_fromUtf8("actionSzenario_duplizieren"))
        self.actionSzenario_l_schen = QtGui.QAction(MainWindow)
        self.actionSzenario_l_schen.setObjectName(_fromUtf8("actionSzenario_l_schen"))
        self.actionProjekt_schlie_en = QtGui.QAction(MainWindow)
        self.actionProjekt_schlie_en.setObjectName(_fromUtf8("actionProjekt_schlie_en"))
        self.actionBla = QtGui.QAction(MainWindow)
        self.actionBla.setObjectName(_fromUtf8("actionBla"))
        self.actionGesamtlauf_starten = QtGui.QAction(MainWindow)
        self.actionGesamtlauf_starten.setObjectName(_fromUtf8("actionGesamtlauf_starten"))
        self.actionSpezifischen_Lauf_anlegen = QtGui.QAction(MainWindow)
        self.actionSpezifischen_Lauf_anlegen.setObjectName(_fromUtf8("actionSpezifischen_Lauf_anlegen"))
        self.actionSpezifischen_Lauf_starten = QtGui.QAction(MainWindow)
        self.actionSpezifischen_Lauf_starten.setObjectName(_fromUtf8("actionSpezifischen_Lauf_starten"))
        self.menuDatei.addAction(self.actionEinstellungen)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionBeenden)
        self.menuProjekt.addAction(self.actionNeues_Projekt)
        self.menuProjekt.addAction(self.actionProjekt_ffnen)
        self.menuProjekt.addAction(self.actionProjekt_schlie_en)
        self.menuProjekt.addSeparator()
        self.menuProjekt.addAction(self.menuZuletzt_benutzt.menuAction())
        self.menuSzenario.addAction(self.actionNeues_Szenario)
        self.menuSzenario.addAction(self.actionSzenario_duplizieren)
        self.menuSzenario.addAction(self.actionSzenario_l_schen)
        self.menuL_ufe.addAction(self.actionGesamtlauf_starten)
        self.menuL_ufe.addAction(self.actionSpezifischen_Lauf_anlegen)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuProjekt.menuAction())
        self.menubar.addAction(self.menuSzenario.menuAction())
        self.menubar.addAction(self.menuL_ufe.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "GGR Verkehrsmodelle", None))
        self.new_button.setToolTip(_translate("MainWindow", "neues Projekt", None))
        self.open_button.setToolTip(_translate("MainWindow", "Projekt öffnen", None))
        self.plus_button.setToolTip(_translate("MainWindow", "Hinzufügen", None))
        self.minus_button.setToolTip(_translate("MainWindow", "Entfernen", None))
        self.edit_button.setToolTip(_translate("MainWindow", "Umbenennen", None))
        self.reset_button.setToolTip(_translate("MainWindow", "Zurücksetzen", None))
        self.lock_button.setToolTip(_translate("MainWindow", "Sperren", None))
        self.copy_button.setToolTip(_translate("MainWindow", "Kopieren", None))
        self.clean_button.setToolTip(_translate("MainWindow", "Aufräumen", None))
        self.context_open_button.setToolTip(_translate("MainWindow", "Öffnen", None))
        self.status_button.setToolTip(_translate("MainWindow", "Prüfen", None))
        self.scenario_choice_button.setText(_translate("MainWindow", "angeklicktes\n"
"Szenario wählen \n"
" und schließen", None))
        self.handle_left_arrow.setText(_translate("MainWindow", "< ", None))
        self.handle_right_arrow.setText(_translate("MainWindow", " >", None))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei", None))
        self.menuProjekt.setTitle(_translate("MainWindow", "Projekt", None))
        self.menuZuletzt_benutzt.setTitle(_translate("MainWindow", "zuletzt benutzt", None))
        self.menuSzenario.setTitle(_translate("MainWindow", "Szenario", None))
        self.menuL_ufe.setTitle(_translate("MainWindow", "Läufe", None))
        self.actionBeenden.setText(_translate("MainWindow", "Beenden", None))
        self.actionProjekt_ffnen.setText(_translate("MainWindow", "Projekt öffnen", None))
        self.actionProjekt_speichern.setText(_translate("MainWindow", "Projekt speichern", None))
        self.actionNeues_Projekt.setText(_translate("MainWindow", "Neues Projekt", None))
        self.actionNeues_Szenario.setText(_translate("MainWindow", "Neues Szenario", None))
        self.actionEinstellungen.setText(_translate("MainWindow", "Einstellungen", None))
        self.actionInfo.setText(_translate("MainWindow", "Info", None))
        self.actionSzenario_duplizieren.setText(_translate("MainWindow", "Szenario duplizieren", None))
        self.actionSzenario_l_schen.setText(_translate("MainWindow", "Szenario löschen", None))
        self.actionProjekt_schlie_en.setText(_translate("MainWindow", "Projekt schließen", None))
        self.actionBla.setText(_translate("MainWindow", "bla", None))
        self.actionGesamtlauf_starten.setText(_translate("MainWindow", "Gesamtlauf starten", None))
        self.actionSpezifischen_Lauf_anlegen.setText(_translate("MainWindow", "spezifischen Lauf anlegen", None))
        self.actionSpezifischen_Lauf_starten.setText(_translate("MainWindow", "spezifischen Lauf starten", None))

import gui_rc
