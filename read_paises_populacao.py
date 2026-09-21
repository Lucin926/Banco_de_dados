import sqlite3

con = sqlite3.connect("crud.db")

cur = con.cursor()

cur.execute("""
    SELECT nome, populacao
    FROM paises
    ORDER BY populacao DESC
""")

resultado = cur.fetchall()

con.close()