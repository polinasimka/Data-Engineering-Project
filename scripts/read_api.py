import requests

url = "https://api.jolpi.ca/ergast/f1/2025/results/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Ошибка:", response.status_code)
