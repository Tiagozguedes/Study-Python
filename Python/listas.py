list1 = [10,20,30,40]
print(list1[1])
print(list1[1:3])

tupla = (11,42,30,50)
print(tupla[0])
print(tupla[1:3])

list2 = [1,2,3,4]
list2.append(5)
print(list2)
print()

list3 = [1,2,3,4]
list3.insert(1,5)
print(list3)
print()

list4 = [1,2,3,2]
list4.remove(2)
print(list4)
print()

list5 = [1,5,9,2,3]
list5.sort()
print(list5)
print()

list6 = [1,5,9,2,3]
list6.reverse()
print(list6)
print()

list7 = [1,2,3]
print(list7.pop(1))
print(list7)

#recurso da tupla
tupla = (1,2,3)
a, b, c = tupla
print(a, b, c)

compras = ['arroz', 'feijao', 'macarrao']
item = input('Digite o item que deseja verificar: ')
for compra in compras:
    if compra == item:
        print(f'O {item} está disponível!')
    else:
        print(f'O {item} precisa ser comprado')
        print(compras)
        break

notas = [85, 70, 90, 60, 75]
notas.sort()
print(notas)

nomes = []
"""while True:
    nome = input('Digite o nome do voluntario (ou sair): ')
    if nome.lower == 'sair':
        break
    nomes.append(nome)
print("\n Voluntários registrados!:", nomes)"""

estoque1 = ('arroz','feijão','macarrão')
estoque2 = ('óleo','sal','açúcar')

estoque_combinado = estoque1 + estoque2
print(estoquecombinado)