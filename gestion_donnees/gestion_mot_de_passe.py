import pymysql


class Gestion_mot_de_passe:
    def __init__(self):
        self.connexion_mysql = pymysql.connect(host='localhost', user='root', password='fazili',
                                    database='systeme_de_gestion_d_universite')
        self.curseur = self.connexion_mysql.cursor()

    def ajouter(self, nom, post_nom, email, mot_de_passe):
        query = (
            "INSERT INTO tableau_de_mot_de_passe(Nom, Post_nom, Email, Mot_de_passe) VALUES(%s,%s,%s,%s)"
        )
        indenfiant = (nom, post_nom, email, mot_de_passe)
        self.curseur.execute(query, indenfiant)
        self.connexion_mysql.commit()

    def verifier(self, email, mot_de_passe):
        self.curseur.execute(f"SELECT * FROM tableau_de_mot_de_passe WHERE Email='{email}'")
        identifiant = self.curseur.fetchone()
        vrai_mot_de_passe = identifiant[3]
        if vrai_mot_de_passe == mot_de_passe:
            return True
        return False

    def changer_mot_de_passe(self, email, mot_de_passe ):
        self.curseur.execute(f"UPDATE tableau_de_mot_de_passe SET Mot_de_passe='{mot_de_passe}' WHERE Email='{email}'")
        self.connexion_mysql.commit()
