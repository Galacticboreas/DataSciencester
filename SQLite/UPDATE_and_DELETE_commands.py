import sqlite3 as sq

with sq.connect("E:\programming\DataSciencester\saper.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT NOT NULL,
    sex INTEGER DEFAULT 1,
    old INTEGER,
    score INTEGER
)""")

def print_res(result):
    for res in result:
        print(res)
    print("-----------")

cur.execute("INSERT INTO users (name, old, score) VALUES('Алексей', 18, 1000)")
cur.execute("INSERT INTO users (name, old, score) VALUES('Миша', 19, 800)")
cur.execute("INSERT INTO users (name, old, score) VALUES('Федор', 26, 1100)")
cur.execute("INSERT INTO users (name, sex, old, score) VALUES('Маша', 2, 18, 1500)")

cur.execute("SELECT * FROM users")
result = cur.fetchall()
print_res(result)
# ('Алексей', 1, 18, 1000)
# ('Алексей', 1, 18, 1000)
# ('Миша', 1, 19, 800)
# ('Федор', 1, 26, 1100)
# ('Маша', 2, 18, 1500)

cur.execute("UPDATE users SET score = 1600 WHERE rowid = 1")
cur.execute("SELECT rowid, * FROM users")
result = cur.fetchall()
print_res(result)
# (1, 'Алексей', 1, 18, 1600) <- !!!
# (2, 'Алексей', 1, 18, 1000)
# (3, 'Миша', 1, 19, 800)
# (4, 'Федор', 1, 26, 1100)
# (5, 'Маша', 2, 18, 1500)

cur.execute("UPDATE users SET score = score+500 WHERE sex = 2")
cur.execute("SELECT * FROM users")
print_res(cur.fetchall())
# ('Алексей', 1, 18, 1600)
# ('Алексей', 1, 18, 1000)
# ('Миша', 1, 19, 800)
# ('Федор', 1, 26, 1100)
# ('Маша', 2, 18, 2000) <- !!!

cur.execute("UPDATE users SET score = 1500 WHERE name LIKE 'Федор'")
cur.execute("SELECT * FROM users")
print_res(cur.fetchall())
# ('Алексей', 1, 18, 1600)
# ('Алексей', 1, 18, 1000)
# ('Миша', 1, 19, 800)
# ('Федор', 1, 26, 1500) <- !!!
# ('Маша', 2, 18, 2000)

cur.execute("INSERT INTO users (name, sex, old, score) VALUES('Мария', 2, 18, 600)")
cur.execute("INSERT INTO users (name, old, score) VALUES('Владимир', 45, 700)")
cur.execute("INSERT INTO users (name, sex, old, score) VALUES('Елена', 2, 17, 500)")
cur.execute("SELECT * FROM users")
print_res(cur.fetchall())
# ('Алексей', 1, 18, 1600)
# ('Алексей', 1, 18, 1000)
# ('Миша', 1, 19, 800)
# ('Федор', 1, 26, 1500)
# ('Маша', 2, 18, 2000)
# ('Мария', 2, 18, 600)
# ('Владимир', 1, 45, 700)
# ('Елена', 2, 17, 500)

cur.execute("DELETE FROM users WHERE rowid IN(2, 5)")
cur.execute("SELECT rowid, * FROM users")
print_res(cur.fetchall())
# 1 (1, 'Алексей', 1, 18, 1600)
# 2 (3, 'Миша', 1, 19, 800)
# 3 (4, 'Федор', 1, 26, 1500)
# 4 (6, 'Мария', 2, 18, 600)
# 5 (7, 'Владимир', 1, 45, 700)
# 6 (8, 'Елена', 2, 17, 500)

cur.execute("INSERT INTO users VALUES('Даша', 2, 24, 1200)")
cur.execute("SELECT rowid, * FROM users")
print_res(cur.fetchall())
# 1 (1, 'Алексей', 1, 18, 1600)
# 2 (3, 'Миша', 1, 19, 800)
# 3 (4, 'Федор', 1, 26, 1500)
# 4 (6, 'Мария', 2, 18, 600)
# 5 (7, 'Владимир', 1, 45, 700)
# 6 (8, 'Елена', 2, 17, 500)
# 7 (9, 'Даша', 2, 24, 1200) <- !!! 7 - 9
