import json

with open('precipitation.json', encoding='utf8') as file:
    rain = json.load(file)

seattle_observations = []

for rain_observation in rain:
    if rain_observation['station'] == 'GHCND:US1WAKG0038':
        seattle_observations.append(rain_observation)

print(seattle_observations)

# with open('file_name.json', 'w', encoding='utf8') as file:
#     json.dump(some_data, file)