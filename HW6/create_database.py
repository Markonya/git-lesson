import csv
import sqlite3

con = sqlite3.connect("cities.db")
cur = con.cursor()
cur.execute("""CREATE TABLE database ('region.name' TEXT, 'city.name' TEXT);""")

with open('towns.csv', 'r', encoding='utf8') as fin:
    dr = csv.DictReader(fin, delimiter=',')
    # for line in dr:
        # print(line['region_name'])
        # print(line['city'])
    to_db = [(i['region_name'], i['city']) for i in dr]

cur.executemany("""INSERT INTO database ('region.name', 'city.name') VALUES (?,?);""", to_db)
con.commit()
con.close()

