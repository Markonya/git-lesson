import sqlite3
from create_database import regions

# search_key = input('Введите регион: ')
search_key = 'Архангельская область'


search_region_id = regions[search_key]
with sqlite3.connect("cities.db") as connection:
    cursor = connection.cursor()
    result = cursor.execute("""SELECT name FROM city WHERE region_id={0};""".format(search_region_id))
    print(*sorted([city[0] for city in result.fetchall()]), sep='\n')

