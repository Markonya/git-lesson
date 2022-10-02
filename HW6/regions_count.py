import sqlite3

# тут совсем сыро, еще надо думать
def count_regions():
    with sqlite3.connect("cities.db") as conn:
        cursor = conn.cursor()
        cursor.executemany("""SELECT 
        "region.name" as region, 
        COUNT("city.name") as city 
        FROM database WHERE region.id = city.id
        GROUP BY
        city.id
        """)
        res = cursor.fetchall()
        print(res)
