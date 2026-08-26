import sqlite3

con = sqlite3.connect("crud.db")
cur = con.cursor()

cur.execute(
    "INSERT INTO table1 (name, age)"
    "VALUES (?, ?)",
    ("Kelvin Maues", 19)
)

con.commit()
con.close()