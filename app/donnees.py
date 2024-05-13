from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(400, 300)
        widget.setStyleSheet(u"""
        QWidget {
                background-color: #fff;
                color: #363062;
        }""")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel()
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u""" 
        QLabelg
                color: #D6D46D;
                font-size: 12px;
                font-weight: normal;
                margin-bottom: 10px;
        }""")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.le_matricule = QLineEdit()
        self.le_matricule.setObjectName(u"le_matricule")
        self.le_matricule.setStyleSheet(u"""
        QLineEdit {
                border-radius: 8px;
                border: 1px solid #e0e4e7;
                padding: 5px 15px;
                }
        QLineEdit:focus {
                border: 1px solid #d0e3ff;
                }
        QLineEdit::placeholder {
                color: #767e89;
                }""")

        self.gridLayout.addWidget(self.le_matricule, 0, 1, 1, 1)

        self.label_2 = QLabel()
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"""
        QLabelg {
                color: #D6D46D;
                font-size: 12px;
                font-weight: normal;
                margin-bottom: 10px;
                }""")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.le_nom = QLineEdit()
        self.le_nom.setObjectName(u"le_nom")
        self.le_nom.setStyleSheet(u"""
                QLineEdit {
                        border-radius: 8px;
                        border: 1px solid #e0e4e7;
                        padding: 5px 15px;
                        }
                QLineEdit:focus {
                        border: 1px solid #d0e3ff;
                        }
                QLineEdit::placeholder {
                        color: #767e89;
                }""")

        self.gridLayout.addWidget(self.le_nom, 1, 1, 1, 1)

        self.label_3 = QLabel()
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"""
        QLabelg {
                color: #D6D46D;
                font-size: 12px;
                font-weight: normal;
                margin-bottom: 10px;
        }""")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.ln_phone = QLineEdit()
        self.ln_phone.setObjectName(u"ln_phone")
        self.ln_phone.setStyleSheet(u"""
                QLineEdit {
                        border-radius: 8px;
                        border: 1px solid #e0e4e7;
                        padding: 5px 15px;
                        }
                QLineEdit:focus {
                        border: 1px solid #d0e3ff;
                        }
                QLineEdit::placeholder {
                        color: #767e89;
                        }""")

        self.gridLayout.addWidget(self.ln_phone, 2, 1, 1, 1)

        self.label_4 = QLabel()
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"""
        QLabelg {
                color: #D6D46D;
                font-size: 12px;
                font-weight: normal;
                margin-bottom: 10px;
        }""")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.le_email = QLineEdit()
        self.le_email.setObjectName(u"le_email")
        self.le_email.setStyleSheet(u"""
        QLineEdit {
                border-radius: 8px;
                border: 1px solid #e0e4e7;
                padding: 5px 15px;
                }
        QLineEdit:focus {
                border: 1px solid #d0e3ff;
                }
        QLineEdit::placeholder {
                color: #767e89;
                }""")

        self.gridLayout.addWidget(self.le_email, 3, 1, 1, 1)

        self.label_5 = QLabel()
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"""
        QLabelg {
                color: #D6D46D;
                font-size: 12px;
                font-weight: normal;
                margin-bottom: 10px;
                }""")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.le_sexe = QLineEdit()
        self.le_sexe.setObjectName(u"le_sexe")
        self.le_sexe.setStyleSheet(u"""
        QLineEdit {
                border-radius: 8px;
                border: 1px solid #e0e4e7;
                padding: 5px 15px;
                }
        QLineEdit:focus {
                border: 1px solid #d0e3ff;
                }
        QLineEdit::placeholder {
                color: #767e89;
                }""")

        self.gridLayout.addWidget(self.le_sexe, 4, 1, 1, 1)

        self.label_6 = QLabel()
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"""
                QLabelg {
                        color: #D6D46D;
                        font-size: 12px;
                        font-weight: normal;
                        margin-bottom: 10px;
                }""")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.le_adresse = QLineEdit()
        self.le_adresse.setObjectName(u"le_adresse")
        self.le_adresse.setStyleSheet(u"""
        QLineEdit {
                border-radius: 8px;
                border: 1px solid #e0e4e7;
                padding: 5px 15px;
                }
        QLineEdit:focus {
                border: 1px solid #d0e3ff;
                }
        QLineEdit::placeholder {
                color: #767e89;
                }""")

        self.gridLayout.addWidget(self.le_adresse, 5, 1, 1, 1)

        self.label_7 = QLabel()
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"""
                QLabelg {
                        color: #D6D46D;
                        font-size: 12px;
                        font-weight: normal;
                        margin-bottom: 10px;
                }""")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.le_date_de_naissance = QLineEdit()
        self.le_date_de_naissance.setObjectName(u"le_date_de_naissance")
        self.le_date_de_naissance.setStyleSheet(u"""
                QLineEdit {
                        border-radius: 8px;
                        border: 1px solid #e0e4e7;
                        padding: 5px 15px;
                        }
                QLineEdit:focus {
                        border: 1px solid #d0e3ff;
                        }
                QLineEdit::placeholder {
                        color: #767e89;
                }""")

        self.gridLayout.addWidget(self.le_date_de_naissance, 6, 1, 1, 1)

        self.bouton = QPushButton()
        self.bouton.setObjectName(u"bouton")
        self.bouton.setCursor(QCursor(Qt.PointingHandCursor))
        self.bouton.setFixedSize(150, 40)
        self.bouton.setStyleSheet(u"""
                QPushButton {
                        background-color: #fff;
                        color: #0d6efd;
                        font-weight: 600;
                        border-radius: 8px;
                        border: 1px solid #0d6efd;
                        padding: 5px 15px;
                        margin-top: 10px;
                        outline: 0px;
                        }
                QPushButton:hover
                QPushButton:focus {
                        background-color: #0b5ed7;
                        color:#fff;
                        border: 3px solid #9ac3fe;
                }""")

        self.gridLayout.addWidget(self.bouton, 7, 1, 1, 2)
        self.win = QWidget()
        self.win.setLayout(self.gridLayout)
        widget.setCentralWidget(self.win)

        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)

    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Donnees", None))
        self.label.setText(QCoreApplication.translate("widget", u"Matricule", None))
        self.label_2.setText(QCoreApplication.translate("widget", u"Noms", None))
        self.label_3.setText(QCoreApplication.translate("widget", u"Telephonne", None))
        self.label_4.setText(QCoreApplication.translate("widget", u"Email", None))
        self.label_5.setText(QCoreApplication.translate("widget", u"Sexe", None))
        self.label_6.setText(QCoreApplication.translate("widget", u"Adresse", None))
        self.label_7.setText(QCoreApplication.translate("widget", u"Date de naissaine", None))
        self.bouton.setText(QCoreApplication.translate("widget", u"Enregistrer", None))
    # retranslateUi
