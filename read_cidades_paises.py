import sqlite3

con = sqlite3.connect("crud.db")

cur = con.cursor()

cur.execute("""
    SELECT cidades.nome, paises.nome
    FROM cidades
    INNER JOIN paises
        ON cidades.pais_id = paises.id
""")

resultado = cur.fetchall()

con.close()