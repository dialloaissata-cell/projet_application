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

    conn.commit()
    cur.close()
    conn.close()

    print("Tables created successfully!")

# IMPORTANT: appel de la fonction
create_table()