
import pyodbc
 
# se connecter à la base de données Microsoft Access
conn = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=‪C:/Users/user/Documents/rt.accdb;'
)
 
# créer un curseur
cursor = conn.cursor()
 
# exécuter une requête SQL pour récupérer des données
cursor.execute('SELECT * FROM kabeya')
 
# parcourir les résultats de la requête
for row in cursor:
    print(row)
 
# fermer le curseur et la connexion
cursor.close()
conn.close()