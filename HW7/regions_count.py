import sqlite3

with sqlite3.connect("cities.db") as connection:
    cursor = connection.cursor()
    result = cursor.execute("""
        SELECT region.name, count(city.id)
        FROM city, region
        WHERE city.region_id = region.id
        GROUP BY city.region_id;
    """)
    print(*['{0} - {1}'.format(*item) for item in sorted(result.fetchall())], sep='\n')
