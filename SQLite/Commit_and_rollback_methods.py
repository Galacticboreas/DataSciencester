import sqlite3 as sq

con = None
try:
    con = sq.connect("E:\programming\DataSciencester\cars.db")
    cur = con.cursor()
 
    cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        BEGIN;
        INSERT INTO cars VALUES(NULL,'Audi',52642);
        INSERT INTO cars VALUES(NULL,'Mercedes',57127);
        INSERT INTO cars VALUES(NULL,'Skoda',9000);
        INSERT INTO cars VALUES(NULL,'Volvo',29000);
        INSERT INTO cars VALUES(NULL,'Bentley',350000);
        UPDATE cars SET price = price+1000
    """)
    con.commit()
 
except sq.Error as e:
    if con: con.rollback()
    print("Request execution error")
finally:
    if con: con.close()
