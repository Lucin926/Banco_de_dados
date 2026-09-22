import sqlite3

con = sqlite3.connect("crud.db")

cur = con.cursor()

cur.execute("""
    SELECT cidades.nome, cidades.populacao, paises.nome
    FROM cidades
    INNER JOIN paises
        ON cidades.pais_id = paises.id
    WHERE cidades.populacao > 500000
""")

resultado = cur.fetchall()

for cidade in resultado:
    print(cidade)

con.close()