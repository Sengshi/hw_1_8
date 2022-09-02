import requests


int_hero = {}
heroes = ['Hulk', 'Captain America', 'Thanos']
url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url).json()
for hero in heroes:
    for parametrs in response:
        if hero == parametrs['name']:
            int_hero[parametrs['name']] = parametrs['powerstats']['intelligence']
for k, v in int_hero.items():
    if v == max(int_hero.values()):
        print(f'Умнейший персонаж комиксов: {k}')
