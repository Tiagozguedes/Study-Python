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

#conjunto vazio
convidados = set()
print(1 in convidados)
print(2 not in convidados)

#Métodos de manipulação entre os conjuntos
a = {1,2,3}
b = {3,4,5}
print(a.union(b))
print(a|b)
a.intersection(b)
print(a & b)
print(a.difference(b))
print(a-b)
print(a.sysmmetric_difference(b))

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
print(f'intens  exclusivos de laura: {', '.join(diference1)}')
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
    convidados.update({'idade': idade,
                        'altura': altura})

print(convidados)
# %%

#dicionário de tuplas
lista_de_tuplas = [("nome", "ana"),("nota", 10.0)]
dicionario = dict(lista_de_tuplas)

#estoque com conjuntos e dicionários
estoque = {
    "frutas": {"maça", "uva"},
    "verduras": {"cenoura","alface"}
}

estoque["frutas"].add(("morango"))
estoque["verduras"].add("alface")
print(estoque)

alunos = {
    "Julia": {
        "nota": 10,
        "altura": 1.80
    },
    "Pedro": {
        "nota": 8.5,
        "altura": 1.75
    },
    "Ana": {
        "nota": 9.0,
        "altura": 1.68
    }
}

# Acessando a nota de outro aluno
print(Alunos["Pedro"]["nota"])


#%%
alunosdict = {}
def media_dos_alunos(a,b):
    return (a+b)/2

while True:
    nome = input("Digite o nome do aluno ou (sair) para ser desconectado: ")
    
    if nome == "sair":
        break

    idade = int(input("Digite a idade do aluno"))
    nota1 = float(input("Digite a nota 1 do aluno"))
    nota2 = float(input("Digite a nota 2 do aluno"))

    media = media_dos_alunos(nota1, nota2)

    alunosdict[nome] = {
        "idade": idade,
        "nota 1": nota1,
        "nota 2": nota2,
        "media": media
    }

print(alunosdict)
# %%
