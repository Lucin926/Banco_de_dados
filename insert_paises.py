import sqlite3

con = sqlite3.connect("crud.db")

cur = con.cursor()

cur.execute("""
    INSERT INTO paises (nome, populacao, area) VALUES
    ('Brasil', 203000000, 8510000),
    ('Estados Unidos', 335000000, 9834000),
    ('Japão', 124000000, 377975),
    ('Alemanha', 84000000, 357592),
    ('Argentina', 46000000, 2780400),
    ('França', 68000000, 551695),
    ('Canadá', 40000000, 9984670),
    ('Austrália', 27000000, 7692024),
    ('Itália', 59000000, 301340),
    ('Espanha', 48000000, 505990),
    ('Portugal', 10000000, 92212),
    ('México', 130000000, 1964375),
    ('Chile', 19000000, 756102),
    ('Colômbia', 52000000, 1141748),
    ('Peru', 34000000, 1285216),
    ('China', 1410000000, 9596961),
    ('Índia', 1420000000, 3287263),
    ('Rússia', 144000000, 17098242),
    ('Reino Unido', 68000000, 243610),
    ('Coreia do Sul', 51000000, 100210)
""")

con.commit()

con.close()