import csv
import sqlite3

con = sqlite3.connect("cities.db")
cur = con.cursor()
cur.execute("""CREATE TABLE region (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'region.name' TEXT UNIQUE);""")
cur.execute("""CREATE TABLE city (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'city.name' TEXT,
region_id INTEGER, FOREIGN KEY (region_id) references region(id));""")

with open('towns.csv', 'r', encoding='utf8') as fin1:
    dr1 = csv.DictReader(fin1, delimiter=',')
    to_db1 = [(i['region_name'], ) for i in dr1]
    new_to_db1 = []
    [new_to_db1.append(item) for item in to_db1 if item not in new_to_db1]

with open('towns.csv', 'r', encoding='utf8') as fin2:
    dr2 = csv.DictReader(fin2, delimiter=',')
    to_db2 = [(i['city'], ) for i in dr2]

cur.executemany("""INSERT INTO region ('region.name') VALUES (?);""", new_to_db1)
cur.executemany("""INSERT INTO city ('city.name') VALUES (?);""", to_db2)
con.commit()
con.close()

