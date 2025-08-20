set1 = {'a','b','c'}

set2 = set([3,4,5,6])

set2.add(4)

set2.update([5,6,7])

set2.remove(5)

set2.discard(2)

set2.pop()

#set2clear()

dic1 = {"nome": "Ana",
        "nota": 10.0
        }

dicionario = {}
dicionario = dict()

#%%
#Criando dicionario com listas e tuplas
lista_de_tuplas = [("nome", "Ana"),("nota",10.0)]
dicionario1 = dict(lista_de_tuplas)

print(dicionario1)
print()
#%%

convidados = set()

while True:
    convidado = input("Digite o seu nome ou sair para encerrar: ")

    if convidado.lower() == "sair":
        break
    convidados.add(convidado)

print(f"Convidados confirmados: {', '.join(convidados)}")
print()

texto1 = set(input("Digite um texto: ").lower().split())
texto2 = set(input("Digite um texto: ").lower().split())

comuns = texto1.intersection(texto2)

print(f'As palavras comunus são {comuns}')
print()

list_laura = set(input("Lista de Laura: ").split(", "))
list_ana = set(input('Lista de Ana: ').split(", "))

comum = list_laura.intersection(list_ana)
diference1 = list_laura.difference(list_ana)
diference2 = list_ana.difference(list_laura)

print(f'palavras comuns{comum}')
print(f'inten  exclusivos de laura: {', '.join(diference1)}')
print(f'intens exclusivos de Ana: {', '.join(diference2)}')
print()

#%%
convidados = {}
while True:
    nome = input("Digite um nome ou (sair) para ser desconectado!").lower()
    if nome == "sair":
        break

    idade = input("Digite sua idade: ")
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite o seu peso: "))

    # convidados[nome] = {
    #     "idade" : idade,
    #     "altura" : altura,
    #     "peso" : peso
    # }
    convidados.update({'idade': idade, 'altura': altura})

print(convidados)
# %%


