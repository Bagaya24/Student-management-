from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(950, 700)
        font = QFont()
        font.setFamily(u"Calibri Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"""
                    QWidget {
                             background-color: #fff;
                             color: #363062;
                             }""")
        MainWindow.setIconSize(QSize(10, 10))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableau_etudiant = QTableWidget(self.centralwidget)
        if (self.tableau_etudiant.columnCount() < 7):
            self.tableau_etudiant.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem.setBackground(QColor(255, 255, 255))
        self.tableau_etudiant.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font1 = QFont()
        font1.setPointSize(8)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem1.setFont(font1)
        self.tableau_etudiant.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter)
        self.tableau_etudiant.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter)
        self.tableau_etudiant.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter)
        self.tableau_etudiant.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter)
        self.tableau_etudiant.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter)
        self.tableau_etudiant.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableau_etudiant.setObjectName(u"tableau_etudiant")
        self.tableau_etudiant.setGeometry(QRect(180, 120, 741, 521))
        self.tableau_etudiant.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tableau_etudiant.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
                                            "    border-top: 2px solid #C2C7CB;\n"
                                            "    position: absolute;\n"
                                            "    top: -0.5em;\n"
                                            "}\n"
                                            "\n"
                                            "QTabWidget::tab-bar {\n"
                                            "    alignment: center;\n"
                                            "}\n"
                                            "\n"
                                            "/* Style the tab using the tab sub-control. Note that\n"
                                            "    it reads QTabBar _not_ QTabWidget */\n"
                                            "QTabBar::tab {\n"
                                            "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                            "                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
                                            "                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
                                            "    border: 2px solid #C4C4C3;\n"
                                            "    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
                                            "    border-top-left-radius: 4px;\n"
                                            "    border-top-right-radius: 4px;\n"
                                            "    min-width: 8ex;\n"
                                            "    padding: 2px;\n"
                                            "}")
        self.lb_titre = QLabel(self.centralwidget)
        self.lb_titre.setObjectName(u"lb_titre")
        self.lb_titre.setGeometry(QRect(240, 20, 531, 61))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(28)
        font2.setBold(False)
        font2.setWeight(50)
        self.lb_titre.setFont(font2)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 200, 143, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_connexion = QPushButton(self.verticalLayoutWidget)
        self.btn_connexion.setObjectName(u"btn_connexion")
        self.btn_connexion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_connexion.setStyleSheet(u"QPushButton {\n"
                                         "  background-color: #0d6efd;\n"
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
                                         "  background-color:#fff;\n"
                                         "  color: #0d6efd;\n"
                                         "  border: 1px solid #9ac3fe;\n"
                                         "}")

        self.verticalLayout.addWidget(self.btn_connexion)

        self.btn_ajouter = QPushButton(self.verticalLayoutWidget)
        self.btn_ajouter.setObjectName(u"btn_ajouter")
        self.btn_ajouter.setEnabled(False)
        self.btn_ajouter.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajouter.setStyleSheet(u"QPushButton {\n"
                                       "  background-color: #0d6efd;\n"
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
                                       "  background-color:#fff;\n"
                                       "  color: #0d6efd;\n"
                                       "  border: 1px solid #9ac3fe;\n"
                                       "}")

        self.verticalLayout.addWidget(self.btn_ajouter)

        self.btn_chercher = QPushButton(self.verticalLayoutWidget)
        self.btn_chercher.setObjectName(u"btn_chercher")
        self.btn_chercher.setEnabled(False)
        self.btn_chercher.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_chercher.setStyleSheet(u"QPushButton {\n"
                                        "  background-color: #0d6efd;\n"
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
                                        "  background-color:#fff;\n"
                                        "  color: #0d6efd;\n"
                                        "  border: 1px solid #9ac3fe;\n"
                                        "}")

        self.verticalLayout.addWidget(self.btn_chercher)

        self.btn_effacer = QPushButton(self.verticalLayoutWidget)
        self.btn_effacer.setObjectName(u"btn_effacer")
        self.btn_effacer.setEnabled(False)
        self.btn_effacer.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_effacer.setStyleSheet(u"QPushButton {\n"
                                       "  background-color: #0d6efd;\n"
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
                                       "  background-color:#fff;\n"
                                       "  color: #0d6efd;\n"
                                       "  border: 1px solid #9ac3fe;\n"
                                       "}")

        self.verticalLayout.addWidget(self.btn_effacer)

        self.btn_maj = QPushButton(self.verticalLayoutWidget)
        self.btn_maj.setObjectName(u"btn_maj")
        self.btn_maj.setEnabled(False)
        self.btn_maj.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_maj.setStyleSheet(u"QPushButton {\n"
                                   "  background-color: #0d6efd;\n"
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
                                   "  background-color:#fff;\n"
                                   "  color: #0d6efd;\n"
                                   "  border: 1px solid #9ac3fe;\n"
                                   "}")

        self.verticalLayout.addWidget(self.btn_maj)

        self.btn_recuper = QPushButton(self.verticalLayoutWidget)
        self.btn_recuper.setObjectName(u"btn_recuper")
        self.btn_recuper.setEnabled(False)
        self.btn_recuper.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_recuper.setStyleSheet(u"QPushButton {\n"
                                       "  background-color: #0d6efd;\n"
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
                                       "  background-color:#fff;\n"
                                       "  color: #0d6efd;\n"
                                       "  border: 1px solid #9ac3fe;\n"
                                       "}")

        self.verticalLayout.addWidget(self.btn_recuper)

        self.btn_quitter = QPushButton(self.verticalLayoutWidget)
        self.btn_quitter.setObjectName(u"btn_quitter")
        self.btn_quitter.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_quitter.setStyleSheet(u"QPushButton {\n"
                                       "  background-color: #0d6efd;\n"
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
                                       "  background-color:#fff;\n"
                                       "  color: #0d6efd;\n"
                                       "  border: 1px solid #9ac3fe;\n"
                                       "}")

        self.verticalLayout.addWidget(self.btn_quitter)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(46, 120, 71, 71))
        self.label.setPixmap(QPixmap(u"../StudentManager/image/groupe.png"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 0, 111, 101))
        self.label_2.setPixmap(QPixmap(u"../StudentManager/image/logo.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuA_propos = QMenu(self.menubar)
        self.menuA_propos.setObjectName(u"menuA_propos")
        self.menuA_propos.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuA_propos.setStyleSheet(u"QMenu {\n"
                                        "    background-color: white;\n"
                                        "    margin: 2px; /* some spacing around the menu */\n"
                                        "}\n"
                                        "\n"
                                        "QMenu::item {\n"
                                        "    padding: 2px 25px 2px 20px;\n"
                                        "    border: 1px solid transparent; /* reserve space for selection border */\n"
                                        "}\n"
                                        "\n"
                                        "QMenu::item:selected {\n"
                                        "    border-color: darkblue;\n"
                                        "    background: rgba(100, 100, 100, 150);\n"
                                        "}\n"
                                        "\n"
                                        "QMenu::icon:checked { /* appearance of a 'checked' icon */\n"
                                        "    background: gray;\n"
                                        "    border: 1px inset gray;\n"
                                        "    position: absolute;\n"
                                        "    top: 1px;\n"
                                        "    right: 1px;\n"
                                        "    bottom: 1px;\n"
                                        "    left: 1px;\n"
                                        "}\n"
                                        "\n"
                                        "QMenu::separator {\n"
                                        "    height: 2px;\n"
                                        "    background: lightblue;\n"
                                        "    margin-left: 10px;\n"
                                        "    margin-right: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "QMenu::indicator {\n"
                                        "    width: 13px;\n"
                                        "    height: 13px;\n"
                                        "}\n"
                                        "")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuA_propos.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableau_etudiant.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Matricule", None))
        ___qtablewidgetitem1 = self.tableau_etudiant.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        ___qtablewidgetitem2 = self.tableau_etudiant.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Telephone", None))
        ___qtablewidgetitem3 = self.tableau_etudiant.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        ___qtablewidgetitem4 = self.tableau_etudiant.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Sexe", None))
        ___qtablewidgetitem5 = self.tableau_etudiant.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        ___qtablewidgetitem6 = self.tableau_etudiant.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Date de naissance", None))
        self.lb_titre.setText(QCoreApplication.translate("MainWindow", u"Systeme de gestion des etudiants", None))
        self.btn_connexion.setText(QCoreApplication.translate("MainWindow", u"Connexion", None))
        self.btn_ajouter.setText(QCoreApplication.translate("MainWindow", u"Ajouter etudiant", None))
        self.btn_chercher.setText(QCoreApplication.translate("MainWindow", u"Chercher etudiants", None))
        self.btn_effacer.setText(QCoreApplication.translate("MainWindow", u"Effacer etudians", None))
        self.btn_maj.setText(QCoreApplication.translate("MainWindow", u"Mise a jour", None))
        self.btn_recuper.setText(QCoreApplication.translate("MainWindow", u"Recuperer donness", None))
        self.btn_quitter.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.label.setText("")
        self.label_2.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuA_propos.setTitle(QCoreApplication.translate("MainWindow", u"A propos", None))
    # retranslateUi
