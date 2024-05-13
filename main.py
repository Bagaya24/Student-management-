from PySide2 import QtWidgets
from PySide2.QtCore import (QPropertyAnimation)
from PySide2.QtGui import (QPixmap)
from PySide2 import QtCore

from app.ui_connexion import Ui_connexion
from app.donnees import Ui_widget
from ui_fenetre_principale import Ui_Gestion_des_etudiants
from gestion_donnees.gestion_table_etudiant import Gestion_tableau_etudiant
from gestion_donnees.gestion_mot_de_passe import Gestion_mot_de_passe


# noinspection SpellCheckingInspection
class FenetreGestion(Ui_Gestion_des_etudiants, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # apply_stylesheet(app, theme="dark_blue.xml")
        self.gestion_tableau_etudiant = Gestion_tableau_etudiant()
        self.setupUi(self)
        self.setup_ui_dimension_tableau()
        self.setup_ui_combobox()
        self.reglage_filier()
        self.connexion()
        self._remplir()

    def setup_ui_dimension_tableau(self):
        self.tableau_etudiant.setColumnWidth(1, 250)
        self.tableau_etudiant.setColumnWidth(2, 150)
        self.tableau_etudiant.setColumnWidth(3, 200)
        self.tableau_etudiant.setColumnWidth(5, 250)
        self.tableau_etudiant.setColumnWidth(6, 200)
        self.tableau_etudiant.setColumnWidth(8, 200)
        self.tableau_etudiant.setColumnWidth(9, 100)
        self.tableau_etudiant.setColumnWidth(10, 100)

    def _gestion_combobox_ajouter(self):
        """
        Gerer le promotion en fonction des facultes dans le menu maj
        :return:
        """
        if self.cb_ajouter_faculte.currentIndex() == 0:
            self.cb_ajouter_promotion.clear()
            self.cb_ajouter_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_ajouter_filiere.clear()
            self.cb_ajouter_filiere.addItem("Tron commun")
        elif self.cb_ajouter_faculte.currentIndex() == 1:
            self.cb_ajouter_promotion.clear()
            self.cb_ajouter_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_ajouter_filiere.clear()
            self.cb_ajouter_filiere.addItem("Tron commun")
        elif self.cb_ajouter_faculte.currentIndex() == 2:
            self.cb_ajouter_promotion.clear()
            self.cb_ajouter_promotion.addItems(["L1", "L2", "L3", "Doc1", "Doc2", "Doc3", "Doc4"])
            self.cb_ajouter_filiere.clear()
            self.cb_ajouter_filiere.addItem("Medecine humaine")
        elif self.cb_ajouter_faculte.currentIndex() == 3:
            self.cb_ajouter_promotion.clear()
            self.cb_ajouter_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_ajouter_filiere.clear()
            self.cb_ajouter_filiere.addItem("Cerveau")
        elif self.cb_ajouter_faculte.currentIndex() == 4:
            self.cb_ajouter_promotion.clear()
            self.cb_ajouter_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_ajouter_filiere.clear()
            self.cb_ajouter_filiere.addItem("Theologie protestante")
        elif self.cb_ajouter_faculte.currentIndex() == 5:
            self.cb_ajouter_promotion.clear()
            self.cb_ajouter_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_ajouter_filiere.clear()
            self.cb_ajouter_filiere.addItem("Tron commun")
        elif self.cb_ajouter_faculte.currentIndex() == 6:
            self.cb_ajouter_promotion.clear()
            self.cb_ajouter_promotion.addItems(["L0", "L1", "L2", "L3", "M1", "M2"])
            self.cb_ajouter_filiere.clear()
            self.cb_ajouter_filiere.addItem("Tron commun")

    def _gestion_combobox_maj(self):
        """
        Gerer le promotion en fonction des facultes dans le menu maj
        :return:
        """
        if self.cb_maj_faculte.currentIndex() == 0:
            self.cb_maj_promotion.clear()
            self.cb_maj_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_maj_filiere.clear()
            self.cb_maj_filiere.addItem("Tron commun")
        elif self.cb_maj_faculte.currentIndex() == 1:
            self.cb_maj_promotion.clear()
            self.cb_maj_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_maj_filiere.clear()
            self.cb_maj_filiere.addItem("Tron commun")
        elif self.cb_maj_faculte.currentIndex() == 2:
            self.cb_maj_promotion.clear()
            self.cb_maj_promotion.addItems(["L1", "L2", "L3", "Doc1", "Doc2", "Doc3", "Doc4"])
            self.cb_maj_filiere.clear()
            self.cb_maj_filiere.addItem("Medecine humaine")
        elif self.cb_maj_faculte.currentIndex() == 3:
            self.cb_maj_promotion.clear()
            self.cb_maj_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_maj_filiere.clear()
            self.cb_maj_filiere.addItem("Cerveau")
        elif self.cb_maj_faculte.currentIndex() == 4:
            self.cb_maj_promotion.clear()
            self.cb_maj_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_maj_filiere.clear()
            self.cb_maj_filiere.addItem("Theologie humaine")
        elif self.cb_maj_faculte.currentIndex() == 5:
            self.cb_maj_promotion.clear()
            self.cb_maj_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_maj_filiere.clear()
            self.cb_maj_filiere.addItem("Tron commun")
        elif self.cb_maj_faculte.currentIndex() == 6:
            self.cb_maj_promotion.clear()
            self.cb_maj_promotion.addItems(["L0", "L1", "L2", "L3", "M1", "M2"])
            self.cb_maj_filiere.clear()
            self.cb_maj_filiere.addItem("Tron commun")

    def _gestion_combobox_trie(self):
        if self.cb_trie_faculte.currentIndex() == 0 and self.cb_trie_faculte.currentText() != "M":
            self.cb_trie_promotion.clear()
            self.cb_trie_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_trie_filiere.clear()
            self.cb_trie_filiere.addItem("Tron commun")
        elif self.cb_trie_faculte.currentIndex() == 1 and self.cb_trie_faculte.currentText() != "F":
            self.cb_trie_promotion.clear()
            self.cb_trie_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_trie_filiere.clear()
            self.cb_trie_filiere.addItem("Tron commun")
        elif self.cb_trie_faculte.currentIndex() == 2:
            self.cb_trie_promotion.clear()
            self.cb_trie_promotion.addItems(["L1", "L2", "L3", "Doc1", "Doc2", "Doc3", "Doc4"])
            self.cb_trie_filiere.clear()
            self.cb_trie_filiere.addItem("Medecine humaine")
        elif self.cb_trie_faculte.currentIndex() == 3:
            self.cb_trie_promotion.clear()
            self.cb_trie_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_trie_filiere.clear()
            self.cb_trie_filiere.addItem("Cerveau")
        elif self.cb_trie_faculte.currentIndex() == 4:
            self.cb_trie_promotion.clear()
            self.cb_trie_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_trie_filiere.clear()
            self.cb_trie_filiere.addItem("Theologie protestante")
        elif self.cb_trie_faculte.currentIndex() == 5:
            self.cb_trie_promotion.clear()
            self.cb_trie_promotion.addItems(["L1", "L2", "L3", "M1", "M2"])
            self.cb_trie_filiere.clear()
            self.cb_trie_filiere.addItem("Tron commun")
        elif self.cb_trie_faculte.currentIndex() == 6:
            self.cb_trie_promotion.clear()
            self.cb_trie_promotion.addItems(["L0", "L1", "L2", "L3", "M1", "M2"])
            self.cb_trie_filiere.clear()
            self.cb_trie_filiere.addItem("Tron commun")

    def setup_ui_combobox(self):
        """
        Permet de gerer tout le combobox du logiciel
        :return:
        """
        self._gestion_combobox_ajouter()
        self._gestion_combobox_maj()
        self._gestion_combobox_trie()

    def _gestion_filiere_ajouter(self):
        """
        gerer les filieres du menu ajouter
        :return:
        """
        if self.cb_ajouter_filiere.currentIndex() == 0:
            if self.cb_ajouter_promotion.currentIndex() == 2:
                self.cb_ajouter_filiere.clear()
                self.cb_ajouter_filiere.addItems(["Sciences de l'economie", "Sciences de gestions"])
            elif self.cb_ajouter_promotion.currentIndex() == 3 or self.cb_ajouter_promotion.currentIndex() == 4:
                self.cb_ajouter_filiere.clear()
                self.cb_ajouter_filiere.addItems(["Gestion des Entreprises", "Gestions Financiere",
                                                  "Economie Monaitaire", "Microfinance et Banque", "Marketing"])
            else:
                self.cb_ajouter_filiere.clear()
                self.cb_ajouter_filiere.addItem("Tron commun")
        if self.cb_ajouter_faculte.currentIndex() == 5:
            if self.cb_ajouter_promotion.currentIndex() != 0:
                self.cb_ajouter_filiere.clear()
                self.cb_ajouter_filiere.addItems(["Management et politique sante", "Environnement et developpement "
                                                                                   "durable", "Epidemiologie"])
            else:
                self.cb_ajouter_filiere.clear()
                self.cb_ajouter_filiere.addItem("Tron commun")
        if self.cb_ajouter_faculte.currentIndex() == 6:
            if self.cb_ajouter_promotion.currentIndex() == 0 or self.cb_ajouter_promotion.currentIndex() == 1:
                self.cb_ajouter_filiere.clear()
                self.cb_ajouter_filiere.addItem("Tron commun")
            elif self.cb_ajouter_promotion.currentIndex() == 2:
                self.cb_ajouter_filiere.clear()
                self.cb_ajouter_filiere.addItems(["Genie civil", "Genie elec-info"])
            else:
                self.cb_ajouter_filiere.clear()
                self.cb_ajouter_filiere.addItems(["Genie civil", "Genie electricite", "Genie informatique",
                                                  "Genie electronique"])

    def _gestion_filiere_maj(self):
        """
        gerer les filieres du menu maj
        :return:
        """
        if self.cb_maj_faculte.currentIndex() == 0:
            if self.cb_maj_promotion.currentIndex() == 2:
                self.cb_maj_filiere.clear()
                self.cb_maj_filiere.addItems(["Sciences de l'economie", "Sciences de gestions"])
            elif self.cb_maj_promotion.currentIndex() == 3 or self.cb_maj_promotion.currentIndex() == 4:
                self.cb_maj_filiere.clear()
                self.cb_maj_filiere.addItems(["Gestion des Entreprises", "Gestions Financiere",
                                              "Economie Monaitaire", "Microfinance et Banque", "Marketing"])
            else:
                self.cb_maj_filiere.clear()
                self.cb_maj_filiere.addItem("Tron commun")
        if self.cb_maj_faculte.currentIndex() == 5:
            if self.cb_maj_promotion.currentIndex() != 0:
                self.cb_maj_filiere.clear()
                self.cb_maj_filiere.addItems(["Management et politique sante", "Environnement et developpement "
                                                                               "durable", "Epidemiologie"])
            else:
                self.cb_maj_filiere.clear()
                self.cb_maj_filiere.addItem("Tron commun")
        if self.cb_maj_faculte.currentIndex() == 6:
            if self.cb_maj_promotion.currentIndex() == 0 or self.cb_maj_promotion.currentIndex() == 1:
                self.cb_maj_filiere.clear()
                self.cb_maj_filiere.addItem("Tron commun")
            elif self.cb_maj_promotion.currentIndex() == 2:
                self.cb_maj_filiere.clear()
                self.cb_maj_filiere.addItems(["Genie civil", "Genie elec-info"])
            else:
                self.cb_maj_filiere.clear()
                self.cb_maj_filiere.addItems(["Genie civil", "Genie electricite", "Genie informatique",
                                              "Genie electronique"])

    def _gestion_filier_trie(self):
        """
        gestion de filier au menu trie
        :return:
        """
        if self.cb_trie_faculte.currentIndex() == 0:
            if self.cb_trie_promotion.currentIndex() == 2:
                self.cb_trie_filiere.clear()
                self.cb_trie_filiere.addItems(["Sciences de l'economie", "Sciences de gestions"])
            elif self.cb_trie_promotion.currentIndex() == 3 or self.cb_trie_promotion.currentIndex() == 4:
                self.cb_trie_filiere.clear()
                self.cb_trie_filiere.addItems(["Gestion des Entreprises", "Gestions Financiere",
                                               "Economie Monaitaire", "Microfinance et Banque", "Marketing"])
            else:
                self.cb_trie_filiere.clear()
                self.cb_trie_filiere.addItem("Tron commun")
        if self.cb_trie_faculte.currentIndex() == 5:
            if self.cb_trie_promotion.currentIndex() != 0:
                self.cb_trie_filiere.clear()
                self.cb_trie_filiere.addItems(["Management et politique sante", "Environnement et developpement "
                                                                                "durable", "Epidemiologie"])
            else:
                self.cb_trie_filiere.clear()
                self.cb_trie_filiere.addItem("Tron commun")
        if self.cb_trie_faculte.currentIndex() == 6:
            if self.cb_trie_promotion.currentIndex() == 0 or self.cb_maj_promotion.currentIndex() == 1:
                self.cb_trie_filiere.clear()
                self.cb_trie_filiere.addItem("Tron commun")
            elif self.cb_trie_promotion.currentIndex() == 2:
                self.cb_trie_filiere.clear()
                self.cb_trie_filiere.addItems(["Genie civil", "Genie elec-info"])
            else:
                self.cb_trie_filiere.clear()
                self.cb_trie_filiere.addItems(["Genie civil", "Genie electricite", "Genie informatique",
                                               "Genie electronique"])

    def reglage_filier(self):
        """
        Permet de gerer toutes les fileres du logiciel
        :return:
        """
        self._gestion_filiere_ajouter()
        self._gestion_filiere_maj()
        self._gestion_filier_trie()

    def connexion(self):
        self.btn_menu.clicked.connect(lambda: self.expendre_menu_btn(120, True, "1"))
        self.btn_afficher_menu.clicked.connect(lambda: self.expendre_menu_btn(318, True,
                                                                              "2"))

        # PAGE DU MENU
        self.btn_ajouter.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajouter))
        self.btn_effacer.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_effacer))
        self.btn_trier.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_trier))
        self.btn_chercher.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_voir))
        # PAGE DU TABLEAU

        self.btn_ajouter.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_tableau))
        self.btn_maj.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_tableau))
        self.btn_chercher.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_tableau))
        self.btn_supprimer.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_tableau))
        self.btn_trier.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_tableau))
        self.btn_effacer.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_tableau))

        self.btn_quitter.clicked.connect(lambda: self.close())
        # AUTRE FONCTION
        self.btn_supprimer.clicked.connect(self.delete)
        self.btn_enregistrer.clicked.connect(self.remplir_tableau)
        self.btn_maj.clicked.connect(self.mettre_jour)
        self.btn_maj_2.clicked.connect(self.remplir_tableau)
        self.btn_voir.clicked.connect(self.voir_identitee)
        self.btn_trier_2.clicked.connect(self.trier)
        self.btn_voir_checher.clicked.connect(self.chercher)
        self.btn_effacer_chercher.clicked.connect(self.chercher)
        self.cb_ajouter_faculte.activated.connect(self.setup_ui_combobox)
        self.cb_ajouter_promotion.activated.connect(self.reglage_filier)
        self.cb_maj_faculte.activated.connect(self.setup_ui_combobox)
        self.cb_maj_promotion.activated.connect(self.reglage_filier)
        self.cb_trie_faculte.activated.connect(self.setup_ui_combobox)
        self.cb_trie_promotion.activated.connect(self.reglage_filier)
        self.cb_trie_universite.activated.connect(self.gestion_combobox_trie)

        self.ln_ajouter_nom.textChanged.connect(self.couleur_initiale)
        self.ln_ajouter_matricule.textChanged.connect(self.couleur_initiale)
        self.ln_ajouter_adresse.textChanged.connect(self.couleur_initiale)
        self.ln_ajouter_email.textChanged.connect(self.couleur_initiale)
        self.ln_ajouter_telephone.textChanged.connect(self.couleur_initiale)
        self.ln_maj_nom.textChanged.connect(self.couleur_initiale)
        self.ln_maj_matricule.textChanged.connect(self.couleur_initiale)
        self.ln_maj_adresse.textChanged.connect(self.couleur_initiale)
        self.ln_maj_email.textChanged.connect(self.couleur_initiale)
        self.ln_maj_telephone.textChanged.connect(self.couleur_initiale)

    def voir_identitee(self):
        """
        permet de voir les identifiants des etudiant
        :return: une fenetre d'avertissement
        """
        current_index = self.tableau_etudiant.currentRow()
        image = self.gestion_tableau_etudiant.trouver_image(self.tableau_etudiant.item(current_index, 0).text())

        if current_index < 0:
            return QtWidgets.QMessageBox.warning(self, 'Erreur', 'Selection la ligne a voir')
        else:
            self.stackedWidget_2.setCurrentWidget(self.page_voir_2)
            self.lb_photo.setPixmap(QPixmap(image))
            self.lb_matricule.setText(self.tableau_etudiant.item(current_index, 0).text())
            self.lb_noms.setText(self.tableau_etudiant.item(current_index, 1).text())
            self.lb_faculte.setText(self.tableau_etudiant.item(current_index, 2).text())
            self.lb_fliere.setText(self.tableau_etudiant.item(current_index, 3).text())
            self.lb_promotion.setText(self.tableau_etudiant.item(current_index, 4).text())
            self.lb_email.setText(self.tableau_etudiant.item(current_index, 5).text())
            self.lb_telephone.setText(self.tableau_etudiant.item(current_index, 6).text())
            self.lb_sexe.setText(self.tableau_etudiant.item(current_index, 7).text())
            self.lb_adresse.setText(self.tableau_etudiant.item(current_index, 8).text())
            self.lb_date_de_naissance.setText(self.tableau_etudiant.item(current_index, 9).text())
            self.lb_date_inscruption.setText(self.tableau_etudiant.item(current_index, 10).text())

    def chercher_image(self):
        """
        recherches la photo de l'etudiant en rengistrer
        :return:
        """
        chemin, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Selectionner une image",
                                                          " ", "image files(*.jpg *.jpeg *.png)")
        return chemin

    def couleur_initiale(self, v):
        """
        rammene les couleurs initiales quand il a ey une erreur
        :param v:
        :return:
        """
        if self.ln_ajouter_nom.text() != "" or self.ln_maj_nom.text() != "":
            self.ln_ajouter_nom.setStyleSheet(u"""
                                                       QLineEdit {
                                                         border: 1px solid #e0e4e7; 
                                                         }     
                                                       QLineEdit::placeholder {
                                                         color: #C70039;
                                                       }
                                                       QLineEdit:focus {
                                                         border: 1px solid #64CCC5;
                                                       }
                                                   """)
            self.ln_maj_nom.setStyleSheet(u"""
                                                   QLineEdit {
                                                     border: 1px solid #e0e4e7; 
                                                     }     
                                                   QLineEdit::placeholder {
                                                     color: #C70039;
                                                   }
                                                   QLineEdit:focus {
                                                     border: 1px solid #64CCC5;
                                                   }
                                               """)
        if self.ln_maj_matricule.text() != "" or self.ln_ajouter_matricule.text() != "":
            self.ln_ajouter_matricule.setStyleSheet(u"""
                                                   QLineEdit {
                                                     border: 1px solid #e0e4e7; 
                                                     }     
                                                   QLineEdit::placeholder {
                                                     color: #C70039;
                                                   }
                                                   QLineEdit:focus {
                                                     border: 1px solid #64CCC5;
                                                   }
                                           """)
            self.ln_maj_matricule.setStyleSheet(u"""
                                                       QLineEdit {
                                                         border: 1px solid #e0e4e7; 
                                                         }     
                                                       QLineEdit::placeholder {
                                                         color: #C70039;
                                                       }
                                                       QLineEdit:focus {
                                                         border: 1px solid #64CCC5;
                                                       }
                                                   """)
            if self.ln_ajouter_email.text() != "" or self.ln_maj_email.text() != "":
                self.ln_ajouter_email.setStyleSheet(u"""
                                                       QLineEdit {
                                                         border: 1px solid #e0e4e7; 
                                                         }     
                                                       QLineEdit::placeholder {
                                                         color: #C70039;
                                                       }
                                                       QLineEdit:focus {
                                                         border: 1px solid #64CCC5;
                                                       }
                                                   """)
                self.ln_maj_email.setStyleSheet(u"""
                                                           QLineEdit {
                                                             border: 1px solid #e0e4e7; 
                                                             }     
                                                           QLineEdit::placeholder {
                                                             color: #C70039;
                                                           }
                                                           QLineEdit:focus {
                                                             border: 1px solid #64CCC5;
                                                           }
                                                       """)
            if self.ln_ajouter_adresse.text() != "" or self.ln_maj_adresse.text() != "":
                self.ln_ajouter_adresse.setStyleSheet(u"""
                                                           QLineEdit {
                                                             border: 1px solid #e0e4e7; 
                                                             }     
                                                           QLineEdit::placeholder {
                                                             color: #C70039;
                                                           }
                                                           QLineEdit:focus {
                                                             border: 1px solid #64CCC5;
                                                           }
                                                       """)
                self.ln_maj_adresse.setStyleSheet(u"""
                                                           QLineEdit {
                                                             border: 1px solid #e0e4e7; 
                                                             }     
                                                           QLineEdit::placeholder {
                                                             color: #C70039;
                                                           }
                                                           QLineEdit:focus {
                                                             border: 1px solid #64CCC5;
                                                           }
                                                       """)
            if self.ln_ajouter_telephone.text() != "" or self.ln_maj_telephone.text() != "":
                self.ln_ajouter_telephone.setStyleSheet(u"""
                                                           QLineEdit {
                                                             border: 1px solid #e0e4e7; 
                                                             }     
                                                           QLineEdit::placeholder {
                                                             color: #C70039;
                                                           }
                                                           QLineEdit:focus {
                                                             border: 1px solid #64CCC5;
                                                           }
                                                       """)
                self.ln_maj_telephone.setStyleSheet(u"""
                                                           QLineEdit {
                                                             border: 1px solid #e0e4e7; 
                                                             }     
                                                           QLineEdit::placeholder {
                                                             color: #C70039;
                                                           }
                                                           QLineEdit:focus {
                                                             border: 1px solid #64CCC5;
                                                           }
                                                       """)

    def expendre_menu_btn(self, maxWidth, enable, nom_menu):
        """
        Permet de creer une animation quand on affiche le menu
        :param maxWidth:
        :param enable:
        :return:
        """
        if enable and nom_menu == "2":
            self.btn_ajouter.setEnabled(True)
            self.btn_maj.setEnabled(True)
            self.btn_effacer.setEnabled(True)
            self.btn_chercher.setEnabled(True)
            self.btn_trier.setEnabled(True)

            # GET WIDTH
            width = self.menu_pages.width()

            maxExtend = maxWidth
            standard = 0

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:

                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.menu_pages, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

        if enable and nom_menu == "1":

            self.btn_afficher_menu.setEnabled(True)
            # GET WIDTH
            width = self.menu_btn.width()
            maxExtend = maxWidth
            standard = 60

            # SET MAX WIDTH
            if width == 60:

                self.btn_afficher_menu.setText("Menu")
                self.btn_ajouter.setText("Ajouter")
                self.btn_effacer.setText("Effacer")
                self.btn_maj.setText("Mis a jour")
                self.btn_chercher.setText("Chercher")
                self.btn_trier.setText("Trier")
                self.btn_quitter.setText("Quitter")
                widthExtended = maxExtend

            else:
                self.btn_afficher_menu.setText("")
                self.btn_ajouter.setText("")
                self.btn_effacer.setText("")
                self.btn_maj.setText("")
                self.btn_chercher.setText("")
                self.btn_trier.setText("")
                self.btn_quitter.setText("")
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.menu_btn, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def chercher(self):

        if self.stackedWidget.currentIndex() == 1:

            if self.cb_effacer.currentIndex() == 0:
                self.liste_des_identifiants = self.gestion_tableau_etudiant.chercher_matricule(
                    int(self.ln_supprimer.text()))

            else:
                self.liste_des_identifiants = self.gestion_tableau_etudiant.chercher_nom(
                    self.ln_supprimer.text())

        elif self.stackedWidget.currentIndex() == 3:

            if self.cb_voir.currentIndex() == 0:
                self.liste_des_identifiants = self.gestion_tableau_etudiant.chercher_matricule(
                    int(self.ln_chercher.text()))
            else:
                self.liste_des_identifiants = self.gestion_tableau_etudiant.chercher_nom(self.ln_chercher.text())

        self.ligne = self.tableau_etudiant.setRowCount(len(self.liste_des_identifiants))
        self.colonne = self.tableau_etudiant.setColumnCount(11)
        for ligne_index, ligne_data in enumerate(self.liste_des_identifiants):
            for colonne_index, colonne_data in enumerate(ligne_data):
                item = QtWidgets.QTableWidgetItem(str(colonne_data))
                self.tableau_etudiant.setItem(ligne_index, colonne_index, item)

    def trier(self):

        if self.cb_trie_universite.currentIndex() == 0:
            self._remplir()

        elif self.cb_trie_universite.currentIndex() == 1:
            self.liste_des_identifiants = self.gestion_tableau_etudiant.trier_faculte(
                self.cb_trie_faculte.currentText(),
                self.cb_trie_filiere.currentText(),
                self.cb_trie_promotion.currentText())
            self.ligne = self.tableau_etudiant.setRowCount(len(self.liste_des_identifiants))
            self.colonne = self.tableau_etudiant.setColumnCount(11)
            for ligne_index, ligne_data in enumerate(self.liste_des_identifiants):
                for colonne_index, colonne_data in enumerate(ligne_data):
                    item = QtWidgets.QTableWidgetItem(str(colonne_data))
                    self.tableau_etudiant.setItem(ligne_index, colonne_index, item)
        else:
            self.liste_des_identifiants = self.gestion_tableau_etudiant.trier_sexe(self.cb_trie_faculte.currentText())
            self.ligne = self.tableau_etudiant.setRowCount(len(self.liste_des_identifiants))
            self.colonne = self.tableau_etudiant.setColumnCount(11)
            for ligne_index, ligne_data in enumerate(self.liste_des_identifiants):
                for colonne_index, colonne_data in enumerate(ligne_data):
                    item = QtWidgets.QTableWidgetItem(str(colonne_data))
                    self.tableau_etudiant.setItem(ligne_index, colonne_index, item)

    def gestion_combobox_trie(self):
        if self.cb_trie_universite.currentIndex() == 1:
            self.cb_trie_faculte.setEnabled(True)
            self.cb_trie_promotion.setEnabled(True)
            self.cb_trie_filiere.setEnabled(True)
            self.cb_trie_faculte.clear()
            self.cb_trie_faculte.addItems((["Economie", "Droit", "Medecine", "Psychologie", "Theologie",
                                            "Sante publique", "Science de l'ingenieur"]))

        elif self.cb_trie_universite.currentIndex() == 2:
            self.cb_trie_faculte.setEnabled(True)
            self.cb_trie_faculte.clear()
            self.cb_trie_promotion.clear()
            self.cb_trie_filiere.clear()
            self.cb_trie_faculte.addItems(["M", "F"])
            self.cb_trie_filiere.setEnabled(False)
            self.cb_trie_promotion.setEnabled(False)

        else:
            self.cb_trie_faculte.clear()
            self.cb_trie_promotion.clear()
            self.cb_trie_filiere.clear()
            self.cb_trie_faculte.setEnabled(False)
            self.cb_trie_filiere.setEnabled(False)
            self.cb_trie_promotion.setEnabled(False)

    def _remplir(self):
        """
        Affiche les identifiants de la base de donnes dans le tableau
        :return:
        """
        self.liste_des_identifiants = self.gestion_tableau_etudiant.remplir_tableau()
        self.ligne = self.tableau_etudiant.setRowCount(len(self.liste_des_identifiants))
        self.colonne = self.tableau_etudiant.setColumnCount(11)

        for ligne_index, ligne_data in enumerate(self.liste_des_identifiants):
            for colonne_index, colonne_data in enumerate(ligne_data):
                item = QtWidgets.QTableWidgetItem(str(colonne_data))
                self.tableau_etudiant.setItem(ligne_index, colonne_index, item)

    def mettre_jour(self):
        current_index = self.tableau_etudiant.currentRow()
        if current_index < 0:
            return QtWidgets.QMessageBox.warning(self, 'Erreur', 'Selection la ligne a mettre a jour')
        else:
            self.btn_maj.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_maj))
            self.ln_maj_matricule.setText(self.tableau_etudiant.item(current_index, 0).text())
            self.ln_maj_nom.setText(self.tableau_etudiant.item(current_index, 1).text())
            self.ln_maj_email.setText(self.tableau_etudiant.item(current_index, 5).text())
            self.ln_maj_telephone.setText(self.tableau_etudiant.item(current_index, 6).text())
            self.ln_maj_adresse.setText(self.tableau_etudiant.item(current_index, 8).text())

            for i in range(0, self.cb_maj_faculte.count()):
                if self.tableau_etudiant.item(current_index, 2).text() == self.cb_maj_faculte.itemText(i):
                    self.cb_maj_faculte.setCurrentIndex(i)
                    self._gestion_combobox_maj()

            for i in range(0, self.cb_maj_promotion.count()):
                if self.tableau_etudiant.item(current_index, 4).text() == self.cb_maj_promotion.itemText(i):
                    self.cb_maj_promotion.setCurrentIndex(i)
                    self._gestion_filiere_maj()
            for i in range(0, self.cb_maj_filiere.count()):
                if self.tableau_etudiant.item(current_index, 3).text() == self.cb_maj_filiere.itemText(i):
                    self.cb_maj_filiere.setCurrentIndex(i)

            date_naissance = QtCore.QDate.fromString(self.tableau_etudiant.item(current_index, 9).text(), "dd/MM/yyyy")
            annee_inscription = QtCore.QDate.fromString(self.tableau_etudiant.item(current_index, 10).text(), "yyyy")
            self.maj_date_de_naissance.setDate(date_naissance)
            self.maj_annee_inscruption.setDate(annee_inscription)

    def remplir_tableau(self):
        """
        Gestion du tableau
        :return:
        """

        if self.stackedWidget.currentIndex() == 0:
            if self.ln_ajouter_nom.text() == "" or self.ln_ajouter_telephone.text() == "" or self.ln_ajouter_adresse.text() == "" or self.ln_ajouter_email.text() == "" or self.ln_ajouter_matricule.text() == "":
                self.alerte()
            else:
                image = self.chercher_image()
                self.gestion_tableau_etudiant.ajouter(int(self.ln_ajouter_matricule.text()), self.ln_ajouter_nom.text(),
                                                      self.cb_ajouter_faculte.currentText(),
                                                      self.cb_ajouter_filiere.currentText(),
                                                      self.cb_ajouter_promotion.currentText(),
                                                      self.ln_ajouter_email.text(), self.ln_ajouter_telephone.text(),
                                                      self.cb_ajouter_sexe.currentText(),
                                                      self.ln_ajouter_adresse.text(),
                                                      self.ajouter_date_de_naissance.text(),
                                                      self.ajouter_annee_inscruption.text(),
                                                      image)
                self._remplir()
                self.reset()

        if self.stackedWidget.currentIndex() == 2:
            if self.ln_maj_nom.text() == "" or self.ln_maj_telephone.text() == "" or self.ln_maj_adresse.text() == "" or self.ln_maj_email.text() == "" or self.ln_maj_matricule.text() == "":
                self.alerte()
            else:
                button = QtWidgets.QMessageBox.question(
                    self,
                    'Confirmation',
                    'Voulez-vous changer de photo?',
                    QtWidgets.QMessageBox.StandardButton.Yes |
                    QtWidgets.QMessageBox.StandardButton.No
                )
                if button == QtWidgets.QMessageBox.StandardButton.Yes:
                    image = self.chercher_image()
                self.gestion_tableau_etudiant.mettre_a_jour(int(self.ln_maj_matricule.text()), self.ln_maj_nom.text(),
                                                            self.cb_maj_faculte.currentText(),
                                                            self.cb_maj_filiere.currentText(),
                                                            self.cb_maj_promotion.currentText(),
                                                            self.ln_maj_email.text(), self.ln_maj_telephone.text(),
                                                            self.cb_maj_sexe.currentText(),
                                                            self.ln_maj_adresse.text(),
                                                            self.maj_date_de_naissance.text(),
                                                            self.maj_annee_inscruption.text(),
                                                            image)
                self._remplir()
                self.reset()

    def alerte(self):
        """
        Alerte si on n'oublies de completer une entre
        :return:
        """
        if self.stackedWidget.currentIndex() == 0:
            if self.ln_ajouter_nom.text() == "":
                self.ln_ajouter_nom.setPlaceholderText("Veillez completer les noms")
                self.ln_ajouter_nom.setStyleSheet(u"""
                                               QLineEdit {
                                                 border: 1px solid #C70039; 
                                                 }     
                                               QLineEdit::placeholder {
                                                 color: #C70039;
                                               }
                                               QLineEdit:focus {
                                                 border: 1px solid #64CCC5;
                                               }
                                           """)
            if self.ln_ajouter_matricule.text() == "":
                self.ln_ajouter_matricule.setPlaceholderText("Veillez completer le matricule")
                self.ln_ajouter_matricule.setStyleSheet(u"""
                                               QLineEdit {
                                                 border: 1px solid #C70039; 
                                                 }     
                                               QLineEdit::placeholder {
                                                 color: #C70039;
                                               }
                                               QLineEdit:focus {
                                                 border: 1px solid #64CCC5;
                                               }
                                           """)
            if self.ln_ajouter_email.text() == "":
                self.ln_ajouter_email.setPlaceholderText("Veillez completer le Mail")
                self.ln_ajouter_email.setStyleSheet(u"""
                                               QLineEdit {
                                                 border: 1px solid #C70039; 
                                                 }     
                                               QLineEdit::placeholder {
                                                 color: #C70039;
                                               }
                                               QLineEdit:focus {
                                                 border: 1px solid #64CCC5;
                                               }
                                           """)
            if self.ln_ajouter_telephone.text() == "":
                self.ln_ajouter_telephone.setPlaceholderText("Veillez completer le numero de telephone")
                self.ln_ajouter_telephone.setStyleSheet(u"""
                                               QLineEdit {
                                                 border: 1px solid #C70039; 
                                                 }     
                                               QLineEdit::placeholder {
                                                 color: #C70039;
                                               }
                                               QLineEdit:focus {
                                                 border: 1px solid #64CCC5;
                                               }
                                           """)
            if self.ln_ajouter_adresse.text() == "":
                self.ln_ajouter_adresse.setPlaceholderText("Veillez completer l'adresse")
                self.ln_ajouter_adresse.setStyleSheet(u"""
                                               QLineEdit {
                                                 border: 1px solid #C70039; 
                                                 }     
                                               QLineEdit::placeholder {
                                                 color: #C70039;
                                               }
                                               QLineEdit:focus {
                                                 border: 1px solid #64CCC5;
                                               }
                                           """)

        elif self.stackedWidget.currentIndex() == 2:
            if self.ln_maj_nom.text() == "":
                self.ln_maj_nom.setPlaceholderText("Veillez completer les noms")
                self.ln_maj_nom.setStyleSheet(u"""
                                                           QLineEdit {
                                                             border: 1px solid #C70039; 
                                                             }     
                                                           QLineEdit::placeholder {
                                                             color: #C70039;
                                                           }
                                                           QLineEdit:focus {
                                                             border: 1px solid #64CCC5;
                                                           }
                                                       """)
            if self.ln_maj_matricule.text() == "":
                self.ln_maj_matricule.setPlaceholderText("Veillez completer le matricule")
                self.ln_maj_matricule.setStyleSheet(u"""
                                                           QLineEdit {
                                                             border: 1px solid #C70039; 
                                                             }     
                                                           QLineEdit::placeholder {
                                                             color: #C70039;
                                                           }
                                                           QLineEdit:focus {
                                                             border: 1px solid #64CCC5;
                                                           }
                                                       """)
            if self.ln_maj_email.text() == "":
                self.ln_maj_email.setPlaceholderText("Veillez completer le Mail")
                self.ln_maj_email.setStyleSheet(u"""
                                                           QLineEdit {
                                                             border: 1px solid #C70039; 
                                                             }     
                                                           QLineEdit::placeholder {
                                                             color: #C70039;
                                                           }
                                                           QLineEdit:focus {
                                                             border: 1px solid #64CCC5;
                                                           }
                                                       """)
            if self.ln_maj_telephone.text() == "":
                self.ln_maj_telephone.setPlaceholderText("Veillez completer le numero de telephone")
                self.ln_maj_telephone.setStyleSheet(u"""
                                                           QLineEdit {
                                                             border: 1px solid #C70039; 
                                                             }     
                                                           QLineEdit::placeholder {
                                                             color: #C70039;
                                                           }
                                                           QLineEdit:focus {
                                                             border: 1px solid #64CCC5;
                                                           }
                                                       """)
            if self.ln_maj_adresse.text() == "":
                self.ln_maj_adresse.setPlaceholderText("Veillez completer l'adresse")
                self.ln_maj_adresse.setStyleSheet(u"""
                                                           QLineEdit {
                                                             border: 1px solid #C70039; 
                                                             }     
                                                           QLineEdit::placeholder {
                                                             color: #C70039;
                                                           }
                                                           QLineEdit:focus {
                                                             border: 1px solid #64CCC5;
                                                           }
                                                       """)

    def delete(self):
        current_row = self.tableau_etudiant.currentRow()
        if current_row < 0:
            return QtWidgets.QMessageBox.warning(self, 'Erreur', 'Selection la ligne a effacer')

        button = QtWidgets.QMessageBox.question(
            self,
            'Confirmation',
            'Voulez-vous vraiment effacer la ligne selectionnee?',
            QtWidgets.QMessageBox.StandardButton.Yes |
            QtWidgets.QMessageBox.StandardButton.No
        )
        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            self.gestion_tableau_etudiant.effacer(int(self.tableau_etudiant.item(current_row, 0).text()))
            self.tableau_etudiant.removeRow(current_row)

    def reset(self):
        """
        Remetre les Qlineedit a leurs etats iniatiales
        :return:
        """
        if self.stackedWidget.currentIndex() == 0:
            self.ln_ajouter_nom.clear()
            self.ln_ajouter_nom.setPlaceholderText("Noms")
            self.ln_ajouter_matricule.clear()
            self.ln_ajouter_matricule.setPlaceholderText("Matricule")
            self.ln_ajouter_email.clear()
            self.ln_ajouter_email.setPlaceholderText("Email")
            self.ln_ajouter_telephone.clear()
            self.ln_ajouter_telephone.setPlaceholderText("Telephone")
            self.ln_ajouter_adresse.clear()
            self.ln_ajouter_adresse.setPlaceholderText("Adresse")
            self.ln_ajouter_nom.setStyleSheet(u"""
                                QLineEdit {
                                  border: 1px solid #e0e4e7; 
                                  }     
                                QLineEdit::placeholder {
                                  color: #C70039;
                                }
                                QLineEdit:focus {
                                  border: 1px solid #64CCC5;
                                }
                            """)
            self.ln_ajouter_matricule.setStyleSheet(u"""
                                QLineEdit {
                                  border: 1px solid #e0e4e7; 
                                  }     
                                QLineEdit::placeholder {
                                  color: #C70039;
                                }
                                QLineEdit:focus {
                                  border: 1px solid #64CCC5;
                                }
                            """)
            self.ln_ajouter_email.setStyleSheet(u"""
                                QLineEdit {
                                  border: 1px solid #e0e4e7; 
                                  }     
                                QLineEdit::placeholder {
                                  color: #C70039;
                                }
                                QLineEdit:focus {
                                  border: 1px solid #64CCC5;
                                }
                            """)
            self.ln_ajouter_telephone.setStyleSheet(u"""
                                QLineEdit {
                                  border: 1px solid #e0e4e7; 
                                  }     
                                QLineEdit::placeholder {
                                  color: #C70039;
                                }
                                QLineEdit:focus {
                                  border: 1px solid #64CCC5;
                                }
                            """)
            self.ln_ajouter_adresse.setStyleSheet(u"""
                                QLineEdit {
                                  border: 1px solid #e0e4e7; 
                                  }     
                                QLineEdit::placeholder {
                                  color: #C70039;
                                }
                                QLineEdit:focus {
                                  border: 1px solid #64CCC5;
                                }
                            """)

        elif self.stackedWidget.currentIndex() == 2:
            self.ln_maj_nom.clear()
            self.ln_maj_nom.setPlaceholderText("Noms")
            self.ln_maj_matricule.clear()
            self.ln_maj_matricule.setPlaceholderText("Matricule")
            self.ln_maj_email.clear()
            self.ln_maj_email.setPlaceholderText("Email")
            self.ln_maj_telephone.clear()
            self.ln_maj_telephone.setPlaceholderText("Telephone")
            self.ln_maj_adresse.clear()
            self.ln_maj_adresse.setPlaceholderText("Adresse")
            self.ln_maj_nom.setStyleSheet(u"""
                                            QLineEdit {
                                              border: 1px solid #e0e4e7; 
                                              }     
                                            QLineEdit::placeholder {
                                              color: #C70039;
                                            }
                                            QLineEdit:focus {
                                              border: 1px solid #64CCC5;
                                            }
                                        """)
            self.ln_maj_matricule.setStyleSheet(u"""
                                            QLineEdit {
                                              border: 1px solid #e0e4e7; 
                                              }     
                                            QLineEdit::placeholder {
                                              color: #C70039;
                                            }
                                            QLineEdit:focus {
                                              border: 1px solid #64CCC5;
                                            }
                                        """)
            self.ln_maj_email.setStyleSheet(u"""
                                            QLineEdit {
                                              border: 1px solid #e0e4e7; 
                                              }     
                                            QLineEdit::placeholder {
                                              color: #C70039;
                                            }
                                            QLineEdit:focus {
                                              border: 1px solid #64CCC5;
                                            }
                                        """)
            self.ln_maj_telephone.setStyleSheet(u"""
                                            QLineEdit {
                                              border: 1px solid #e0e4e7; 
                                              }     
                                            QLineEdit::placeholder {
                                              color: #C70039;
                                            }
                                            QLineEdit:focus {
                                              border: 1px solid #64CCC5;
                                            }
                                        """)
            self.ln_maj_adresse.setStyleSheet(u"""
                                            QLineEdit {
                                              border: 1px solid #e0e4e7; 
                                              }     
                                            QLineEdit::placeholder {
                                              color: #C70039;
                                            }
                                            QLineEdit:focus {
                                              border: 1px solid #64CCC5;
                                            }
                                        """)


