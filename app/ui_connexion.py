# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connexionkoGcTo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_connexion(object):
    def setupUi(self, connexion):
        if not connexion.objectName():
            connexion.setObjectName(u"connexion")
        connexion.setEnabled(True)
        connexion.resize(778, 778)
        connexion.setMinimumSize(QSize(778, 778))
        connexion.setMaximumSize(QSize(778, 778))
        connexion.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u"image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        connexion.setWindowIcon(icon)
        connexion.setStyleSheet(u"QWidget {\n"
"  background-color: #fff;\n"
"}\n"
"")
        self.label = QLabel(connexion)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(7, 7, 760, 760))
        self.label.setPixmap(QPixmap(u"image/bg.jpeg"))
        self.stackedWidget = QStackedWidget(connexion)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(195, 195, 393, 380))
        self.stackedWidget.setStyleSheet(u"*{\n"
"	background-color:rgba(255,255,255,50);\n"
"}\n"
"QWidget{\n"
"	border-radius:20px;\n"
"}\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"border-radius:20px;")
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.page_connexion = QFrame(self.page)
        self.page_connexion.setObjectName(u"page_connexion")
        self.page_connexion.setMinimumSize(QSize(380, 380))
        self.page_connexion.setStyleSheet(u"*{\n"
"	background-color:rgba(255,255,255,200);\n"
"}\n"
"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #176B87;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #64CCC5;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}\n"
"")
        self.page_connexion.setFrameShape(QFrame.StyledPanel)
        self.page_connexion.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.page_connexion)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.page_connexion)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color:transparent;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_inscription = QPushButton(self.frame_6)
        self.btn_inscription.setObjectName(u"btn_inscription")
        self.btn_inscription.setMinimumSize(QSize(100, 0))
        self.btn_inscription.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.btn_inscription.setFont(font)
        self.btn_inscription.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_inscription.setStyleSheet(u"color:#176B87;\n"
"")
        self.btn_inscription.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_inscription, 0, Qt.AlignRight)

        self.lb_titre = QLabel(self.frame_6)
        self.lb_titre.setObjectName(u"lb_titre")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(22)
        self.lb_titre.setFont(font1)
        self.lb_titre.setStyleSheet(u"background-color:transparent;\n"
"")
        self.lb_titre.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_titre)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_3 = QFrame(self.page_connexion)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color:transparent;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 12, -1)
        self.lb_utilisateur = QLabel(self.frame_3)
        self.lb_utilisateur.setObjectName(u"lb_utilisateur")
        self.lb_utilisateur.setMinimumSize(QSize(38, 0))
        self.lb_utilisateur.setMaximumSize(QSize(36, 16777215))
        self.lb_utilisateur.setPixmap(QPixmap(u"image/user.png"))

        self.horizontalLayout.addWidget(self.lb_utilisateur)

        self.ln_email = QLineEdit(self.frame_3)
        self.ln_email.setObjectName(u"ln_email")
        self.ln_email.setMinimumSize(QSize(334, 0))
        self.ln_email.setMaximumSize(QSize(334, 16777215))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(10)
        self.ln_email.setFont(font2)

        self.horizontalLayout.addWidget(self.ln_email)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.page_connexion)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(380, 380))
        self.frame_4.setStyleSheet(u"background-color:transparent;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 0, -1)
        self.lb_mot_de_passe = QLabel(self.frame_4)
        self.lb_mot_de_passe.setObjectName(u"lb_mot_de_passe")
        self.lb_mot_de_passe.setPixmap(QPixmap(u"image/password.png"))

        self.horizontalLayout_2.addWidget(self.lb_mot_de_passe, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:transparent;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 30)
        self.ln_mot_de_passe = QLineEdit(self.frame_2)
        self.ln_mot_de_passe.setObjectName(u"ln_mot_de_passe")
        self.ln_mot_de_passe.setFont(font2)

        self.verticalLayout.addWidget(self.ln_mot_de_passe, 0, Qt.AlignTop)

        self.ch_voir_page_connexion = QCheckBox(self.frame_2)
        self.ch_voir_page_connexion.setObjectName(u"ch_voir_page_connexion")
        self.ch_voir_page_connexion.setFont(font2)
        self.ch_voir_page_connexion.setCursor(QCursor(Qt.PointingHandCursor))
        self.ch_voir_page_connexion.setStyleSheet(u"")
        self.ch_voir_page_connexion.setChecked(False)

        self.verticalLayout.addWidget(self.ch_voir_page_connexion)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.page_connexion)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color:transparent;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_connexion = QPushButton(self.frame_5)
        self.btn_connexion.setObjectName(u"btn_connexion")
        self.btn_connexion.setMinimumSize(QSize(100, 0))
        self.btn_connexion.setMaximumSize(QSize(170, 16777215))
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_connexion.setFont(font3)
        self.btn_connexion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_connexion.setStyleSheet(u"QPushButton {\n"
"  background-color: #fff;\n"
"  color: #176B87;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #0d6efd;\n"
"  padding: 5px 15px;\n"
"  margin-top: 10px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color: #176B87;\n"
"  border: 3px solid #176B87;\n"
" color: #fff;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.btn_connexion, 0, Qt.AlignHCenter)

        self.btn_mot_de_passe_oublier = QPushButton(self.frame_5)
        self.btn_mot_de_passe_oublier.setObjectName(u"btn_mot_de_passe_oublier")
        self.btn_mot_de_passe_oublier.setMaximumSize(QSize(130, 13))
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setBold(True)
        font4.setUnderline(True)
        font4.setWeight(75)
        self.btn_mot_de_passe_oublier.setFont(font4)
        self.btn_mot_de_passe_oublier.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_mot_de_passe_oublier.setStyleSheet(u"color:#176B87;")
        self.btn_mot_de_passe_oublier.setFlat(True)

        self.verticalLayout_2.addWidget(self.btn_mot_de_passe_oublier, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.page_connexion)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_11 = QVBoxLayout(self.page_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.page_inscription = QFrame(self.page_2)
        self.page_inscription.setObjectName(u"page_inscription")
        self.page_inscription.setStyleSheet(u"*{\n"
"	background-color:rgba(255,255,255,100);\n"
"}\n"
"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #176B87;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #64CCC5;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.page_inscription.setFrameShape(QFrame.StyledPanel)
        self.page_inscription.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.page_inscription)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_2 = QLabel(self.page_inscription)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_14.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.ln_nom = QLineEdit(self.page_inscription)
        self.ln_nom.setObjectName(u"ln_nom")
        self.ln_nom.setFont(font2)

        self.verticalLayout_14.addWidget(self.ln_nom)

        self.ln_post_nom = QLineEdit(self.page_inscription)
        self.ln_post_nom.setObjectName(u"ln_post_nom")
        self.ln_post_nom.setFont(font2)

        self.verticalLayout_14.addWidget(self.ln_post_nom)

        self.ln_email_page2 = QLineEdit(self.page_inscription)
        self.ln_email_page2.setObjectName(u"ln_email_page2")
        self.ln_email_page2.setFont(font2)

        self.verticalLayout_14.addWidget(self.ln_email_page2)

        self.ln_mot_de_passe_page2 = QLineEdit(self.page_inscription)
        self.ln_mot_de_passe_page2.setObjectName(u"ln_mot_de_passe_page2")
        self.ln_mot_de_passe_page2.setFont(font2)

        self.verticalLayout_14.addWidget(self.ln_mot_de_passe_page2)

        self.ln_confirmer_mot_de_passe_page2 = QLineEdit(self.page_inscription)
        self.ln_confirmer_mot_de_passe_page2.setObjectName(u"ln_confirmer_mot_de_passe_page2")
        self.ln_confirmer_mot_de_passe_page2.setFont(font2)

        self.verticalLayout_14.addWidget(self.ln_confirmer_mot_de_passe_page2)

        self.ch_voir_page_inscription = QCheckBox(self.page_inscription)
        self.ch_voir_page_inscription.setObjectName(u"ch_voir_page_inscription")
        self.ch_voir_page_inscription.setFont(font2)
        self.ch_voir_page_inscription.setCursor(QCursor(Qt.PointingHandCursor))
        self.ch_voir_page_inscription.setStyleSheet(u"background-color:transparent;\n"
"")

        self.verticalLayout_14.addWidget(self.ch_voir_page_inscription)

        self.btn_inscription_page2 = QPushButton(self.page_inscription)
        self.btn_inscription_page2.setObjectName(u"btn_inscription_page2")
        self.btn_inscription_page2.setMinimumSize(QSize(100, 0))
        self.btn_inscription_page2.setMaximumSize(QSize(100, 16777215))
        self.btn_inscription_page2.setFont(font3)
        self.btn_inscription_page2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_inscription_page2.setStyleSheet(u"QPushButton {\n"
"  background-color: #fff;\n"
"  color: #176B87;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #0d6efd;\n"
"  padding: 5px 15px;\n"
"  margin-top: 10px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color: #176B87;\n"
"  border: 3px solid #176B87;\n"
" color: #fff;\n"
"}\n"
"")

        self.verticalLayout_14.addWidget(self.btn_inscription_page2, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.page_inscription)

        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_12 = QVBoxLayout(self.page_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.page_reinitialiser = QFrame(self.page_5)
        self.page_reinitialiser.setObjectName(u"page_reinitialiser")
        self.page_reinitialiser.setStyleSheet(u"*{\n"
"	background-color:rgba(255,255,255,100);\n"
"}\n"
"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #176B87;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #64CCC5;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.page_reinitialiser.setFrameShape(QFrame.StyledPanel)
        self.page_reinitialiser.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.page_reinitialiser)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_4 = QLabel(self.page_reinitialiser)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setFamily(u"Calibri")
        font5.setPointSize(20)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_13.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.ln_email_page3 = QLineEdit(self.page_reinitialiser)
        self.ln_email_page3.setObjectName(u"ln_email_page3")
        self.ln_email_page3.setFont(font2)

        self.verticalLayout_13.addWidget(self.ln_email_page3)

        self.ln_nouveau_mot_de_passe = QLineEdit(self.page_reinitialiser)
        self.ln_nouveau_mot_de_passe.setObjectName(u"ln_nouveau_mot_de_passe")
        self.ln_nouveau_mot_de_passe.setFont(font2)

        self.verticalLayout_13.addWidget(self.ln_nouveau_mot_de_passe)

        self.ln_confirmer_mot_de_passe_page3 = QLineEdit(self.page_reinitialiser)
        self.ln_confirmer_mot_de_passe_page3.setObjectName(u"ln_confirmer_mot_de_passe_page3")
        self.ln_confirmer_mot_de_passe_page3.setFont(font2)

        self.verticalLayout_13.addWidget(self.ln_confirmer_mot_de_passe_page3)

        self.ch_voir_page_reinitialiser = QCheckBox(self.page_reinitialiser)
        self.ch_voir_page_reinitialiser.setObjectName(u"ch_voir_page_reinitialiser")
        self.ch_voir_page_reinitialiser.setCursor(QCursor(Qt.PointingHandCursor))
        self.ch_voir_page_reinitialiser.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_13.addWidget(self.ch_voir_page_reinitialiser)

        self.frame = QFrame(self.page_reinitialiser)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(150, 50))
        self.frame.setStyleSheet(u"background-color:transparent;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.btn_confirmer = QPushButton(self.frame)
        self.btn_confirmer.setObjectName(u"btn_confirmer")
        self.btn_confirmer.setMinimumSize(QSize(100, 0))
        self.btn_confirmer.setMaximumSize(QSize(150, 35))
        self.btn_confirmer.setFont(font3)
        self.btn_confirmer.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_confirmer.setToolTipDuration(9)
        self.btn_confirmer.setStyleSheet(u"QPushButton {\n"
"  background-color: #fff;\n"
"  color: #176B87;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #0d6efd;\n"
"  padding: 5px 15px;\n"
"  margin-top: 10px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color: #176B87;\n"
"  border: 3px solid #176B87;\n"
" color: #fff;\n"
"}\n"
"")

        self.verticalLayout_15.addWidget(self.btn_confirmer)


        self.verticalLayout_13.addWidget(self.frame, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.page_reinitialiser)

        self.stackedWidget.addWidget(self.page_5)

        self.retranslateUi(connexion)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(connexion)
    # setupUi

    def retranslateUi(self, connexion):
        connexion.setWindowTitle(QCoreApplication.translate("connexion", u"Connexion", None))
        self.label.setText("")
        self.btn_inscription.setText(QCoreApplication.translate("connexion", u"inscription", None))
        self.lb_titre.setText(QCoreApplication.translate("connexion", u"SE CONNECTER", None))
        self.lb_utilisateur.setText("")
        self.ln_email.setPlaceholderText(QCoreApplication.translate("connexion", u"Email", None))
        self.lb_mot_de_passe.setText("")
        self.ln_mot_de_passe.setPlaceholderText(QCoreApplication.translate("connexion", u"Mot de passe", None))
        self.ch_voir_page_connexion.setText(QCoreApplication.translate("connexion", u"voir mot de passe", None))
        self.btn_connexion.setText(QCoreApplication.translate("connexion", u"connexion", None))
        self.btn_mot_de_passe_oublier.setText(QCoreApplication.translate("connexion", u"mot de passe oublier?", None))
        self.label_2.setText(QCoreApplication.translate("connexion", u"INSCRIPTION", None))
        self.ln_nom.setPlaceholderText(QCoreApplication.translate("connexion", u"Nom", None))
        self.ln_post_nom.setPlaceholderText(QCoreApplication.translate("connexion", u"Post_nom", None))
        self.ln_email_page2.setPlaceholderText(QCoreApplication.translate("connexion", u"Email", None))
        self.ln_mot_de_passe_page2.setPlaceholderText(QCoreApplication.translate("connexion", u"Mot de passe", None))
        self.ln_confirmer_mot_de_passe_page2.setPlaceholderText(QCoreApplication.translate("connexion", u"Confirmer mot de passe", None))
        self.ch_voir_page_inscription.setText(QCoreApplication.translate("connexion", u"voir mot de passe", None))
        self.btn_inscription_page2.setText(QCoreApplication.translate("connexion", u"s'inscrire", None))
        self.label_4.setText(QCoreApplication.translate("connexion", u"REINITIALISER LE MOT DE PASSE", None))
        self.ln_email_page3.setPlaceholderText(QCoreApplication.translate("connexion", u"Email", None))
        self.ln_nouveau_mot_de_passe.setPlaceholderText(QCoreApplication.translate("connexion", u"Nouveau mot de passe", None))
        self.ln_confirmer_mot_de_passe_page3.setPlaceholderText(QCoreApplication.translate("connexion", u"Confirmer mot de passe", None))
        self.ch_voir_page_reinitialiser.setText(QCoreApplication.translate("connexion", u"voir mot de passe", None))
        self.btn_confirmer.setText(QCoreApplication.translate("connexion", u"Confirmer", None))
    # retranslateUi

