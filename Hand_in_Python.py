import json
from datetime import datetime
from datetime import date

#Loading the precipitation file
with open('precipitation.json', encoding='utf8') as file:
    rain = json.load(file)

#initialising a list of Seattle-observations
seattle_observations = []

#Changing the 'date' value into a datetime object to be able to access the months
for rain_observation in rain:
    if rain_observation['station'] == 'GHCND:US1WAKG0038':
        rain_datetime = datetime.strptime(rain_observation['date'], '%Y-%m-%d')
        rain_observation['date'] = rain_datetime.date()
        seattle_observations.append(rain_observation)

seattle_rain_per_month = []

for month in range(1,13):
    seattle_rain_per_month.append(0)
    print(seattle_rain_per_month)
    for seattle_rain_observation in seattle_observations:
        if seattle_rain_observation['date'].month == month:
            seattle_rain_per_month[month-1] += seattle_rain_observation['value']

with open('Exercise1.json', 'w', encoding='utf8') as file:
    json.dump(seattle_rain_per_month, file)

# with open('file_name.json', 'w', encoding='utf8') as file:
#     json.dump(some_data, file)