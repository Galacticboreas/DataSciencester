import sqlite3 as sq
from unittest import result

with sq.connect("E:\programming\DataSciencester\cars.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )""")

# When the context manager completes its work, it automatically 
# executes two methods:

# con.commit() – applying all changes to the database tables;
# con.close() – closing the connection to the database.
# These are the necessary actions to save the changes made to 
# the database.

def print_res(result):
    for res in result:
        print(res)
    print("--------------")

# cur.execute("INSERT INTO cars VALUES(1,'Audi',52642)")
# cur.execute("INSERT INTO cars VALUES(2,'Mercedes',57127)")
# cur.execute("INSERT INTO cars VALUES(3,'Skoda',9000)")
# cur.execute("INSERT INTO cars VALUES(4,'Volvo',29000)")
# cur.execute("INSERT INTO cars VALUES(5,'Bentley',350000)")

cars = [
    ('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000)
]
cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
cur.execute("SELECT * FROM cars")
print_res(cur.fetchall())
# (1, 'Audi', 52642)
# (2, 'Mercedes', 57127)
# (3, 'Skoda', 9000)
# (4, 'Volvo', 29000)
# (5, 'Bentley', 350000)

cur.execute("""UPDATE cars SET price = :Price 
    WHERE model LIKE 'A%'""", 
    {'Price': 0}
)
cur.execute("SELECT * FROM cars")
print_res(cur.fetchall())
# (1, 'Audi', 0)           <- !!!
# (2, 'Mercedes', 57127)
# (3, 'Skoda', 9000)
# (4, 'Volvo', 29000)
# (5, 'Bentley', 350000)

cur.executescript("""DELETE FROM cars WHERE model LIKE 'A%';
    UPDATE cars SET price = price+1000
""")
# This method has one limitation: you cannot use query templates 
# here, as we did in previous methods. The execute script 
# literally writes SQL queries as is with all the data.
cur.execute("SELECT * FROM cars")
print_res(cur.fetchall())
# (2, 'Mercedes', 58127)
# (3, 'Skoda', 10000)
# (4, 'Volvo', 30000)
# (5, 'Bentley', 351000)

