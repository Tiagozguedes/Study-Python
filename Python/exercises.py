

numero = input('Digite um número')
print(f'Seu número é: {numero}')
print()

def soma(a,b):
    return a+b

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))

soma_numeros = soma(numero1,numero2)
print(f'A soma dos dois é: {soma_numeros} ')
print()
#%%
notas_bimestrais = []
for i in range(4):
    nota = int(input('Digite sua nota aqui: '))
    if nota > 10 or nota < 0:
        print('Nota inválida!')
        break
    notas_bimestrais.append(nota)
    

media_bimestral = sum(notas_bimestrais)/4
print(f'Sua média bimestral é {media_bimestral}')
print()
# %%
#%%
def conversor (metro):
    return metro * 100

metros = eval(input('Digite o valor em metros: '))
print(f'{metros} metros é igual a {conversor(metros)}cm')
print()
# %%

#calculo da área de um circulo

#%%
r_circulo = float(input('Digite a raio do circulo em cm'))

def calcular_area_circulo(r):
    return math.pi * (r**2)

area_circulo = calcular_area_circulo(r_circulo)
print(f'A área do circulo em cm é {area_circulo}')
# %%
print()


hora_paga = float(input('Quanto você ganha por hora?'))
dias_trabalho_mes = int(input('Quantos dias você trabalha no mês?'))

def calculo_de_salario(h_trabalho, d_trabalho,):
    return h_trabalho * d_trabalho

print(f'Seu salário mensal é {calculo_de_salario(hora_paga,dias_trabalho_mes)}')
print()

temperatura_farenheit = float(input('Digite a temperatura em Ferenheit'))

def conversao_temperatura (farenheit):
    return (farenheit -32 / 1.8)

print(f'A temperatua em graus Censius é {conversao_temperatura(temperatura_farenheit)}°')
print()

"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas."""
#%%
pesopeixe = float(input('Digite o peso do peixe em KG: '))

if pesopeixe > 50:
    excesso = pesopeixe - 50
    multa = excesso * 4
    print(f'Seu peixe tem {excesso} de excesso, você terá que pagar R${multa}')
else:
    print('Peso do peixe é de 50Kg. Sem multa para você!')
print()

# %%

"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:"""
#%%
salario = float(input('Digite seu salário'))

def imposto(salario):
    ir = salario * 0.11
    inss = salario * 0.08
    sindicato = salario * 0.05
    print(f"""R${ir} de imposto de renda
    R${inss} de Inss 
    R${sindicato} de sindicato""")
    return salario - ir - inss - sindicato

print(f'Seu salário é {salario} e com descontos fica {imposto(salario)}')
print()
# %%

"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

#%%
import math
area_pintada = float(input('Digite a área a ser pintada em m^2'))

# 1 -> 3
def calcular_tinta(area_pintada):
    tinta_litro = area_pintada / 3
    preco_tinta = (tinta_litro * 80) / 18
    latas_tinta = math.ceil(tinta_litro / 18)
    return preco_tinta, latas_tinta

preco_tinta, latas_tinta = calcular_tinta(area_pintada)

print(f'Para a pintura dessa área de {area_pintada}m^2 irá ser necessário {latas_tinta} latas de tinta e irá custar R${preco_tinta:.2f}')
print()
# regra de 3 que mostra quanto é o preço dos meus litros de tinta: tinta_litro * 80 = 18 * preco_tinta
# 1 -> 18L
# La -> TL
# 1 * TL = 18L * La
# %%

# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho_arquivo = input('Qual o tamanho do arquivo?')
velocidade_internet = input('Qual a sua velocidade de internet?')
