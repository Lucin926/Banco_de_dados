import sqlite3

con = sqlite3.connect("crud.db")
cur = con.cursor()

cur.execute(
    "DELETE FROM table1 "
    "WHERE id = ?",
    (10,)
)

con.commit()
con.close()