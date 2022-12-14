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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QWidget)
import imagens

class Ui_MusicPlayer(object):
    def setupUi(self, MusicPlayer):
        if not MusicPlayer.objectName():
            MusicPlayer.setObjectName(u"MusicPlayer")
        MusicPlayer.setWindowModality(Qt.WindowModal)
        MusicPlayer.resize(408, 456)
        MusicPlayer.setMinimumSize(QSize(408, 456))
        MusicPlayer.setMaximumSize(QSize(408, 456))
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        MusicPlayer.setFont(font)
        icon = QIcon()
        icon.addFile(u":/BTT/icons/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MusicPlayer.setWindowIcon(icon)
        MusicPlayer.setStyleSheet(u"background-color: rgb(43, 25, 62);\n"
"border-radius: 2px;")
        MusicPlayer.setAnimated(True)
        self.centralwidget = QWidget(MusicPlayer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"border-radius: 5px;")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 25, 391, 371))
        font1 = QFont()
        font1.setFamilies([u"Ink Free"])
        font1.setPointSize(17)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.listWidget.setFont(font1)
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	font: 17pt \"Ink Free\";\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.238636 rgba(43, 25, 62, 255), stop:0.994318 rgba(255, 0, 208, 111));\n"
"	color: rgb(32, 27, 44);\n"
"	border-radius: 11px;\n"
"}\n"
"QListWidget:item:selected{\n"
"	selection-color: rgb(255, 170, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.238636 rgba(43, 25, 62, 255), stop:0.994318 rgba(255, 0, 208, 111));\n"
"	border-radius: 11px;\n"
"}\n"
"QListWidget:item:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.238636 rgba(43, 25, 62, 255), stop:0.994318 rgba(255, 0, 208, 111));\n"
"	border-radius: 11px;\n"
"}\n"
"QScrollBar {\n"
"	background-color: rgb(32, 27, 44);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.238636 rgba(43, 25, 62, 255), stop:0.994318 rgba(255, 0, 208, 111));\n"
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
"	background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(43, 25, 62, 255), stop:1 rgba(255, 0, 208, 111));\n"
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
"	background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(43, 25, 62, 255), stop:1 rgba(255, 0, 208, 111));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 11px;\n"
"}\n"
"QPushButton:pressed {\n"
"	border-radius: 12px;\n"
"	border: 1px solid ;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 0, 0, 164), stop:0.988636 rgba(255, 175, 0, 89));\n"
"	icon: url(:/BTT/icons/reproduzir - press.png);\n"
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
"	background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(43, 25, 62, 255), stop:1 rgba(255, 0, 208, 111));\n"
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
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:0, stop:0.238636 rgba(43, 25, 62, 255), stop:0.994318 rgba(255, 0, 208, 111));\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider:handle {\n"
"	background-color: rgb(32, 27, 44);\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider:add-page {\n"
"	alternate-background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:0, stop:0.238636 rgba(43, 25, 62, 255), stop:0.994318 rgba(255, 0, 208, 111));\n"
"}\n"
"QSlider:sub-page {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.238636 rgba(43, 25, 62, 255), stop:0.994318 rgba(255, 0, 208, 111));\n"
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
"	background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(43, 25, 62, 255), stop:1 rgba(255, 0, 208, 111));\n"
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
"	background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(43, 25, 62, 255), stop:1 rgba(255, 0, 208, 111));\n"
"}\n"
"QPushButton:pressed {\n"
"	border-radius: 6px;\n"
"	border: 1px solid ;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 0, 0, 164), stop:0.988636 rgba(255, 175, 0, 89));\n"
"	Icon: url(:/BTT/icons/minimizar - press.png);\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 440, 91, 16))
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgba(255, 170, 255, 130);\n"
"border: 1px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 118, 118, 255), stop:0.988636 rgba(255, 220, 142, 255));")
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.bt_diretorio = QPushButton(self.centralwidget)
        self.bt_diretorio.setObjectName(u"bt_diretorio")
        self.bt_diretorio.setGeometry(QRect(385, 435, 21, 21))
        self.bt_diretorio.setFont(font)
        self.bt_diretorio.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 118, 118, 255), stop:0.988636 rgba(255, 220, 142, 255));\n"
