import sqlite3


def count_regions():
    with sqlite3.connect("cities.db") as conn:
        cursor = conn.cursor()
        cursor.executemany("""SELECT 
        "region.name" as region, 
        COUNT("city.name") as city 
        FROM database WHERE region.id = cities.id
        GROUP BY
        cities.id
        """)
        res = cursor.fetchall()
        print(res)
