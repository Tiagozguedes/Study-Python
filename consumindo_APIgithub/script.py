import requests
import json

class ListaDeRepositorios():
    def __init__(self, usuario):
        self._usuario = usuario

    def requisicao_api(self):
        resposta = requests.get(f'https://api.github.com/users/{self._usuario}/repos')

        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def imprime_repositorios(self):
        dados_api = self.requisicao_api()
        if isinstance(dados_api, int):
            print(f"Erro na requisição. Código de status: {dados_api}")
        else:
            for repositorio in dados_api:
                print(repositorio['name'])

# Linha 24 corrigida (agora com o nome correto 'ListaDeRepositorios')
repositorios = ListaDeRepositorios('gustavaress') 
repositorios.imprime_repositorios()