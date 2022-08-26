import requests
import json


int_hero = {}
heroes = ['Hulk', 'Captain America', 'Thanos']
url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = json.loads(requests.get(url).text)
for hero in heroes:
    for parametrs in response:
        if hero == parametrs['name']:
            int_hero[parametrs['name']] = parametrs['powerstats']['intelligence']
            break
print(f'Умнейший персонаж комиксов: {max(int_hero)}')
