import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5")
    
    result = cur.fetchall()
    print(result)
    # [('Сергей', 1, 33, 2000), 
    #   ('Маша ', 2, 18, 1500), 
    #   ('Федор', 1, 26, 1100), 
    #  ('Михаил', 1, 19, 1000), 
    # ('Алексей', 1, 22, 1000)]

    for result in cur:
        print(result)
#     ('Сергей', 1, 33, 2000)
#      ('Маша ', 2, 18, 1500)
#      ('Федор', 1, 26, 1100)
#      'Михаил', 1, 19, 1000)
#    ('Алексей', 1, 22, 1000)

    result = cur.fetchone()
    print(result)
    # ('Сергей', 1, 33, 2000)

    result2 = cur.fetchmany(2)
    print(result2)
    # [('Маша ', 2, 18, 1500), ('Федор', 1, 26, 1100)]

con.close()
