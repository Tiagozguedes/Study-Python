# for e while são laços de repetição

nomes = ["Carlos", "Ana", "Pedro", "Maria"]

for nome in nomes:
    if nome == "Pedro":
        print("Nome encontrado!")
        continue
    print(nome)
print()

for i in range(5):
    print("Boas Vindas!")
print()

valores = [10,20,30,40,50]

soma = 0

for valor in valores:
    soma += valor

print(f"O total da soma é {soma}")
print()

projetos = ["website", "jogo", "análise de dados", None, "aplicativo movel"]

for projeto in projetos:
    if projeto == None:
        print("Projeto Ausente")
        continue
    print(projeto)

print()

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == "O Hobbit":
        print(f"Livro encontrado: {livro}")
        break
    print(livro)

print()

estoque = 5

while estoque > 0:
    print(f"Venda realizada! Estoque restante = {estoque}")
    estoque -=1
print("Sem unidades disponíveis")
print()

x = 10

while x > 0:
    if x % 2 == 0:
        print(f'Faltam apenas {x} segundos - Não perca essa oportunidade')
    else:
        print(f'Contagem continua:{x} segundos restantes')
    x-=1
print('Aproveite a promoção agora!')
print()

livros = [
    {"nome": "1984", "estoqui": 5},
    {"nome": "Dom Casmurro", "estoqui": 0},
    {"nome": "O Pequeno Príncipe", "estoqui": 3},
    {"nome": "O Hobbit", "estoqui": 0},
]

for livro in livros:
    if livro["estoqui"] == 0:
        continue
    print(f'Livro disponível: {livro['nome']}')