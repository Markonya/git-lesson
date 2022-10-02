import sqlite3
from sqlite3 import Cursor


def search_cities():
    with sqlite3.connect("cities.db") as conn:
        cursor: Cursor = conn.cursor()
        cursor.executemany("""SELECT "city.name" FROM database WHERE "region.name" MATCH 'Архангельская область'  """)
        res = cursor.fetchall()
    if res:
        print(res)
