import sqlite3

con = sqlite3.connect("crud.db")
cur = con.cursor()

cur.execute(
    "SELECT * FROM table1"
)

dados = cur.fetchall()

print(dados)
con.close()