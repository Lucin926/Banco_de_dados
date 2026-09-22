import sqlite3

con = sqlite3.connect("crud.db")

cur = con.cursor()

cur.execute("""
    INSERT INTO cidades (nome, populacao, area, pais_id) VALUES
    ('São Paulo', 12300000, 1521, 1),
    ('Rio de Janeiro', 6700000, 1200, 1),
    ('Brasília', 2900000, 5802, 1),
    ('Salvador', 2900000, 693, 1),
    ('Manaus', 2300000, 11401, 1),
    ('Belo Horizonte', 2300000, 331, 1),
    ('Curitiba', 1800000, 435, 1),
    ('Recife', 1500000, 218, 1),

    ('Nova York', 8300000, 783, 2),
    ('Los Angeles', 3800000, 1302, 2),
    ('Chicago', 2700000, 589, 2),
    ('Houston', 2300000, 1651, 2),
    ('Phoenix', 1600000, 1340, 2),

    ('Tóquio', 14000000, 2194, 3),
    ('Osaka', 2700000, 225, 3),
    ('Yokohama', 3700000, 437, 3),
    ('Nagoya', 2300000, 326, 3),

    ('Berlim', 3700000, 891, 4),
    ('Hamburgo', 1900000, 755, 4),
    ('Munique', 1500000, 310, 4),

    ('Buenos Aires', 3100000, 203, 5),
    ('Córdoba', 1500000, 576, 5),
    ('Rosário', 1300000, 178, 5),

    ('Paris', 2100000, 105, 6),
    ('Marselha', 870000, 241, 6),
    ('Lyon', 520000, 48, 6),

    ('Toronto', 3000000, 630, 7),
    ('Montreal', 1800000, 431, 7),
    ('Vancouver', 675000, 115, 7),

    ('Sydney', 5300000, 12368, 8),
    ('Melbourne', 5100000, 9992, 8),
    ('Brisbane', 1300000, 15826, 8),

    ('Roma', 2800000, 1285, 9),
    ('Milão', 1400000, 182, 9),
    ('Nápoles', 910000, 119, 9),

    ('Madri', 3300000, 604, 10),
    ('Barcelona', 1600000, 101, 10),
    ('Valência', 800000, 135, 10),

    ('Lisboa', 550000, 100, 11),
    ('Porto', 230000, 41, 11),
    ('Braga', 200000, 183, 11),

    ('Cidade do México', 9200000, 1485, 12),
    ('Guadalajara', 1400000, 151, 12),
    ('Monterrey', 1100000, 324, 12),

    ('Santiago', 6300000, 641, 13),
    ('Valparaíso', 300000, 402, 13),

    ('Bogotá', 8000000, 1775, 14),
    ('Medellín', 2600000, 382, 14),
    ('Cali', 2200000, 564, 14),

    ('Lima', 10500000, 2672, 15),
    ('Arequipa', 1000000, 633, 15),

    ('Pequim', 21500000, 16411, 16),
    ('Xangai', 25000000, 6340, 16),
    ('Guangzhou', 15000000, 7434, 16),

    ('Nova Délhi', 33000000, 1484, 17),
    ('Mumbai', 21000000, 603, 17),
    ('Bangalore', 13000000, 741, 17),

    ('Moscou', 13000000, 2561, 18),
    ('São Petersburgo', 5600000, 1439, 18),

    ('Londres', 9000000, 1572, 19),
    ('Manchester', 550000, 116, 19),
    ('Birmingham', 1200000, 268, 19),

    ('Seul', 9500000, 605, 20),
    ('Busan', 3300000, 770, 20),
    ('Incheon', 3000000, 1063, 20)
""")

con.commit()

con.close()