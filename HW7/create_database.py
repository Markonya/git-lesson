import csv
import sqlite3

connection = sqlite3.connect("cities.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE region (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT UNIQUE);""")
cursor.execute("""CREATE TABLE city (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT,
region_id INTEGER, FOREIGN KEY (region_id) references region(id),
            UNIQUE(name, region_id) ON CONFLICT IGNORE);""")

with open('towns.csv', 'r', encoding='utf8') as fin1:
    dr1 = csv.DictReader(fin1, delimiter=',')
    to_db1 = [(i['region_name'],) for i in dr1]
    new_to_db1 = []
    [new_to_db1.append(item) for item in to_db1 if item not in new_to_db1]
    cursor.executemany("""INSERT INTO region (name) VALUES (?);""", new_to_db1)
connection.commit()

with sqlite3.connect("cities.db") as connection:
    cursor = connection.cursor()
    result = cursor.execute("""SELECT name, id FROM region;""")
    regions = dict(result.fetchall())

with open('towns.csv', 'r', encoding='utf8') as fin2:
    cities = []
    fin2.readline()

    for city in fin2:
        city = city.split(',')
        name = city[0]
        region = city[4]
        region_id = regions.get(region)
        if region_id:
            cities.append((name, region_id))
        else:
            pass

with sqlite3.connect("cities.db") as connection:
    cursor = connection.cursor()
    cursor.executemany("""INSERT INTO city (name, region_id) VALUES (?, ?);""", cities)

connection.commit()
connection.close()
