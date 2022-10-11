import sqlite3

# search_key = input('Введите регион: ')
search_key = 'Архангельская область'

with sqlite3.connect("cities.db") as connection:
    cursor = connection.cursor()
    result = cursor.execute("""
        SELECT city.name, city.region_id 
        FROM city, region 
        WHERE city.region_id = region.id AND region.name LIKE '{0}';
        """.format(search_key))
    print(*sorted([city[0] for city in result.fetchall()]), sep='\n')

