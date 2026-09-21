import sqlite3

con = sqlite3.connect("crud.db")

con.execute("PRAGMA foreign_keys = ON")

cur = con.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS paises (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        populacao INTEGER NOT NULL,
        area REAL NOT NULL
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS cidades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        populacao INTEGER NOT NULL,
        area REAL NOT NULL,
        pais_id INTEGER NOT NULL,

        FOREIGN KEY (pais_id) REFERENCES paises(id)
    )
""")

con.commit()
con.close()
