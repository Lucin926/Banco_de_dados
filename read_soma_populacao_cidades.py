import sqlite3

con = sqlite3.connect("crud.db")

cur = con.cursor()

cur.execute("""
    SELECT paises.nome, SUM(cidades.populacao)
    FROM paises
    INNER JOIN cidades
        ON cidades.pais_id = paises.id
    GROUP BY paises.id
""")

resultado = cur.fetchall()

for pais in resultado:
    print(pais)

con.close()