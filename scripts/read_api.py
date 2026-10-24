import requests
import pandas as pd
from pathlib import Path

url = "https://api.jolpi.ca/ergast/f1/2025/races/"
response = requests.get(url, timeout=10)
response.raise_for_status()

data = response.json()
races = data["MRData"]["RaceTable"]["Races"]

df = pd.DataFrame(races)
df = df[["season", "round", "raceName", "date", "time"]]

print(df.head(10))

out_dir = Path("data")
out_dir.mkdir(exist_ok=True)

df.to_csv(out_dir / "f1_races_2025.csv", index=False)
