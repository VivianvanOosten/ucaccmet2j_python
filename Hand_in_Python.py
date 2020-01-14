import json
from datetime import datetime
from datetime import date

with open('precipitation.json', encoding='utf8') as file:
    rain = json.load(file)

seattle_observations = []

for rain_observation in rain:
    if rain_observation['station'] == 'GHCND:US1WAKG0038':
        rain_datetime = datetime.strptime(rain_observation['date'], '%Y-%m-%d')
        rain_observation['date'] = rain_datetime.date()
        seattle_observations.append(rain_observation)





# with open('file_name.json', 'w', encoding='utf8') as file:
#     json.dump(some_data, file)