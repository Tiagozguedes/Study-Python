import requests

res = requests.get('https://scotch.io')

if res: #True
    print('Responde Ok')
else: 
    print('Responde Failed')

print(res.status_code)

print(res.text) #text retorna um id de resposta em json

API_KEY = 'your yandex api key'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

res = requests.get(url)

params = dict(key=API_KEY,
        text='HELLO',
        lang=es-es)

res = request.get(url, params = params)

print(res.text)

json = res.json()
print(json)

print(json['text'])
print(json['text'][0])

#Fazendo um request para criar cartas novas em uma API de baralho

id = "jfivj1v6vb6o"

url1 = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

puxar_carta = f'https://deckofcardsapi.com/api/deck/{id}/draw/?count=2'

criar_baralho = "https://deckofcardsapi.com/api/deck/new/"

def get_url():
   r = requests.post(criar_baralho, data={"jokers_enabled": True})
   print(r.text)


