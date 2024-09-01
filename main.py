import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'aec18af6303cd7034ab1be43ea99b3aa'
HEADER = {'(Content-Type' : 'application/json','trainer_token' : 'aec18af6303cd7034ab1be43ea99b3aa'}
 
'''body_create_pokemons = {
    "name": "TarasBulba",
    "photo_id": 79
}
respons = requests.post(url = f'{URL}/pokemons', headers=HEADER, json=body_create_pokemons )
print(respons.text)'''

'''body_rename_pokemons={
    "pokemon_id": "64370",
    "name": "VosstavshiyizPekla",
    "photo_id": 95
}
respons=requests.put(url = f'{URL}/pokemons', headers=HEADER, json=body_rename_pokemons )
print(respons.text)'''

body_add_in_pokeball={
    "pokemon_id": "64370"
}
respons=requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_in_pokeball )
print(respons.text)