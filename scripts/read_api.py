import requests
import pandas as pd

url = "https://api.jolpi.ca/ergast/f1/2025/races/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    races = data["MRData"]["RaceTable"]["Races"]
    df = pd.DataFrame(races)
    df = df[["season", "round", "raceName", "date", "time"]]
    print(df.head(10))
    df.to_csv("data/f1_races_2025.csv", index=False)
else:
    print("Ошибка:", response.status_code)
