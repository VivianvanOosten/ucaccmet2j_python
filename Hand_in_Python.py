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

#initialising a list of monhtly precipitation
seattle_per_month = [0] * 12

# summing over the rain per month
for seattle_rain_observation in seattle_observations:
    month = seattle_rain_observation['date'].month
    seattle_per_month[month-1] += seattle_rain_observation['value']

seattle_total = sum(seattle_per_month)

#calculating the percentage of total rain per month
seattle_per_month = [rain_per_month *100 / seattle_total for rain_per_month in seattle_per_month]

# reading it into a file 
with open('Exercise2.json', 'w', encoding='utf8') as file:
    json.dump(seattle_per_month, file)