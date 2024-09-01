import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'aec18af6303cd7034ab1be43ea99b3aa'
HEADER = {'(Content-Type' : 'application/json'}
TRAINER_ID='5050'

def test_status_code():
    response=requests.get(url = f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.status_code ==200



def test_part_of_response():
    response_get=requests.get(url = f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'somus01'


'{"status":"success","data":[{"id":"5050","trainer_name":"somus01","level":"5","pokemons":["34162","32243","33345","33217","33314","64370","33176","33304","33298","50853","44220","33297","33239","33226","33305","32240","32245","32233","34186","33307","64368","53787","33306","34184","34133","64369","33102","33224","33225","33118","33296","33240","33112","33100","33223","33238"],"pokemons_alive":["64368","64369"],"pokemons_in_pokeballs":[],"get_history_battle":"1","is_premium":false,"premium_duration":0,"avatar_id":1,"city":"Волгоград"}]}'
