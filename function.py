def somar (a, b):
    soma = a + b
    return soma

def comprimentar(nome = "Visitante"):
    print(f'Olá, {nome}!')

comprimentar()

comprimentar("Jade") #Saida é Olá Jade!

def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

boa_dia = criar_saudacao("Bom dia")
boa_noite = criar_saudacao("Boa noite")
print(boa_dia("Vini"))
print(boa_noite("Ana"))

def calcular_idade(ano_nascimento, ano_atual):
    return ano_nascimento - ano_atual

nascimento = int(input('Digite o ano do seu nascimento: '))
atual = int(input('Digite o ano atual: '))

idade = calcular_idade(nascimento, atual)
print(f'A sua idade atual é : {idade}')
print()

def contar_letras(palavras):
    return len(palavras)

texto = input('Digite uma palavra: ')
print(f'Essa palavra tem {contar_letras(texto)} letras20')
# numeros_letra = contar_letras(texto)
# print(f'Essa palavra tem {numeros_letra} de letras')

print(f'Essa palavra tem {contar_letras(texto)} letras20')
print()


def saudacao(hora): 
    if hora < 12:
        return 'Bom dia'
    elif hora < 18:
        return 'Boa tarde'
    else:
        return 'Boa noite'

hora_atual = int(input('Digite a hora: '))
print(saudacao(hora_atual))
print()

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]

def converter (lista):
    return [int(telefones) for telefone in lista]

def verificar_tipos (lista):
    for num in lista:
        if not isinstance(num, int):
            return "Erro na conversõo."

    return "Todos os números foram convertidos corretamente."

telefones_convertidos = converter(telefones)
print(verificar_tipos(telefones_convertidos))
print()

vendas = input('Digite os valores: ').split()
valortotal = sum(map(float, vendas))
print(f'O total vendido é: {valortotal}')






