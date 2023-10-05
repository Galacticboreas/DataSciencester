import sqlite3 as sq
from unittest import result

with sq.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("SELECT name, old, score FROM users")
    cur.execute("SELECT rowid, * FROM users")

    result = cur.fetchall()
    for res in result:
        print(res)
# (1, 'Михаил', 1, 19, 0)
# (2, 'Федор', 1, 32, 0)
# (3, 'Алексей', 1, 22, 0)
# (4, 'Миша', 1, 19, 0)
# (5, 'Федор', 1, 26, 0)
# (6, 'Маша ', 2, 18, 0)
# (7, 'Мария', 2, 18, 0)
# (8, 'Сергей', 1, 33, 0)
# (9, 'Владимир', 1, 43, 0)
# (10, 'Елена', 2, 17, 0)
# (11, 'Юля', 2, 23, 0)
