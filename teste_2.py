import pymysql

connexion_mysql = pymysql.connect(host="localhost", user="root", password="fazili",
                                 database="systeme_de_gestion_d_universite")
curseur = connexion_mysql.cursor()
curseur.execute("SELECT * FROM tableau_de_gestion_d_etudiant WHERE facultee LIKE 's%'")
a = curseur.fetchall()
for i in a:
    print(i)
    
