import sqlite3


def search_cities():
    with sqlite3.connect("cities.db") as conn:
        cursor = conn.cursor()
        cursor.executemany("""
        SELECT "city.name" 
        FROM city
        WHERE "region.name" = 'Архангельская область' 
        """)
        res = cursor.fetchall()
    if res:
        print(res)

