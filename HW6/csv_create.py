import sqlite3
from pathlib import Path
import requests
import pandas as pd

# with sqlite3.connect('cities.db') as connection:
#     cursor = connection.cursor()

url = ("https://raw.githubusercontent.com/"
      "epogrebnyak/ru-cities/main/assets/towns.csv")

p = Path("towns.csv")
if not p.exists():
    content = requests.get(url).text
    p.write_text(content, encoding="utf-8")

df = pd.read_csv("towns.csv")
print(df.sample(5))