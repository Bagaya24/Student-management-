# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fenetre_principalejbSpth.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icon_rc

class Ui_Gestion_des_etudiants(object):
    def setupUi(self, Gestion_des_etudiants):
        if not Gestion_des_etudiants.objectName():
            Gestion_des_etudiants.setObjectName(u"Gestion_des_etudiants")
        Gestion_des_etudiants.resize(1300, 700)
        Gestion_des_etudiants.setMinimumSize(QSize(0, 600))
        icon = QIcon()
        icon.addFile(u"../../../../.designer/backup/image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Gestion_des_etudiants.setWindowIcon(icon)
        self.centralwidget = QWidget(Gestion_des_etudiants)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	background-color:transparent;\n"
"	color:#fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color:#04364A;\n"
"}\n"
"\n"
"#menu_btn{\n"
"	background-color:#176B87;\n"
"	border-radius: 24px;\n"
"\n"
"}\n"
"#page_ajouter{\n"
"	background-color:#176B87;\n"
"}\n"
"#page_effacer{\n"
"	background-color:#176B87;\n"
"}\n"
"#page_maj{\n"
"	background-color:#176B87;\n"
"}\n"
"#page_voir{\n"
"	background-color:#176B87;\n"
"}\n"
"#page_voir_2{\n"
"	background-color:#176B87;\n"
"}\n"
"#page_trier{\n"
"	background-color:#176B87;\n"
"}\n"
"QComboBox{\n"
"	border: 1px solid #e0e4e7;\n"
"	border-radius: 8px;\n"
"	paddiing-leftl: 10px;\n"
"	height: 25px\n"
"}\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"	width: 12px;\n"
"	height: 12px;\n"
"	margin-right: 15px;\n"
"}\n"
"QComboBox::on{\n"
"	border:2px solid #64CCC5;\n"
"}\n"
"QComboBox QListView{\n"
"	font-size: 12px;\n"
"	border: 1px solid rgba(0,0,0,10%);\n"
"	padding: 5px;\n"
"	background-color:#04364A;\n"
"}\n"
"QComboBox QListView::it"
                        "em{\n"
"	padding-left: 10px;\n"
"	background-color:#fff;\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"	background-color:#04364A;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"	background-color:#04364A;\n"
"}\n"
"QDateEdit{\n"
"	height: 25px;\n"
"	border: 1px solid #e0e4e7;\n"
"	border-radius: 8px\n"
"}\n"
"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #64CCC5;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}\n"
"QPushButton {\n"
"  background-color: #176B87;\n"
"  color: #fff;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #0d6efd;\n"
"  padding: 5px 15px;\n"
"  margin-top: 10px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color: #64CCC5;\n"
"  border: 3px solid #64CCC5;\n"
"}\n"
"QTableWidget {\n"
"        background-color: #f2f2f2;\n"
"        border-radius: 10px;\n"
"        padding: 10px;\n"
"    }\n"
"QTableWidget"
                        "::item {\n"
"        color: #04364A;\n"
"        background-color: #f2f2f2;\n"
"    }\n"
"QTableWidget::item:selected {\n"
"        background-color: #0078d7;\n"
"        color: #fff;\n"
"    }\n"
"QHeaderView::section{\n"
"	color:#04364A;\n"
"	padding:4px;\n"
"	boder:none;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #f2f2f2;\n"
"    height: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #176B87;\n"
"    min-width: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f2f2f2;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical"
                        " {\n"
"    background: #176B87;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"#stackedWidget{\n"
"	border-radius: 24px;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.menu_haut = QWidget(self.centralwidget)
        self.menu_haut.setObjectName(u"menu_haut")
        self.menu_haut.setMinimumSize(QSize(0, 80))
        self.menu_haut.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_2 = QHBoxLayout(self.menu_haut)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_2 = QWidget(self.menu_haut)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.widget_2)


        self.gridLayout.addWidget(self.menu_haut, 0, 0, 1, 1)

        self.menu_bas = QWidget(self.centralwidget)
        self.menu_bas.setObjectName(u"menu_bas")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menu_bas.sizePolicy().hasHeightForWidth())
        self.menu_bas.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.menu_bas)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QWidget(self.menu_bas)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setMinimumSize(QSize(18, 0))
        self.menu_btn.setMaximumSize(QSize(60, 16777215))
        self.verticalLayout = QVBoxLayout(self.menu_btn)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_menu = QPushButton(self.menu_btn)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu.setStyleSheet(u"QPushButton{\n"
"	border:none\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color:#176B87;\n"
"  border:2px solid #64CCC5;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icones/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon1)
        self.btn_menu.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_menu)

        self.btn_afficher_menu = QPushButton(self.menu_btn)
        self.btn_afficher_menu.setObjectName(u"btn_afficher_menu")
        self.btn_afficher_menu.setEnabled(False)
        self.btn_afficher_menu.setMaximumSize(QSize(100000, 40))
        self.btn_afficher_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_afficher_menu.setStyleSheet(u"QPushButton{\n"
"	border:none\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color:#176B87;\n"
"  border:2px solid #64CCC5;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icones/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_afficher_menu.setIcon(icon2)
        self.btn_afficher_menu.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_afficher_menu)

        self.btn_ajouter = QPushButton(self.menu_btn)
        self.btn_ajouter.setObjectName(u"btn_ajouter")
        self.btn_ajouter.setEnabled(False)
        self.btn_ajouter.setMaximumSize(QSize(16777215, 40))
        self.btn_ajouter.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajouter.setStyleSheet(u"QPushButton{\n"
"	border:none\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color:#176B87;\n"
"  border:2px solid #64CCC5;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icones/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ajouter.setIcon(icon3)
        self.btn_ajouter.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.btn_ajouter)

        self.btn_effacer = QPushButton(self.menu_btn)
        self.btn_effacer.setObjectName(u"btn_effacer")
        self.btn_effacer.setEnabled(False)
        self.btn_effacer.setMaximumSize(QSize(16777215, 40))
        self.btn_effacer.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_effacer.setStyleSheet(u"QPushButton{\n"
"	border:none\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color:#176B87;\n"
"  border:2px solid #64CCC5;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icones/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_effacer.setIcon(icon4)

        self.verticalLayout.addWidget(self.btn_effacer)

        self.btn_maj = QPushButton(self.menu_btn)
        self.btn_maj.setObjectName(u"btn_maj")
        self.btn_maj.setEnabled(False)
        self.btn_maj.setMinimumSize(QSize(0, 0))
        self.btn_maj.setMaximumSize(QSize(1000, 40))
        self.btn_maj.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_maj.setStyleSheet(u"QPushButton{\n"
"	border:none\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color:#176B87;\n"
"  border:2px solid #64CCC5;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icones/edit-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maj.setIcon(icon5)

        self.verticalLayout.addWidget(self.btn_maj)

        self.btn_chercher = QPushButton(self.menu_btn)
        self.btn_chercher.setObjectName(u"btn_chercher")
        self.btn_chercher.setEnabled(False)
        self.btn_chercher.setMaximumSize(QSize(16777215, 40))
        self.btn_chercher.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_chercher.setStyleSheet(u"QPushButton{\n"
"	border:none\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color:#176B87;\n"
"  border:2px solid #64CCC5;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icones/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_chercher.setIcon(icon6)

        self.verticalLayout.addWidget(self.btn_chercher)

        self.btn_trier = QPushButton(self.menu_btn)
        self.btn_trier.setObjectName(u"btn_trier")
        self.btn_trier.setEnabled(False)
        self.btn_trier.setStyleSheet(u"QPushButton{\n"
"	border:none\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color:#176B87;\n"
"  border:2px solid #64CCC5;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icones/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_trier.setIcon(icon7)

        self.verticalLayout.addWidget(self.btn_trier)

        self.btn_quitter = QPushButton(self.menu_btn)
        self.btn_quitter.setObjectName(u"btn_quitter")
        self.btn_quitter.setEnabled(True)
        self.btn_quitter.setMaximumSize(QSize(16777215, 40))
        self.btn_quitter.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_quitter.setStyleSheet(u"QPushButton{\n"
"	border:none\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color:#176B87;\n"
"  border:2px solid #64CCC5;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icones/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_quitter.setIcon(icon8)

        self.verticalLayout.addWidget(self.btn_quitter)


        self.horizontalLayout.addWidget(self.menu_btn)

        self.menu_pages = QWidget(self.menu_bas)
        self.menu_pages.setObjectName(u"menu_pages")
        self.menu_pages.setMinimumSize(QSize(0, 0))
        self.menu_pages.setMaximumSize(QSize(0, 16777215))
        self.menu_pages.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.menu_pages)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.menu_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(300, 0))
        self.stackedWidget.setMaximumSize(QSize(300, 16777215))
        self.stackedWidget.setStyleSheet(u"")
        self.page_ajouter = QWidget()
        self.page_ajouter.setObjectName(u"page_ajouter")
        self.verticalLayout_5 = QVBoxLayout(self.page_ajouter)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ln_ajouter_matricule = QLineEdit(self.page_ajouter)
        self.ln_ajouter_matricule.setObjectName(u"ln_ajouter_matricule")

        self.verticalLayout_5.addWidget(self.ln_ajouter_matricule)

        self.ln_ajouter_nom = QLineEdit(self.page_ajouter)
        self.ln_ajouter_nom.setObjectName(u"ln_ajouter_nom")

        self.verticalLayout_5.addWidget(self.ln_ajouter_nom)

        self.cb_ajouter_faculte = QComboBox(self.page_ajouter)
        self.cb_ajouter_faculte.addItem("")
        self.cb_ajouter_faculte.addItem("")
        self.cb_ajouter_faculte.addItem("")
        self.cb_ajouter_faculte.addItem("")
        self.cb_ajouter_faculte.addItem("")
        self.cb_ajouter_faculte.addItem("")
        self.cb_ajouter_faculte.addItem("")
        self.cb_ajouter_faculte.setObjectName(u"cb_ajouter_faculte")
        self.cb_ajouter_faculte.setDuplicatesEnabled(False)

        self.verticalLayout_5.addWidget(self.cb_ajouter_faculte)

        self.cb_ajouter_promotion = QComboBox(self.page_ajouter)
        self.cb_ajouter_promotion.setObjectName(u"cb_ajouter_promotion")
        self.cb_ajouter_promotion.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_ajouter_promotion.setEditable(False)
        self.cb_ajouter_promotion.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.verticalLayout_5.addWidget(self.cb_ajouter_promotion)

        self.cb_ajouter_filiere = QComboBox(self.page_ajouter)
        self.cb_ajouter_filiere.setObjectName(u"cb_ajouter_filiere")
        self.cb_ajouter_filiere.setDuplicatesEnabled(False)

        self.verticalLayout_5.addWidget(self.cb_ajouter_filiere)

        self.ln_ajouter_email = QLineEdit(self.page_ajouter)
        self.ln_ajouter_email.setObjectName(u"ln_ajouter_email")

        self.verticalLayout_5.addWidget(self.ln_ajouter_email)

        self.ln_ajouter_telephone = QLineEdit(self.page_ajouter)
        self.ln_ajouter_telephone.setObjectName(u"ln_ajouter_telephone")

        self.verticalLayout_5.addWidget(self.ln_ajouter_telephone)

        self.ln_ajouter_adresse = QLineEdit(self.page_ajouter)
        self.ln_ajouter_adresse.setObjectName(u"ln_ajouter_adresse")

        self.verticalLayout_5.addWidget(self.ln_ajouter_adresse)

        self.cb_ajouter_sexe = QComboBox(self.page_ajouter)
        self.cb_ajouter_sexe.addItem("")
        self.cb_ajouter_sexe.addItem("")
        self.cb_ajouter_sexe.setObjectName(u"cb_ajouter_sexe")
        self.cb_ajouter_sexe.setEditable(False)

        self.verticalLayout_5.addWidget(self.cb_ajouter_sexe)

        self.ajouter_date_de_naissance = QDateEdit(self.page_ajouter)
        self.ajouter_date_de_naissance.setObjectName(u"ajouter_date_de_naissance")

        self.verticalLayout_5.addWidget(self.ajouter_date_de_naissance)

        self.ajouter_annee_inscruption = QDateEdit(self.page_ajouter)
        self.ajouter_annee_inscruption.setObjectName(u"ajouter_annee_inscruption")

        self.verticalLayout_5.addWidget(self.ajouter_annee_inscruption)

        self.btn_enregistrer = QPushButton(self.page_ajouter)
        self.btn_enregistrer.setObjectName(u"btn_enregistrer")
        self.btn_enregistrer.setMinimumSize(QSize(100, 0))
        self.btn_enregistrer.setMaximumSize(QSize(125, 16777215))
        self.btn_enregistrer.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_enregistrer, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_ajouter)
        self.page_effacer = QWidget()
        self.page_effacer.setObjectName(u"page_effacer")
        self.verticalLayout_6 = QVBoxLayout(self.page_effacer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ln_supprimer_matricule = QLineEdit(self.page_effacer)
        self.ln_supprimer_matricule.setObjectName(u"ln_supprimer_matricule")

        self.verticalLayout_6.addWidget(self.ln_supprimer_matricule)

        self.ln_supprimer_nom = QLineEdit(self.page_effacer)
        self.ln_supprimer_nom.setObjectName(u"ln_supprimer_nom")

        self.verticalLayout_6.addWidget(self.ln_supprimer_nom)

        self.widget = QWidget(self.page_effacer)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_effacer_chercher = QPushButton(self.widget)
        self.btn_effacer_chercher.setObjectName(u"btn_effacer_chercher")

        self.horizontalLayout_6.addWidget(self.btn_effacer_chercher)

        self.btn_supprimer = QPushButton(self.widget)
        self.btn_supprimer.setObjectName(u"btn_supprimer")
        self.btn_supprimer.setMinimumSize(QSize(0, 30))
        self.btn_supprimer.setMaximumSize(QSize(1234, 16777215))
        self.btn_supprimer.setAutoDefault(False)

        self.horizontalLayout_6.addWidget(self.btn_supprimer)


        self.verticalLayout_6.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page_effacer)
        self.page_maj = QWidget()
        self.page_maj.setObjectName(u"page_maj")
        self.verticalLayout_7 = QVBoxLayout(self.page_maj)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.ln_maj_matricule = QLineEdit(self.page_maj)
        self.ln_maj_matricule.setObjectName(u"ln_maj_matricule")

        self.verticalLayout_7.addWidget(self.ln_maj_matricule)

        self.ln_maj_nom = QLineEdit(self.page_maj)
        self.ln_maj_nom.setObjectName(u"ln_maj_nom")

        self.verticalLayout_7.addWidget(self.ln_maj_nom)

        self.cb_maj_faculte = QComboBox(self.page_maj)
        self.cb_maj_faculte.addItem("")
        self.cb_maj_faculte.addItem("")
        self.cb_maj_faculte.addItem("")
        self.cb_maj_faculte.addItem("")
        self.cb_maj_faculte.addItem("")
        self.cb_maj_faculte.addItem("")
        self.cb_maj_faculte.addItem("")
        self.cb_maj_faculte.setObjectName(u"cb_maj_faculte")

        self.verticalLayout_7.addWidget(self.cb_maj_faculte)

        self.cb_maj_promotion = QComboBox(self.page_maj)
        self.cb_maj_promotion.setObjectName(u"cb_maj_promotion")

        self.verticalLayout_7.addWidget(self.cb_maj_promotion)

        self.cb_maj_filiere = QComboBox(self.page_maj)
        self.cb_maj_filiere.setObjectName(u"cb_maj_filiere")

        self.verticalLayout_7.addWidget(self.cb_maj_filiere)

        self.ln_maj_email = QLineEdit(self.page_maj)
        self.ln_maj_email.setObjectName(u"ln_maj_email")

        self.verticalLayout_7.addWidget(self.ln_maj_email)

        self.ln_maj_telephone = QLineEdit(self.page_maj)
        self.ln_maj_telephone.setObjectName(u"ln_maj_telephone")

        self.verticalLayout_7.addWidget(self.ln_maj_telephone)

        self.ln_maj_adresse = QLineEdit(self.page_maj)
        self.ln_maj_adresse.setObjectName(u"ln_maj_adresse")

        self.verticalLayout_7.addWidget(self.ln_maj_adresse)

        self.cb_maj_sexe = QComboBox(self.page_maj)
        self.cb_maj_sexe.addItem("")
        self.cb_maj_sexe.addItem("")
        self.cb_maj_sexe.setObjectName(u"cb_maj_sexe")

        self.verticalLayout_7.addWidget(self.cb_maj_sexe)

        self.maj_date_de_naissance = QDateEdit(self.page_maj)
        self.maj_date_de_naissance.setObjectName(u"maj_date_de_naissance")

        self.verticalLayout_7.addWidget(self.maj_date_de_naissance)

        self.maj_annee_inscruption = QDateEdit(self.page_maj)
        self.maj_annee_inscruption.setObjectName(u"maj_annee_inscruption")

        self.verticalLayout_7.addWidget(self.maj_annee_inscruption)

        self.btn_maj_2 = QPushButton(self.page_maj)
        self.btn_maj_2.setObjectName(u"btn_maj_2")
        self.btn_maj_2.setMinimumSize(QSize(130, 0))
        self.btn_maj_2.setMaximumSize(QSize(130, 16777215))

        self.verticalLayout_7.addWidget(self.btn_maj_2, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_maj)
        self.page_voir = QWidget()
        self.page_voir.setObjectName(u"page_voir")
        self.verticalLayout_8 = QVBoxLayout(self.page_voir)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.ln_chercher_matricule = QLineEdit(self.page_voir)
        self.ln_chercher_matricule.setObjectName(u"ln_chercher_matricule")

        self.verticalLayout_8.addWidget(self.ln_chercher_matricule)

        self.ln_chercher_nom = QLineEdit(self.page_voir)
        self.ln_chercher_nom.setObjectName(u"ln_chercher_nom")

        self.verticalLayout_8.addWidget(self.ln_chercher_nom)

        self.widget_6 = QWidget(self.page_voir)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_voir_checher = QPushButton(self.widget_6)
        self.btn_voir_checher.setObjectName(u"btn_voir_checher")
        self.btn_voir_checher.setMinimumSize(QSize(100, 0))
        self.btn_voir_checher.setMaximumSize(QSize(12345, 16777215))

        self.horizontalLayout_7.addWidget(self.btn_voir_checher)

        self.btn_voir = QPushButton(self.widget_6)
        self.btn_voir.setObjectName(u"btn_voir")
        self.btn_voir.setMinimumSize(QSize(100, 0))
        self.btn_voir.setMaximumSize(QSize(1234, 16777215))

        self.horizontalLayout_7.addWidget(self.btn_voir)


        self.verticalLayout_8.addWidget(self.widget_6)

        self.stackedWidget.addWidget(self.page_voir)
        self.page_trier = QWidget()
        self.page_trier.setObjectName(u"page_trier")
        self.verticalLayout_10 = QVBoxLayout(self.page_trier)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.cb_trie_universite = QComboBox(self.page_trier)
        self.cb_trie_universite.addItem("")
        self.cb_trie_universite.addItem("")
        self.cb_trie_universite.addItem("")
        self.cb_trie_universite.setObjectName(u"cb_trie_universite")

        self.verticalLayout_10.addWidget(self.cb_trie_universite)

        self.cb_trie_faculte = QComboBox(self.page_trier)
        self.cb_trie_faculte.setObjectName(u"cb_trie_faculte")
        self.cb_trie_faculte.setEnabled(False)

        self.verticalLayout_10.addWidget(self.cb_trie_faculte)

        self.cb_trie_promotion = QComboBox(self.page_trier)
        self.cb_trie_promotion.setObjectName(u"cb_trie_promotion")
        self.cb_trie_promotion.setEnabled(False)

        self.verticalLayout_10.addWidget(self.cb_trie_promotion)

        self.cb_trie_filiere = QComboBox(self.page_trier)
        self.cb_trie_filiere.setObjectName(u"cb_trie_filiere")
        self.cb_trie_filiere.setEnabled(False)

        self.verticalLayout_10.addWidget(self.cb_trie_filiere)

        self.frame = QFrame(self.page_trier)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(10000, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_trier_2 = QPushButton(self.frame)
        self.btn_trier_2.setObjectName(u"btn_trier_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_trier_2.sizePolicy().hasHeightForWidth())
        self.btn_trier_2.setSizePolicy(sizePolicy2)
        self.btn_trier_2.setMinimumSize(QSize(100, 0))
        self.btn_trier_2.setMaximumSize(QSize(100, 16777215))
        self.btn_trier_2.setSizeIncrement(QSize(0, 0))
        self.btn_trier_2.setBaseSize(QSize(0, 0))
        self.btn_trier_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.btn_trier_2)


        self.verticalLayout_10.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_trier)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.menu_pages)

        self.widget_5 = QWidget(self.menu_bas)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget_2 = QStackedWidget(self.widget_5)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_tableau = QWidget()
        self.page_tableau.setObjectName(u"page_tableau")
        self.verticalLayout_11 = QVBoxLayout(self.page_tableau)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tableau_etudiant = QTableWidget(self.page_tableau)
        if (self.tableau_etudiant.columnCount() < 11):
            self.tableau_etudiant.setColumnCount(11)
        brush = QBrush(QColor(4, 54, 74, 255))
        brush.setStyle(Qt.SolidPattern)
        font1 = QFont()
        font1.setPointSize(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem.setForeground(brush);
        self.tableau_etudiant.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setForeground(brush);
        self.tableau_etudiant.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font1);
        __qtablewidgetitem2.setForeground(brush);
        self.tableau_etudiant.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setForeground(brush);
        self.tableau_etudiant.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font1);
        __qtablewidgetitem4.setForeground(brush);
        self.tableau_etudiant.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setForeground(brush);
        self.tableau_etudiant.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setForeground(brush);
        self.tableau_etudiant.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setForeground(brush);
        self.tableau_etudiant.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setForeground(brush);
        self.tableau_etudiant.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setForeground(brush);
        self.tableau_etudiant.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setForeground(brush);
        self.tableau_etudiant.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableau_etudiant.setObjectName(u"tableau_etudiant")

        self.verticalLayout_11.addWidget(self.tableau_etudiant)

        self.stackedWidget_2.addWidget(self.page_tableau)
        self.page_voir_2 = QWidget()
        self.page_voir_2.setObjectName(u"page_voir_2")
        self.horizontalLayout_4 = QHBoxLayout(self.page_voir_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_3 = QWidget(self.page_voir_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(300, 0))
        self.widget_3.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.widget_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lb_photo = QLabel(self.widget_3)
        self.lb_photo.setObjectName(u"lb_photo")
        self.lb_photo.setMinimumSize(QSize(282, 400))
        self.lb_photo.setMaximumSize(QSize(282, 400))
        self.lb_photo.setPixmap(QPixmap(u"../../../../.designer/backup/image/_1cebba32-6425-4fa3-b382-d989000d3381.jpeg"))
        self.lb_photo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lb_photo)

        self.lb_matricule = QLabel(self.widget_3)
        self.lb_matricule.setObjectName(u"lb_matricule")
        font2 = QFont()
        font2.setPointSize(17)
        self.lb_matricule.setFont(font2)
        self.lb_matricule.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lb_matricule)


        self.horizontalLayout_4.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.page_voir_2)
        self.widget_4.setObjectName(u"widget_4")
        self.formLayout = QFormLayout(self.widget_4)
        self.formLayout.setObjectName(u"formLayout")
        self.label_20 = QLabel(self.widget_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(150, 50))
        self.label_20.setMaximumSize(QSize(150, 50))
        font3 = QFont()
        font3.setPointSize(13)
        self.label_20.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_20)

        self.lb_noms = QLabel(self.widget_4)
        self.lb_noms.setObjectName(u"lb_noms")
        self.lb_noms.setMinimumSize(QSize(250, 50))
        self.lb_noms.setMaximumSize(QSize(250, 16777215))
        self.lb_noms.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lb_noms)

        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 50))
        self.label.setMaximumSize(QSize(150, 50))
        self.label.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.lb_faculte = QLabel(self.widget_4)
        self.lb_faculte.setObjectName(u"lb_faculte")
        self.lb_faculte.setMinimumSize(QSize(250, 50))
        self.lb_faculte.setMaximumSize(QSize(250, 16777215))
        self.lb_faculte.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lb_faculte)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(150, 50))
        self.label_4.setMaximumSize(QSize(150, 50))
        self.label_4.setFont(font3)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.lb_fliere = QLabel(self.widget_4)
        self.lb_fliere.setObjectName(u"lb_fliere")
        self.lb_fliere.setMinimumSize(QSize(250, 50))
        self.lb_fliere.setMaximumSize(QSize(250, 16777215))
        self.lb_fliere.setFont(font3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lb_fliere)

        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(150, 50))
        self.label_6.setMaximumSize(QSize(150, 50))
        self.label_6.setFont(font3)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.lb_promotion = QLabel(self.widget_4)
        self.lb_promotion.setObjectName(u"lb_promotion")
        self.lb_promotion.setMinimumSize(QSize(250, 50))
        self.lb_promotion.setMaximumSize(QSize(250, 16777215))
        self.lb_promotion.setFont(font3)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lb_promotion)

        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(150, 50))
        self.label_8.setMaximumSize(QSize(150, 50))
        self.label_8.setFont(font3)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_8)

        self.lb_email = QLabel(self.widget_4)
        self.lb_email.setObjectName(u"lb_email")
        self.lb_email.setMinimumSize(QSize(250, 50))
        self.lb_email.setMaximumSize(QSize(250, 16777215))
        self.lb_email.setFont(font3)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lb_email)

        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 50))
        self.label_10.setMaximumSize(QSize(150, 50))
        self.label_10.setFont(font3)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_10)

        self.lb_telephone = QLabel(self.widget_4)
        self.lb_telephone.setObjectName(u"lb_telephone")
        self.lb_telephone.setMinimumSize(QSize(250, 50))
        self.lb_telephone.setMaximumSize(QSize(250, 16777215))
        self.lb_telephone.setFont(font3)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lb_telephone)

        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 50))
        self.label_12.setMaximumSize(QSize(150, 50))
        self.label_12.setFont(font3)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_12)

        self.lb_adresse = QLabel(self.widget_4)
        self.lb_adresse.setObjectName(u"lb_adresse")
        self.lb_adresse.setMinimumSize(QSize(250, 50))
        self.lb_adresse.setMaximumSize(QSize(250, 16777215))
        self.lb_adresse.setFont(font3)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lb_adresse)

        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(150, 50))
        self.label_14.setMaximumSize(QSize(150, 50))
        self.label_14.setFont(font3)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_14)

        self.lb_sexe = QLabel(self.widget_4)
        self.lb_sexe.setObjectName(u"lb_sexe")
        self.lb_sexe.setMinimumSize(QSize(250, 50))
        self.lb_sexe.setMaximumSize(QSize(250, 16777215))
        self.lb_sexe.setFont(font3)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lb_sexe)

        self.label_16 = QLabel(self.widget_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(150, 50))
        self.label_16.setMaximumSize(QSize(150, 50))
        self.label_16.setFont(font3)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_16)

        self.lb_date_de_naissance = QLabel(self.widget_4)
        self.lb_date_de_naissance.setObjectName(u"lb_date_de_naissance")
        self.lb_date_de_naissance.setMinimumSize(QSize(250, 50))
        self.lb_date_de_naissance.setMaximumSize(QSize(250, 16777215))
        self.lb_date_de_naissance.setFont(font3)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lb_date_de_naissance)

        self.label_18 = QLabel(self.widget_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(150, 50))
        self.label_18.setMaximumSize(QSize(150, 50))
        self.label_18.setFont(font3)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_18)

        self.lb_date_inscruption = QLabel(self.widget_4)
        self.lb_date_inscruption.setObjectName(u"lb_date_inscruption")
        self.lb_date_inscruption.setMinimumSize(QSize(250, 50))
        self.lb_date_inscruption.setMaximumSize(QSize(250, 16777215))
        self.lb_date_inscruption.setFont(font3)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.lb_date_inscruption)


        self.horizontalLayout_4.addWidget(self.widget_4)

        self.stackedWidget_2.addWidget(self.page_voir_2)

        self.verticalLayout_3.addWidget(self.stackedWidget_2)


        self.horizontalLayout.addWidget(self.widget_5)


        self.gridLayout.addWidget(self.menu_bas, 1, 0, 1, 1)

        Gestion_des_etudiants.setCentralWidget(self.centralwidget)

        self.retranslateUi(Gestion_des_etudiants)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Gestion_des_etudiants)
    # setupUi

    def retranslateUi(self, Gestion_des_etudiants):
        Gestion_des_etudiants.setWindowTitle(QCoreApplication.translate("Gestion_des_etudiants", u"Gestion des etudiants", None))
        self.label_2.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Systeme de gestion des etudiants", None))
        self.btn_menu.setText("")
        self.btn_afficher_menu.setText("")
        self.btn_ajouter.setText("")
        self.btn_effacer.setText("")
        self.btn_maj.setText("")
        self.btn_chercher.setText("")
        self.btn_trier.setText("")
        self.btn_quitter.setText("")
        self.ln_ajouter_matricule.setPlaceholderText(QCoreApplication.translate("Gestion_des_etudiants", u"Matricule", None))
        self.ln_ajouter_nom.setPlaceholderText(QCoreApplication.translate("Gestion_des_etudiants", u"Noms", None))
        self.cb_ajouter_faculte.setItemText(0, QCoreApplication.translate("Gestion_des_etudiants", u"Economie", None))
        self.cb_ajouter_faculte.setItemText(1, QCoreApplication.translate("Gestion_des_etudiants", u"Droit", None))
        self.cb_ajouter_faculte.setItemText(2, QCoreApplication.translate("Gestion_des_etudiants", u"Medecin", None))
        self.cb_ajouter_faculte.setItemText(3, QCoreApplication.translate("Gestion_des_etudiants", u"Psychologie", None))
        self.cb_ajouter_faculte.setItemText(4, QCoreApplication.translate("Gestion_des_etudiants", u"Theologie", None))
        self.cb_ajouter_faculte.setItemText(5, QCoreApplication.translate("Gestion_des_etudiants", u"Sante publique", None))
        self.cb_ajouter_faculte.setItemText(6, QCoreApplication.translate("Gestion_des_etudiants", u"Science de l'ingenieur", None))

        self.cb_ajouter_faculte.setCurrentText(QCoreApplication.translate("Gestion_des_etudiants", u"Economie", None))
        self.cb_ajouter_faculte.setPlaceholderText("")
        self.cb_ajouter_promotion.setPlaceholderText("")
        self.cb_ajouter_filiere.setCurrentText("")
        self.cb_ajouter_filiere.setPlaceholderText("")
        self.ln_ajouter_email.setPlaceholderText(QCoreApplication.translate("Gestion_des_etudiants", u"Email", None))
        self.ln_ajouter_telephone.setPlaceholderText(QCoreApplication.translate("Gestion_des_etudiants", u"Telephone", None))
        self.ln_ajouter_adresse.setPlaceholderText(QCoreApplication.translate("Gestion_des_etudiants", u"Adresse", None))
        self.cb_ajouter_sexe.setItemText(0, QCoreApplication.translate("Gestion_des_etudiants", u"M", None))
        self.cb_ajouter_sexe.setItemText(1, QCoreApplication.translate("Gestion_des_etudiants", u"F", None))

        self.cb_ajouter_sexe.setPlaceholderText("")
        self.ajouter_annee_inscruption.setDisplayFormat(QCoreApplication.translate("Gestion_des_etudiants", u"yyyy", None))
        self.btn_enregistrer.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Enregistrer", None))
        self.ln_supprimer_matricule.setPlaceholderText(QCoreApplication.translate("Gestion_des_etudiants", u"Matricule", None))
        self.ln_supprimer_nom.setPlaceholderText(QCoreApplication.translate("Gestion_des_etudiants", u"Noms", None))
        self.btn_effacer_chercher.setText(QCoreApplication.translate("Gestion_des_etudiants", u"chercher", None))
        self.btn_supprimer.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Supprimer", None))
        self.ln_maj_matricule.setPlaceholderText(QCoreApplication.translate("Gestion_des_etudiants", u"Matricule", None))
        self.ln_maj_nom.setPlaceholderText(QCoreApplication.translate("Gestion_des_etudiants", u"Noms", None))
        self.cb_maj_faculte.setItemText(0, QCoreApplication.translate("Gestion_des_etudiants", u"Economie", None))
        self.cb_maj_faculte.setItemText(1, QCoreApplication.translate("Gestion_des_etudiants", u"Droit", None))
        self.cb_maj_faculte.setItemText(2, QCoreApplication.translate("Gestion_des_etudiants", u"Medecine", None))
        self.cb_maj_faculte.setItemText(3, QCoreApplication.translate("Gestion_des_etudiants", u"Psychologie", None))
        self.cb_maj_faculte.setItemText(4, QCoreApplication.translate("Gestion_des_etudiants", u"Theologie", None))
        self.cb_maj_faculte.setItemText(5, QCoreApplication.translate("Gestion_des_etudiants", u"Sante publique", None))
        self.cb_maj_faculte.setItemText(6, QCoreApplication.translate("Gestion_des_etudiants", u"Science de l'ingenieur", None))

        self.ln_maj_email.setPlaceholderText(QCoreApplication.translate("Gestion_des_etudiants", u"Email", None))
        self.ln_maj_telephone.setPlaceholderText(QCoreApplication.translate("Gestion_des_etudiants", u"Telephone", None))
        self.ln_maj_adresse.setPlaceholderText(QCoreApplication.translate("Gestion_des_etudiants", u"Adresse", None))
        self.cb_maj_sexe.setItemText(0, QCoreApplication.translate("Gestion_des_etudiants", u"M", None))
        self.cb_maj_sexe.setItemText(1, QCoreApplication.translate("Gestion_des_etudiants", u"F", None))

        self.maj_annee_inscruption.setDisplayFormat(QCoreApplication.translate("Gestion_des_etudiants", u"yyyy", None))
        self.btn_maj_2.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Mettre a jour", None))
        self.ln_chercher_matricule.setPlaceholderText(QCoreApplication.translate("Gestion_des_etudiants", u"Matricule", None))
        self.ln_chercher_nom.setPlaceholderText(QCoreApplication.translate("Gestion_des_etudiants", u"Noms", None))
        self.btn_voir_checher.setText(QCoreApplication.translate("Gestion_des_etudiants", u"chercher", None))
        self.btn_voir.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Voir", None))
        self.cb_trie_universite.setItemText(0, QCoreApplication.translate("Gestion_des_etudiants", u"Toutes les facultees", None))
        self.cb_trie_universite.setItemText(1, QCoreApplication.translate("Gestion_des_etudiants", u"Par facultee", None))
        self.cb_trie_universite.setItemText(2, QCoreApplication.translate("Gestion_des_etudiants", u"Sexe", None))

        self.btn_trier_2.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Trier", None))
        ___qtablewidgetitem = self.tableau_etudiant.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Matricule", None));
        ___qtablewidgetitem1 = self.tableau_etudiant.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Noms", None));
        ___qtablewidgetitem2 = self.tableau_etudiant.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Facultee", None));
        ___qtablewidgetitem3 = self.tableau_etudiant.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Filier", None));
        ___qtablewidgetitem4 = self.tableau_etudiant.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Promotion", None));
        ___qtablewidgetitem5 = self.tableau_etudiant.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Email", None));
        ___qtablewidgetitem6 = self.tableau_etudiant.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Telephone", None));
        ___qtablewidgetitem7 = self.tableau_etudiant.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Sexe", None));
        ___qtablewidgetitem8 = self.tableau_etudiant.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Adresse", None));
        ___qtablewidgetitem9 = self.tableau_etudiant.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Annee de naiss.", None));
        ___qtablewidgetitem10 = self.tableau_etudiant.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Annee de l'inscru.", None));
        self.lb_photo.setText("")
        self.lb_matricule.setText(QCoreApplication.translate("Gestion_des_etudiants", u"17480", None))
        self.label_20.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Noms :", None))
        self.lb_noms.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Bagaya Fazili Glody", None))
        self.label.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Facultee :", None))
        self.lb_faculte.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Science de l'ingenieur", None))
        self.label_4.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Filiere :", None))
        self.lb_fliere.setText(QCoreApplication.translate("Gestion_des_etudiants", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Promotion :", None))
        self.lb_promotion.setText(QCoreApplication.translate("Gestion_des_etudiants", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Email: ", None))
        self.lb_email.setText(QCoreApplication.translate("Gestion_des_etudiants", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Telephone: ", None))
        self.lb_telephone.setText(QCoreApplication.translate("Gestion_des_etudiants", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Adresse :", None))
        self.lb_adresse.setText(QCoreApplication.translate("Gestion_des_etudiants", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Sexe :", None))
        self.lb_sexe.setText(QCoreApplication.translate("Gestion_des_etudiants", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Date de naissance :", None))
        self.lb_date_de_naissance.setText(QCoreApplication.translate("Gestion_des_etudiants", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("Gestion_des_etudiants", u"Date d'inscruption :", None))
        self.lb_date_inscruption.setText(QCoreApplication.translate("Gestion_des_etudiants", u"TextLabel", None))
    # retranslateUi

