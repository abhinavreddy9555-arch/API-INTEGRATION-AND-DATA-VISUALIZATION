import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

API_KEY = "06f20562534966808d7a58e81bd9b8dd"
CITY = "Warangal"

URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()



temps = []
dates = []

for item in data['list']:
    temps.append(item['main']['temp'])
    dates.append(datetime.datetime.fromtimestamp(item['dt']))

plt.figure(figsize=(12,6))
sns.lineplot(x=dates, y=temps)

plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date/Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
