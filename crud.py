import mysql.connector

# Etablir une connexion a la base de donnees

connexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "crudPython"
)

# Creation d<utilisateurs
def create_user(nom, email):
    cursor = connexion.cursor()
    cursor.execute("""
         INSERT INTO utilisateurs (nom, email)
         VALUES (%s, %s)
    """, (nom, email))
    connexion.commit()               
    

# Lecture des utilisateurs
def read_users():
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM utilisateurs")
    for (id, nom, email) in cursor:
        print(f"ID : {id}, Nom : {nom}, Email : {email}")

# Mise a jour des utilisateurs
def update_user(id, email):
    cursor = connexion.cursor()
    cursor.execute("""
        UPDATE utilisateurs
        SET email = %s
        WHERE id = %s
    """, (email, id))
    connexion.commit()

# Supression d'utilisateur
def delete_user(id):
    cursor = connexion.cursor()
    cursor.execute("""
        DELETE FROM utilisateurs
        WHERE id = %s
    """, (id,))
    connexion.commit()

"""
Creation des utilisateurs

create_user("John Doe", "john.doe@example.com")
create_user("Bobby Lee", "bobbyleeing@yahoo.com")
create_user("Stroma Valentin", "stromingbig@example.com")
create_user("Louis Bonnet", "bonnetteblan@yahoo.fr")
"""

read_users()
update_user(9, "emicheldev@gmail.com")
delete_user(9)