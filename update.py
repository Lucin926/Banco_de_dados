import sqlite3

con = sqlite3.connect("crud.db")
cur = con.cursor()

cur.execute(
    "UPDATE table1"
    "SET name = ?"
    "WHERE id = ?",
    ("LuciluciKelvin", 13)
)

con.commit()
con.close()