import sqlite3

con = sqlite3.connect("crud.db")

cur = con.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS table1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
    """
)

con.commit()
con.close()