import sqlite3

con = sqlite3.connect("crud.db")

cur = con.cursor()

cur.execute("""
    SELECT nome, populacao
    FROM cidades
    WHERE populacao > 1000000
""")

resultado = cur.fetchall()


con.close()
