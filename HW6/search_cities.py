import sqlite3


def search_cities():
    with sqlite3.connect("cities.db") as conn:
        cursor.executemany("""
        SELECT "city.name" 
        FROM database 
        WHERE "region.name" = 'Архангельская область' 
        """)
        res = cursor.fetchall()
    if res:
        print(res)

