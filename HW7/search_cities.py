import sqlite3


def search_cities():
    with sqlite3.connect("cities.db") as con:
        cursor = con.cursor()
        cursor.executemany("""
        SELECT "city.name" 
        FROM city
        WHERE "region.name" = 'Архангельская область' 
        """)
        res = cursor.fetchall()
    if res:
        print(res)