class Connexion(Ui_connexion, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(400, 50, 50, 50)
        self.fenetre_principale = FenetreGestion()
        self.gestion_mot_de_passe = Gestion_mot_de_passe()
        self.connexion()

    def connexion(self):
        self.btn_connexion.clicked.connect(self.verifier_mot_de_passe)
        self.btn_inscription_page2.clicked.connect(self.verifier_mot_de_passe)
        self.btn_confirmer.clicked.connect(self.verifier_mot_de_passe)

        # changer de page
        self.btn_inscription.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_mot_de_passe_oublier.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))

        # reset les lineedit
        self.btn_inscription.clicked.connect(self.effacer_ln)
        self.btn_inscription.clicked.connect(self.reset_mot_de_passe)
        self.btn_mot_de_passe_oublier.clicked.connect(self.effacer_ln)
        self.btn_mot_de_passe_oublier.clicked.connect(self.reset_mot_de_passe)

        # cacher le mot de passe
        self.ln_mot_de_passe.textChanged.connect(self.cache_mot_de_passe)
        self.ln_mot_de_passe_page2.textChanged.connect(self.cache_mot_de_passe)
        self.ln_nouveau_mot_de_passe.textChanged.connect(self.cache_mot_de_passe)
        self.ln_confirmer_mot_de_passe_page2.textChanged.connect(self.cache_mot_de_passe)
        self.ln_confirmer_mot_de_passe_page3.textChanged.connect(self.cache_mot_de_passe)
        self.ch_voir_page_connexion.stateChanged.connect(self.cache_mot_de_passe)
        self.ch_voir_page_inscription.stateChanged.connect(self.cache_mot_de_passe)
        self.ch_voir_page_reinitialiser.stateChanged.connect(self.cache_mot_de_passe)

    def verifier_mot_de_passe(self):
        if self.stackedWidget.currentIndex() == 0:
            if self.gestion_mot_de_passe.verifier(self.ln_email.text(), self.ln_mot_de_passe.text()):
                self.fenetre_principale.show()
                self.close()
            else:

                QtWidgets.QMessageBox.warning(self, "Erreur de connexion", "Veillez verifier "
                                                                           "votre mot de passe ou Email")
                self.alarme_mot_de_passe()

        elif self.stackedWidget.currentIndex() == 1:
            if len(self.ln_mot_de_passe_page2.text()) >= 8:
                if self.ln_mot_de_passe_page2.text() == self.ln_confirmer_mot_de_passe_page2.text():
                    if self.ln_nom.text() != "" and self.ln_post_nom.text() != "" and self.ln_email_page2.text() != "":
                        try:
                            self.gestion_mot_de_passe.ajouter(self.ln_nom.text(), self.ln_post_nom.text(),
                                                              self.ln_email_page2.text(), self.ln_mot_de_passe_page2.text())
                            QtWidgets.QMessageBox.information(self, "Confirmation", "Vous venez de creer un compte "
                                                                                    "utilisateur")
                            self.stackedWidget.setCurrentWidget(self.page)
                            self.effacer_ln()
                        except :
                            QtWidgets.QMessageBox.warning(self, "Erreur", "Il y'a un probleme avec la base de "
                                                                          "donnee, veillez saisir un autre Email")



                    else:
                        QtWidgets.QMessageBox.warning(self, "Erreur d'enregistrement", "Veillez remplir l'une "
                                                                                       "de ces 3 entrees 'Nom, Post_nom"
                                                                                       ",Email'")
                else:
                    self.alarme_mot_de_passe()
            else:
                self.alarme_mot_de_passe_court()

        elif self.stackedWidget.currentIndex() == 2:
            if len(self.ln_nouveau_mot_de_passe.text()) >= 8:
                if self.ln_confirmer_mot_de_passe_page3.text() == self.ln_nouveau_mot_de_passe.text():
                    if self.ln_email_page3.text() != "":
                        self.gestion_mot_de_passe.changer_mot_de_passe(self.ln_email_page3.text(),
                                                                       self.ln_nouveau_mot_de_passe.text())
                    self.reset_mot_de_passe()
                    QtWidgets.QMessageBox.information(self, "Confirmation", "Vous venez reinitialiser le mot de "
                                                                            "passe")
                    self.stackedWidget.setCurrentWidget(self.page)
                    self.effacer_ln()
                else:
                    self.alarme_mot_de_passe()
            else:
                self.alarme_mot_de_passe_court()

    def reset_mot_de_passe(self):
        if self.stackedWidget.currentIndex() == 0:
            self.ln_mot_de_passe.setStyleSheet(u"""
                                        QLineEdit {
                                          border: 1px solid #176B87; 
                                          }     
                                        QLineEdit::placeholder {
                                          color: #C70039;
                                        }
                                        QLineEdit:focus {
                                          border: 1px solid #64CCC5;
                                        }
                                    """)
        elif self.stackedWidget.currentIndex() == 1:
            self.ln_mot_de_passe_page2.setPlaceholderText("Mot de passe")
            self.ln_mot_de_passe_page2.setStyleSheet(u"""
                                                                                QLineEdit {
                                                                                  border: 1px solid #176B87; 
                                                                                  }     
                                                                                QLineEdit::placeholder {
                                                                                  color: #C70039;
                                                                                }
                                                                                QLineEdit:focus {
                                                                                  border: 1px solid #64CCC5;
                                                                                }
                                                                            """)
            self.ln_confirmer_mot_de_passe_page2.setPlaceholderText("Confirmer mot de passe")
            self.ln_confirmer_mot_de_passe_page2.setStyleSheet(u"""
                                                                    QLineEdit {
                                                                      border: 1px solid #176B87; 
                                                                      }     
                                                                    QLineEdit::placeholder {
                                                                      color: #C70039;
                                                                    }
                                                                    QLineEdit:focus {
                                                                      border: 1px solid #64CCC5;
                                                                    }
                                                                """)
        elif self.stackedWidget.currentIndex() == 2:
            self.ln_nouveau_mot_de_passe.setPlaceholderText("Nouveau mot de passe")
            self.ln_nouveau_mot_de_passe.setStyleSheet(u"""
                                                                                QLineEdit {
                                                                                  border: 1px solid #176B87; 
                                                                                  }     
                                                                                QLineEdit::placeholder {
                                                                                  color: #C70039;
                                                                                }
                                                                                QLineEdit:focus {
                                                                                  border: 1px solid #64CCC5;
                                                                                }
                                                                            """)
            self.ln_confirmer_mot_de_passe_page3.setPlaceholderText("Confirmer mot de passe")
            self.ln_confirmer_mot_de_passe_page3.setStyleSheet(u"""
                                                                    QLineEdit {
                                                                      border: 1px solid #176B87; 
                                                                      }     
                                                                    QLineEdit::placeholder {
                                                                      color: #C70039;
                                                                    }
                                                                    QLineEdit:focus {
                                                                      border: 1px solid #64CCC5;
                                                                    }
                                                                """)
        self.ln_mot_de_passe.setStyleSheet(u"""
                                                QLineEdit {
                                                  border: 1px solid #176B87; 
                                                  }     
                                                QLineEdit::placeholder {
                                                  color: #C70039;
                                                }
                                                QLineEdit:focus {
                                                  border: 1px solid #64CCC5;
                                                }
                                            """)

    def alarme_mot_de_passe_court(self):

        if self.stackedWidget.currentIndex() == 1:
            self.ln_mot_de_passe_page2.clear()
            self.ln_mot_de_passe_page2.setPlaceholderText("Mot de passe trop court")
            self.ln_mot_de_passe_page2.setStyleSheet(u"""
                                                   QLineEdit {
                                                     border: 1px solid #C70039; 
                                                     }     
                                                   QLineEdit::placeholder {
                                                     color: #C70039;
                                                   }
                                                   QLineEdit:focus {
                                                     border: 1px solid #64CCC5;
                                                   }
                                               """)
        elif self.stackedWidget.currentIndex() == 2:
            self.ln_nouveau_mot_de_passe.clear()
            self.ln_nouveau_mot_de_passe.setPlaceholderText("Mot de passe trop court")
            self.ln_nouveau_mot_de_passe.setStyleSheet(u"""
                                                               QLineEdit {
                                                                 border: 1px solid #C70039; 
                                                                 }     
                                                               QLineEdit::placeholder {
                                                                 color: #C70039;
                                                               }
                                                               QLineEdit:focus {
                                                                 border: 1px solid #64CCC5;
                                                               }
                                                           """)

    def alarme_mot_de_passe(self):
        if self.stackedWidget.currentIndex() == 0:
            self.ln_mot_de_passe.clear()
            self.ln_mot_de_passe.setPlaceholderText("Verifier le mot de passe")
            self.ln_mot_de_passe.setStyleSheet(u"""
                                               QLineEdit {
                                                 border: 1px solid #C70039; 
                                                 }     
                                               QLineEdit::placeholder {
                                                 color: #C70039;
                                               }
                                               QLineEdit:focus {
                                                 border: 1px solid #64CCC5;
                                               }
                                           """)
        elif self.stackedWidget.currentIndex() == 1:
            self.ln_confirmer_mot_de_passe_page2.clear()
            self.ln_confirmer_mot_de_passe_page2.setPlaceholderText("Les mots de passe ne sont pas les memes")
            self.ln_confirmer_mot_de_passe_page2.setStyleSheet(u"""
                                                   QLineEdit {
                                                     border: 1px solid #C70039; 
                                                     }     
                                                   QLineEdit::placeholder {
                                                     color: #C70039;
                                                   }
                                                   QLineEdit:focus {
                                                     border: 1px solid #64CCC5;
                                                   }
                                               """)
        elif self.stackedWidget.currentIndex() == 2:
            self.ln_confirmer_mot_de_passe_page3.clear()
            self.ln_confirmer_mot_de_passe_page3.setPlaceholderText("Les mots de passe ne sont pas les memes")
            self.ln_confirmer_mot_de_passe_page3.setStyleSheet(u"""
                                                               QLineEdit {
                                                                 border: 1px solid #C70039; 
                                                                 }     
                                                               QLineEdit::placeholder {
                                                                 color: #C70039;
                                                               }
                                                               QLineEdit:focus {
                                                                 border: 1px solid #64CCC5;
                                                               }
                                                           """)

    def effacer_ln(self):
        self.ln_mot_de_passe.clear()
        self.ln_email.clear()
        self.ln_email_page2.clear()
        self.ln_nouveau_mot_de_passe.clear()
        self.ln_confirmer_mot_de_passe_page2.clear()
        self.ln_email_page3.clear()
        self.ln_mot_de_passe_page2.clear()
        self.ln_nom.clear()
        self.ln_post_nom.clear()
        self.ln_confirmer_mot_de_passe_page3.clear()

    def cache_mot_de_passe(self):

        if str(self.ch_voir_page_connexion.checkState()).split(".")[4] == "Unchecked":
            self.ln_mot_de_passe.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        elif str(self.ch_voir_page_connexion.checkState()).split(".")[4] == "Checked":
            self.ln_mot_de_passe.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        if str(self.ch_voir_page_inscription.checkState()).split(".")[4] == "Unchecked":
            self.ln_mot_de_passe_page2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.ln_confirmer_mot_de_passe_page2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        elif str(self.ch_voir_page_inscription.checkState()).split(".")[4] == "Checked":
            self.ln_mot_de_passe_page2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.ln_confirmer_mot_de_passe_page2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        if str(self.ch_voir_page_reinitialiser.checkState()).split(".")[4] == "Unchecked":
            self.ln_nouveau_mot_de_passe.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.ln_confirmer_mot_de_passe_page3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        elif str(self.ch_voir_page_reinitialiser.checkState()).split(".")[4] == "Checked":
            self.ln_nouveau_mot_de_passe.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.ln_confirmer_mot_de_passe_page3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)

    def afficher_fenetre_principale(self):
        self.fenetre_principale.show()
        self.close()


class Donnes(Ui_widget, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = Connexion()
    win.show()
    app.exec_()