"	Icon: url(:/BTT/icons/abrir.png);\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(43, 25, 62, 255), stop:1 rgba(255, 0, 208, 111));\n"
"}\n"
"QPushButton:pressed {\n"
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
        self.l_selec_pasta.setGeometry(QRect(280, 435, 101, 20))
        self.l_selec_pasta.setFont(font)
        self.l_selec_pasta.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.238636 rgba(43, 25, 62, 255), stop:0.994318 rgba(255, 0, 208, 111));")
        self.bt_salva_pl_personalizada = QPushButton(self.centralwidget)
        self.bt_salva_pl_personalizada.setObjectName(u"bt_salva_pl_personalizada")
        self.bt_salva_pl_personalizada.setGeometry(QRect(385, 410, 21, 20))
        font3 = QFont()
        font3.setFamilies([u"Ink Free"])
        font3.setPointSize(14)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.bt_salva_pl_personalizada.setFont(font3)
        self.bt_salva_pl_personalizada.setStyleSheet(u"QPushButton {\n"
"	icon: url(:/BTT/icons/criar - pl.png);\n"
"	border: 1px solid;\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 118, 118, 255), stop:0.988636 rgba(255, 220, 142, 255));\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(43, 25, 62, 255), stop:1 rgba(255, 0, 208, 111));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	icon: url(:/BTT/icons/criar - pl - press.png);\n"
"	font: 17pt \"Ink Free\";\n"
"	border: 1px solid ;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 0, 0, 164), stop:0.988636 rgba(255, 175, 0, 89));\n"
"}")
        self.bt_salva_pl_personalizada.setIconSize(QSize(20, 20))
        self.cb_lista_playlist = QComboBox(self.centralwidget)
        self.cb_lista_playlist.addItem("")
        self.cb_lista_playlist.setObjectName(u"cb_lista_playlist")
        self.cb_lista_playlist.setGeometry(QRect(0, 0, 131, 22))
        self.cb_lista_playlist.setStyleSheet(u"QComboBox {\n"
"	font: 700 italic 10pt \"Segoe UI\";\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.238636 rgba(43, 25, 62, 255), stop:0.994318 rgba(255, 0, 208, 111));\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.238636 rgba(43, 25, 62, 255), stop:0.994318 rgba(255, 0, 208, 111));\n"
"	border-radius: 6px;\n"
"}\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(175, 0, 63, 20))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgba(255, 170, 255, 130);\n"
"border: 1px solid;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.835227 rgba(255, 118, 118, 255), stop:0.988636 rgba(255, 220, 142, 255));\n"
"border-radius: 8px;")
        self.label_2.setScaledContents(False)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.l_selec_pasta_personalizada = QLabel(self.centralwidget)
        self.l_selec_pasta_personalizada.setObjectName(u"l_selec_pasta_personalizada")
        self.l_selec_pasta_personalizada.setEnabled(True)
        self.l_selec_pasta_personalizada.setGeometry(QRect(291, 415, 91, 14))
        self.l_selec_pasta_personalizada.setFont(font)
        self.l_selec_pasta_personalizada.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.238636 rgba(43, 25, 62, 255), stop:0.994318 rgba(255, 0, 208, 111));")
        MusicPlayer.setCentralWidget(self.centralwidget)

        self.retranslateUi(MusicPlayer)

        self.bt_diretorio.setDefault(False)


        QMetaObject.connectSlotsByName(MusicPlayer)
    # setupUi

    def retranslateUi(self, MusicPlayer):
        MusicPlayer.setWindowTitle(QCoreApplication.translate("MusicPlayer", u"MPV", None))
        self.bt_anterior.setText("")
        self.bt_proximo.setText("")
        self.bt_sair.setText("")
        self.bt_minimizar.setText("")
        self.label.setText(QCoreApplication.translate("MusicPlayer", u"<html><head/><body><p>Cr\u00e9ditos: <a href=\"https://icons8.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Icons8</span></a></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.bt_diretorio.setToolTip(QCoreApplication.translate("MusicPlayer", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; font-style:italic; color:#201b2c;\">Selecionar um Diret\u00f3rio</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.l_selec_pasta.setText(QCoreApplication.translate("MusicPlayer", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700; font-style:italic; color:#ffffff;\">Play List padr\u00e3o  -&gt;</span></p></body></html>", None))
        self.bt_salva_pl_personalizada.setText("")
        self.cb_lista_playlist.setItemText(0, QCoreApplication.translate("MusicPlayer", u"playlist.MPVlist", None))

        self.cb_lista_playlist.setCurrentText(QCoreApplication.translate("MusicPlayer", u"playlist.MPVlist", None))
        self.label_2.setText(QCoreApplication.translate("MusicPlayer", u"<html><head/><body><p><span style=\" font-style:italic;\">GitHub: </span><a href=\"https://github.com/Classic1912/Reprodutor-de-Musica-Pyside6\"><span style=\" font-size:11pt; font-style:italic; text-decoration: underline; color:#0000ff;\">V</span></a></p></body></html>", None))
        self.l_selec_pasta_personalizada.setText(QCoreApplication.translate("MusicPlayer", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:700; font-style:italic; color:#ffffff;\">Nova Play List-&gt;</span></p></body></html>", None))
    # retranslateUi

