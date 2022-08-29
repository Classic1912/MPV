# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QWidget)
import imagens

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(408, 456)
        MainWindow.setMinimumSize(QSize(408, 456))
        MainWindow.setMaximumSize(QSize(408, 456))
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/BTT/icons/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.625 rgba(0, 8, 131, 200), stop:0.988636 rgba(109, 70, 151, 255));\n"
"border-radius: 2px;")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"border-radius: 5px;")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 25, 391, 371))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.listWidget.setFont(font1)
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.244318 rgba(0, 15, 255, 55), stop:0.994318 rgba(255, 0, 208, 111));\n"
"	font: 700 italic 18pt \"Calibri\";\n"
"	color: rgb(32, 27, 44);\n"
"	border-radius: 11px;\n"
"	border: 1px solid rgb(170, 0, 0) ;\n"
"	\n"
"}\n"
"QListWidget:pressed {\n"
"	border-radius: 11px;\n"
"}\n"
"QListWidget:item:selected{\n"
"	color: rgb(32, 27, 44);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.238636 rgba(0, 15, 255, 69), stop:0.994318 rgba(255, 0, 208, 82));\n"
"	border-radius: 11px;\n"
"}\n"
"QScrollBar {\n"
"	background-color: rgb(32, 27, 44);\n"
"}")
        self.bt_anterior = QPushButton(self.centralwidget)
        self.bt_anterior.setObjectName(u"bt_anterior")
        self.bt_anterior.setGeometry(QRect(140, 420, 35, 30))
        self.bt_anterior.setFont(font)
        self.bt_anterior.setStyleSheet(u"QPushButton {\n"
"	border-radius: 11px;\n"
"	border: 1px solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 118, 118, 255), stop:0.988636 rgba(255, 220, 142, 255));\n"
"	Icon: url(:/BTT/icons/retroceder - normal.png);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.238636 rgba(0, 15, 255, 69), stop:0.994318 rgba(255, 0, 208, 82));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 11px;\n"
"}\n"
"QPushButton:pressed {\n"
"	border-radius: 12px;\n"
"	border: 1px solid ;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 0, 0, 164), stop:0.988636 rgba(255, 175, 0, 89));\n"
"	Icon: url(:/BTT/icons/retroceder - press.png);\n"
"\n"
"}")
        self.bt_anterior.setIconSize(QSize(30, 30))
        self.bt_play = QPushButton(self.centralwidget)
        self.bt_play.setObjectName(u"bt_play")
        self.bt_play.setGeometry(QRect(180, 420, 35, 30))
        self.bt_play.setFont(font)
        self.bt_play.setStyleSheet(u"QPushButton {\n"
"	border-radius: 11px;\n"
"	border: 1px solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 118, 118, 255), stop:0.988636 rgba(255, 220, 142, 255));\n"
"	Icon: url(:/BTT/icons/reproduzir.png);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.238636 rgba(0, 15, 255, 69), stop:0.994318 rgba(255, 0, 208, 82));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 11px;\n"
"}\n"
"QPushButton:pressed {\n"
"	border-radius: 12px;\n"
"	border: 1px solid ;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 0, 0, 164), stop:0.988636 rgba(255, 175, 0, 89));\n"
"}")
        self.bt_play.setText(u"")
        self.bt_play.setIconSize(QSize(30, 30))
        self.bt_proximo = QPushButton(self.centralwidget)
        self.bt_proximo.setObjectName(u"bt_proximo")
        self.bt_proximo.setGeometry(QRect(220, 420, 35, 30))
        font2 = QFont()
        font2.setPointSize(50)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.bt_proximo.setFont(font2)
        self.bt_proximo.setStyleSheet(u"QPushButton {\n"
"	border-radius: 11px;\n"
"	border: 1px solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 118, 118, 255), stop:0.988636 rgba(255, 220, 142, 255));\n"
"	Icon: url(:/BTT/icons/avan - normal.png);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.238636 rgba(0, 15, 255, 69), stop:0.994318 rgba(255, 0, 208, 82));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 11px;\n"
"}\n"
"QPushButton:pressed {\n"
"	border-radius: 12px;\n"
"	border: 1px solid ;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 0, 0, 164), stop:0.988636 rgba(255, 175, 0, 89));\n"
"	Icon: url(:/BTT/icons/avan - press.png);\n"
"\n"
"}")
        self.bt_proximo.setIconSize(QSize(30, 30))
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(59, 400, 291, 15))
        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setStyleSheet(u"QSlider{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.267045 rgba(0, 15, 255, 55), stop:0.994318 rgba(255, 0, 208, 111));\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider:handle {\n"
"	background-color: rgb(32, 27, 44);\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider:add-page {\n"
"	background-color: rgba(81, 11, 163, 0.45);\n"
"}\n"
"QSlider:sub-page {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.267045 rgba(0, 15, 255, 55), stop:0.994318 rgba(255, 0, 208, 111));\n"
"}")
        self.horizontalSlider.setValue(0)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.bt_sair = QPushButton(self.centralwidget)
        self.bt_sair.setObjectName(u"bt_sair")
        self.bt_sair.setGeometry(QRect(387, 1, 21, 20))
        self.bt_sair.setFont(font)
        self.bt_sair.setStyleSheet(u"QPushButton {\n"
"	border-radius: 6px;\n"
"	border: 1px solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 118, 118, 255), stop:0.988636 rgba(255, 220, 142, 255));\n"
"	Icon: url(:/BTT/icons/excluir - normal.png);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.238636 rgba(0, 15, 255, 69), stop:0.994318 rgba(255, 0, 208, 82));\n"
"}\n"
"QPushButton:pressed {\n"
"	bborder-radius: 6px;\n"
"	border: 1px solid ;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 0, 0, 164), stop:0.988636 rgba(255, 175, 0, 89));\n"
"	Icon: url(:/BTT/icons/excluir - press.png);\n"
"\n"
"}")
        self.bt_minimizar = QPushButton(self.centralwidget)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setGeometry(QRect(365, 1, 21, 20))
        self.bt_minimizar.setFont(font)
        self.bt_minimizar.setStyleSheet(u"QPushButton {\n"
"	border-radius: 6px;\n"
"	border: 1px solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 118, 118, 255), stop:0.988636 rgba(255, 220, 142, 255));\n"
"	Icon: url(:/BTT/icons/minimizar - normal.png);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.238636 rgba(0, 15, 255, 69), stop:0.994318 rgba(255, 0, 208, 82));\n"
"}\n"
"QPushButton:pressed {\n"
"	border-radius: 6px;\n"
"	border: 1px solid ;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 0, 0, 164), stop:0.988636 rgba(255, 175, 0, 89));\n"
"	Icon: url(:/BTT/icons/minimizar - press.png);\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 88, 16))
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgba(255, 170, 255, 130);")
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.bt_diretorio = QPushButton(self.centralwidget)
        self.bt_diretorio.setObjectName(u"bt_diretorio")
        self.bt_diretorio.setGeometry(QRect(385, 435, 21, 21))
        self.bt_diretorio.setFont(font)
        self.bt_diretorio.setStyleSheet(u"QPushButton {\n"
"	border-radius: 11px;\n"
"	border: 1px solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 118, 118, 255), stop:0.988636 rgba(255, 220, 142, 255));\n"
"	Icon: url(:/BTT/icons/abrir.png);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.238636 rgba(0, 15, 255, 69), stop:0.994318 rgba(255, 0, 208, 82));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 11px;\n"
"}\n"
"QPushButton:pressed {\n"
"	border-radius: 12px;\n"
"	border: 1px solid ;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 0, 0, 164), stop:0.988636 rgba(255, 175, 0, 89));\n"
"	icon: url(:/BTT/icons/abrir - press.png);\n"
"}")
        self.bt_diretorio.setText(u"")
        self.bt_diretorio.setIconSize(QSize(20, 20))
        self.bt_diretorio.setCheckable(False)
        self.bt_diretorio.setFlat(False)
        self.l_selec_pasta = QLabel(self.centralwidget)
        self.l_selec_pasta.setObjectName(u"l_selec_pasta")
        self.l_selec_pasta.setEnabled(True)
        self.l_selec_pasta.setGeometry(QRect(260, 435, 124, 20))
        self.l_selec_pasta.setFont(font)
        self.l_selec_pasta.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.238636 rgba(0, 15, 255, 69), stop:0.994318 rgba(255, 0, 208, 82));")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.bt_diretorio.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_anterior.setText("")
        self.bt_proximo.setText("")
        self.bt_sair.setText("")
        self.bt_minimizar.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Cr\u00e9ditos: <a href=\"https://icons8.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Icons8</span></a></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.bt_diretorio.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; font-style:italic; color:#201b2c;\">Selecionar um Diret\u00f3rio</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.l_selec_pasta.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700; font-style:italic; color:#201b2c;\">Selecione uma pasta -&gt;</span></p></body></html>", None))
    # retranslateUi

