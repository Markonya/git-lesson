from pathlib import Path
import requests
import pandas as pd

url = ("https://raw.githubusercontent.com/"
       "epogrebnyak/ru-cities/main/assets/towns.csv")

path = Path("towns.csv")
if not p.exists():
    content = requests.get(url).text
    path.write_text(content, encoding="utf-8")

file = pd.read_csv("towns.csv")
print(file.sample(5))
