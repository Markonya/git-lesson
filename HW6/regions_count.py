import sqlite3

# тут совсем сыро, еще надо думать
def count_regions():
    with sqlite3.connect("cities.db") as conn:
        cursor = conn.cursor()
        cursor.executemany("""SELECT 
        "region.name", 
        COUNT("city.name") 
        FROM region WHERE region_id = id
        GROUP BY
        'region.name'
        """)
        res = cursor.fetchall()
        print(res)
