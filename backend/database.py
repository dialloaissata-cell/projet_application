import psycopg2

def connexion_à_postgresql():
    return psycopg2.connect(
        host="localhost",
        dbname="projet_framework",
        user="postgres",
        password="A17122003f",
    )

def create_table():
    conn = connexion_à_postgresql()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS classes (
        id_classe SERIAL PRIMARY KEY,
        nom_classe VARCHAR (25) NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS etudiants (
        numero VARCHAR(10) PRIMARY KEY,
        code VARCHAR(10),
        prenom VARCHAR(25),
        nom VARCHAR(25),
        date_naissance DATE,
        id_classe INTEGER,
        FOREIGN KEY (id_classe) REFERENCES classes(id_classe)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS matieres (
        id_matiere serial PRIMARY KEY,
        nom_matiere varchar(25));
    """)

    cur.execute("""
        CREATE TABLE etuadiant_matiere(
        numero VARCHAR(10),
        FOREIGN KEY (numero) REFERENCES etudiants(numero));
                """)
    
    cur.execute("""
        CREATE TABLE note_devoir(
        id_note_devoir serial PRIMARY KEY,
        valeur_devoir INTEGER,
        id_matiere INTEGER,
        FOREIGN KEY(id_matiere) REFERENCES matieres(id_matiere));
                """)
      

    cur.execute("""
        CREATE TABLE note_examen(
        id_note_examen serial PRIMARY KEY,
        valeur_examen  INTEGER,
        id_matiere INTEGER,
        FOREIGN KEY(id_matiere) REFERENCES matieres(id_matiere));
                """)
      

    conn.commit()
    cur.close()
    conn.close()

    print("Tables created successfully!")

# IMPORTANT: appel de la fonction
create_table()