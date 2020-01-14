import json
import csv
from datetime import datetime
from datetime import date

#Loading the precipitation file
with open('precipitation.json', encoding='utf8') as file:
    rain = json.load(file)

with open('stations.csv') as file:
    stations = csv.DictReader(file)
    per_station = {}
    for row in stations:
        per_station[row['Location']] = {
            'State': row['State'],
            'Station': row['Station']
        }

#initialising our overall total amount of rain
overall_total = 0

for station in per_station:
    #initialising a list of station-specific-observations
    observations = []

    #Changing the 'date' value into a datetime object to be able to access the months
    for rain_observation in rain:
        if rain_observation['station'] == per_station[station]['Station']:
            rain_datetime = datetime.strptime(rain_observation['date'], '%Y-%m-%d')
            rain_observation['date'] = rain_datetime.date()
            observations.append(rain_observation)

    #initialising a list of monhtly precipitation
    per_month = [0] * 12

    # summing over the rain per month
    for rain_observation in observations:
        month = rain_observation['date'].month
        per_month[month-1] += rain_observation['value']

    total = sum(per_month)
    overall_total += total

    #calculating the percentage of total rain per month
    per_month_relative = [rain_per_month / total for rain_per_month in per_month]

    #Adding the calculated data to our dictionary
    per_station[station]["totalMonthlyPrecipitation"] = per_month
    per_station[station]["relativeMonthlyPrecipitation"] = per_month_relative
    per_station[station]["totalYearlyPrecipitation"] = total

# Adding the relative yearly rain to the dictionary
for station in per_station:
    relative_yearly = per_station[station]["totalYearlyPrecipitation"] / overall_total
    per_station[station]["relativeYearlyPrecipitation"] = relative_yearly
    print(relative_yearly)

# reading it into a file 
with open('Exercise3.json', 'w', encoding='utf8') as file:
    json.dump(per_station, file)