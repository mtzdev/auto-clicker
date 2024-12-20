# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowBgLNXE.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 366)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(3, -2, 841, 51))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u"font-family: \"Segoe UI\", Arial, sans-serif;\n"
"font-size: 38px;\n"
"font-weight: bold;\n"
"color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:1, y2:0,\n"
"    stop:0 #1565C0,\n"
"    stop:0.5 #0D47A1,\n"
"    stop:1 #42A5F5\n"
");\n"
"border: none;\n"
"background: transparent;\n"
"padding: 10px 25px;\n"
"border-radius: 12px;\n"
"\n"
"QLabel::hover {\n"
"    transform: scale(1.05);\n"
"    box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);\n"
"}\n"
"")
        self.titleLabel.setFrameShape(QFrame.Shape.NoFrame)
        self.titleLabel.setTextFormat(Qt.TextFormat.AutoText)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineSeparator = QFrame(self.centralwidget)
        self.lineSeparator.setObjectName(u"lineSeparator")
        self.lineSeparator.setGeometry(QRect(0, 50, 841, 21))
        self.lineSeparator.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineSeparator.setFrameShape(QFrame.Shape.HLine)
        self.lineSeparator.setFrameShadow(QFrame.Shadow.Sunken)
        self.mouseBox = QGroupBox(self.centralwidget)
        self.mouseBox.setObjectName(u"mouseBox")
        self.mouseBox.setGeometry(QRect(10, 60, 391, 281))
        self.mouseBox.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.mouseBox.setStyleSheet(u"QGroupBox {\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: #2979FF;\n"
"    border: 2px solid #2979FF;\n"
"    border-radius: 8px;\n"
"    margin-top: 15px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 10px;\n"
"    color: #FFFFFF;\n"
"    background-color: #121212;\n"
"    border-radius: 4px;\n"
"}")
        self.mouseBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.keybindMLabel = QLabel(self.mouseBox)
        self.keybindMLabel.setObjectName(u"keybindMLabel")
        self.keybindMLabel.setGeometry(QRect(10, 140, 105, 25))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.keybindMLabel.setFont(font1)
        self.keybindMLabel.setStyleSheet(u"font: 16pt \"Verdana\";")
        self.modeMLabel = QLabel(self.mouseBox)
        self.modeMLabel.setObjectName(u"modeMLabel")
        self.modeMLabel.setGeometry(QRect(10, 210, 182, 25))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.modeMLabel.setFont(font2)
        self.modeMLabel.setStyleSheet(u"font: 14pt \"Verdana\";")
        self.cpsMLabel = QLabel(self.mouseBox)
        self.cpsMLabel.setObjectName(u"cpsMLabel")
        self.cpsMLabel.setGeometry(QRect(10, 70, 225, 23))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(15)
        font3.setBold(False)
        font3.setItalic(False)
        self.cpsMLabel.setFont(font3)
        self.cpsMLabel.setStyleSheet(u"font: 15pt \"Verdana\";")
        self.cpsMouseSpin = QSpinBox(self.mouseBox)
        self.cpsMouseSpin.setObjectName(u"cpsMouseSpin")
        self.cpsMouseSpin.setGeometry(QRect(240, 71, 91, 25))
        self.cpsMouseSpin.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.cpsMouseSpin.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.cpsMouseSpin.setStyleSheet(u"font: 12pt \"Verdana\";")
        self.cpsMouseSpin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cpsMouseSpin.setAccelerated(True)
        self.cpsMouseSpin.setMinimum(1)
        self.cpsMouseSpin.setMaximum(1000)
        self.cpsMouseSpin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.cpsMouseSpin.setValue(5)
        self.cpsMouseSpin.setDisplayIntegerBase(10)
        self.bindMouseButton = QPushButton(self.mouseBox)
        self.bindMouseButton.setObjectName(u"bindMouseButton")
        self.bindMouseButton.setGeometry(QRect(180, 140, 191, 31))
        self.bindMouseButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bindMouseButton.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.bindMouseButton.setStyleSheet(u"font: 10pt \"Verdana\";")
        self.lineEdit = QLineEdit(self.mouseBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 140, 31, 31))
        self.lineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lineEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit.setAcceptDrops(False)
        self.lineEdit.setStyleSheet(u"font: 15pt \"Verdana\";")
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.leftModeButton = QPushButton(self.mouseBox)
        self.leftModeButton.setObjectName(u"leftModeButton")
        self.leftModeButton.setGeometry(QRect(180, 210, 90, 31))
        self.leftModeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.leftModeButton.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.leftModeButton.setStyleSheet(u"font: 10pt \"Verdana\";")
        self.rightModeButton = QPushButton(self.mouseBox)
        self.rightModeButton.setObjectName(u"rightModeButton")
        self.rightModeButton.setGeometry(QRect(280, 210, 90, 31))
        self.rightModeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.rightModeButton.setMouseTracking(False)
        self.rightModeButton.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.rightModeButton.setAcceptDrops(False)
        self.rightModeButton.setAutoFillBackground(False)
        self.rightModeButton.setStyleSheet(u"font: 10pt \"Verdana\";")
        self.rightModeButton.setCheckable(False)
        self.rightModeButton.setAutoDefault(False)
        self.rightModeButton.setFlat(False)
        self.tecladoBox = QGroupBox(self.centralwidget)
        self.tecladoBox.setObjectName(u"tecladoBox")
        self.tecladoBox.setGeometry(QRect(410, 60, 431, 281))
        self.tecladoBox.setStyleSheet(u"QGroupBox {\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: #2979FF;\n"
"    border: 2px solid #2979FF;\n"
"    border-radius: 8px;\n"
"    margin-top: 15px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 10px;\n"
"    color: #FFFFFF;\n"
"    background-color: #121212;\n"
"    border-radius: 4px;\n"
"}")
        self.tecladoBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.todo_keyboard_label = QLabel(self.tecladoBox)
        self.todo_keyboard_label.setObjectName(u"todo_keyboard_label")
        self.todo_keyboard_label.setGeometry(QRect(50, 120, 296, 38))
        self.todo_keyboard_label.setMaximumSize(QSize(296, 38))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI 13"])
        font4.setPointSize(22)
        font4.setBold(False)
        font4.setItalic(False)
        self.todo_keyboard_label.setFont(font4)
        self.todo_keyboard_label.setStyleSheet(u"font: 22pt \"Segoe UI\" bold;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.rightModeButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"mtz Auto-Clicker", None))
        self.mouseBox.setTitle(QCoreApplication.translate("MainWindow", u"MOUSE", None))
        self.keybindMLabel.setText(QCoreApplication.translate("MainWindow", u"Key-Bind:", None))
        self.modeMLabel.setText(QCoreApplication.translate("MainWindow", u"Modo AutoClick:", None))
        self.cpsMLabel.setText(QCoreApplication.translate("MainWindow", u"Cliques por segundo:", None))
        self.bindMouseButton.setText(QCoreApplication.translate("MainWindow", u"CLIQUE AQUI PARA BINDAR", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.leftModeButton.setText(QCoreApplication.translate("MainWindow", u"ESQUERDO", None))
        self.rightModeButton.setText(QCoreApplication.translate("MainWindow", u"DIREITO", None))
        self.tecladoBox.setTitle(QCoreApplication.translate("MainWindow", u"TECLADO", None))
        self.todo_keyboard_label.setText(QCoreApplication.translate("MainWindow", u"Em desenvolvimento!", None))
    # retranslateUi

