import pymysql


class Gestion_tableau_etudiant:
    def __init__(self):
        self.connexion_mysql = pymysql.connect(host="localhost", user="root", password="fazili",
                                               database="systeme_de_gestion_d_universite")
        self.curseur = self.connexion_mysql.cursor()

    def ajouter(self, matricule, noms, faculte, filier, promotion, email, telephone, sexe, adresse, date_de_naissance,
                date_d_inscription, image):

        query = (
            "INSERT INTO tableau_de_gestion_d_etudiant(Matricule, Noms, Facultee, Filiere, Promotion, Email, Telephone, Sexe, Adresse, "
            "Date_de_naissance, Annee_d_inscription, Image) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

        identifiants = (matricule, noms, faculte, filier, promotion, email, telephone, sexe, adresse, date_de_naissance,
                        date_d_inscription, image)
        self.curseur.execute(query, identifiants)
        self.connexion_mysql.commit()

    def effacer(self, matricule):

        query = "DELETE FROM tableau_de_gestion_d_etudiant WHERE matricule=%s"
        self.curseur.execute(query, matricule)
        self.connexion_mysql.commit()

    def mettre_a_jour(self, matricule, noms, faculte, filier, promotion, email, telephone, sexe, adresse,
                      date_de_naissance,
                      date_d_inscription, image):
        query = """UPDATE tableau_de_gestion_d_etudiant SET Noms=%s, Facultee=%s, Filiere=%s, Promotion=%s, Email=%s, 
                    Telephone=%s, Sexe=%s, Adresse=%s, Date_de_naissance=%s, Annee_d_inscription=%s, image=%s
                     WHERE Matricule=%s"""
        identifiants = (noms, faculte, filier, promotion, email, telephone, sexe, adresse, date_de_naissance,
                        date_d_inscription, image, matricule)
        self.curseur.execute(query, identifiants)
        self.connexion_mysql.commit()

    def trier_faculte(self, faculte, filier, promotion):
        query = "SELECT * FROM tableau_de_gestion_d_etudiant WHERE Facultee LIKE %s and Filiere=%s and promotion=%s"
        departement = (faculte, filier, promotion)
        self.curseur.execute(query, departement)
        identifiants = self.curseur.fetchall()
        liste_des_etudiants = []
        for identifiant in identifiants:
            liste_des_etudiants.append(identifiant)

        return liste_des_etudiants

    def trier_sexe(self, sexe):
        query = "SELECT * FROM tableau_de_gestion_d_etudiant WHERE sexe=%s"
        self.curseur.execute(query, sexe)
        identifiants = self.curseur.fetchall()
        liste_des_etudiants = []
        for identifiant in identifiants:
            liste_des_etudiants.append(identifiant)
        return liste_des_etudiants

    def chercher_nom(self, nom):
        query = f"SELECT * FROM tableau_de_gestion_d_etudiant WHERE Noms LIKE '%{nom}%'"
        self.curseur.execute(query)
        liste_des_etudiants = []
        identifiants = self.curseur.fetchall()
        for identifiant in identifiants:
            liste_des_etudiants.append(identifiant)
        return liste_des_etudiants

    def chercher_matricule(self, matricule):
        query = "SELECT * FROM tableau_de_gestion_d_etudiant WHERE Matricule=%s"
        self.curseur.execute(query, matricule)

        liste_des_etudiants = []
        identifiants = self.curseur.fetchall()
        for identifiant in identifiants:
            liste_des_etudiants.append(identifiant)
        return liste_des_etudiants

    def remplir_tableau(self):

        query = "SELECT * FROM tableau_de_gestion_d_etudiant"

        self.curseur.execute(query)
        identifiants = self.curseur.fetchall()
        liste_des_identifiants = []
        for identifiant in identifiants:
            liste_des_identifiants.append(identifiant)

        return liste_des_identifiants

    def trouver_image(self, matricule):

        query = "SELECT * FROM tableau_de_gestion_d_etudiant WHERE matricule = %s"
        self.curseur.execute(query, matricule)
        identifiants = self.curseur.fetchall()
        for image in identifiants:
            image = image[11]
        return image
