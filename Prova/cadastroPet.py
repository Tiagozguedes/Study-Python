
### 1-a) **(1 Ponto)** 

#def checaCadastroPet(...)
def checaCadastroPET(id_entrada: str) -> str:
    """
    Verifica e formata o ID do PET.

    Aceita strings nos formatos 'TTIIIIIAAAA' ou 'TT-IIIII-AAAA'
    e retorna o ID no formato padrão 'TT-IIIII-AAAA'.
    Qualquer outro formato é rejeitado.
    """
    # Remove hífens se houverem
    id_sem_hifens = id_entrada.replace('-', '')

    # Verifica o formato com base no comprimento
    if len(id_sem_hifens) == 11 and id_sem_hifens.isdigit():
        tipo = id_sem_hifens[0:2]
        sequencial = id_sem_hifens[2:7]
        ano = id_sem_hifens[7:11]
        
        return f"{tipo}-{sequencial}-{ano}"
    else:
        # Rejeita outros formatos
        return "Formato de ID inválido. Use 'TT-IIIII-AAAA' ou 'TTIIIIIAAAA'."

    
#def cadastroPET(...)
def cadastroPET(lista_pets: list, nome_pet: str, tipo_pet: str, ano_nascimento: int) -> list:
    """
    Cria um cadastro de pets, gerando um ID sequencial e adicionando-o à lista.

    Nos parâmetros de entrada, deve inserir:
    - A lista atual de PETS cadastrados;
    - O tipo do PET;
    - O ano de nascimento do PET;
    - O nome do PET.
    """
    # 1. Encontrar o maior ID sequencial
    max_id_sequencial = 0
    if lista_pets:
        for pet in lista_pets:
            # Garante que o ID do pet na lista é uma tupla ou string antes de converter
            if 'ID' in pet:
                try:
                    if isinstance(pet['ID'], tuple) and len(pet['ID']) >= 2:
                        id_sequencial = int(pet['ID'][1])
                    elif isinstance(pet['ID'], str) and len(pet['ID']) >= 7:
                        # Se o ID é uma string, pega a parte sequencial
                        id_sequencial = int(pet['ID'][3:8].replace('-', ''))
                    else:
                        continue # Pula para o próximo pet se o formato do ID for inesperado
                        
                    if id_sequencial > max_id_sequencial:
                        max_id_sequencial = id_sequencial
                except (ValueError, IndexError):
                    continue

    # 2. Atribuir o código do tipo de animal usando match/case
    novo_id_sequencial = str(max_id_sequencial + 1).zfill(5)
    tipo_pet_lower = tipo_pet.lower()
    match tipo_pet_lower:
        case 'cão' | 'cao' | 'cachorro':
            codigo_tipo = '01'
        case 'gato':
            codigo_tipo = '02'
        case 'demais mamíferos' | 'demais mamiferos':
            codigo_tipo = '03'
        case 'ave' | 'aves':
            codigo_tipo = '03' # O documento especifica '03' para aves
        case 'reptil' | 'repteis':
            codigo_tipo = '04'
        case _:
            codigo_tipo = '05'
    
    # 3. Criar a tupla de ID completa e o dicionário do novo pet
    id_completo = (codigo_tipo, novo_id_sequencial, str(ano_nascimento))
    novo_pet = {
        'ID': id_completo,
        'nome': nome_pet,
        'Tipo': tipo_pet.capitalize(),
        'Ano': str(ano_nascimento)
    }

    # 4. Adicionar o novo pet à lista e retornar
    lista_pets.append(novo_pet)
    return lista_pets

#def buscaPET(...)
def buscaPET(lista_pets: list, id_busca: str) -> None:
    """
    Busca um pet na lista de cadastro e imprime seus dados.

    Recebe a lista de PETS cadastrados e o ID de um PET.
    Imprime os dados do pet se encontrado, ou uma mensagem de erro caso contrário.
    """
    # 1. Valida e formata o ID de busca
    id_formatado = checaCadastroPET(id_busca)

    # 2. Verifica se o ID é válido
    if "inválido" in id_formatado:
        print(f"\nErro: {id_formatado}")
        return

    # 3. Busca o pet na lista
    pet_encontrado = None
    for pet in lista_pets:
        if 'ID' in pet:
            # Cria a representação do ID do pet na lista para comparação
            if isinstance(pet['ID'], tuple) and len(pet['ID']) == 3:
                id_pet_cadastrado = f"{pet['ID'][0]}-{pet['ID'][1]}-{pet['ID'][2]}"
            elif isinstance(pet['ID'], str):
                id_pet_cadastrado = pet['ID']
            else:
                continue

            if id_pet_cadastrado == id_formatado:
                pet_encontrado = pet
                break
    
    # 4. Imprime os dados do pet ou a mensagem de erro
    if pet_encontrado:
        # Armazena os dados em variáveis temporárias
        nome = pet_encontrado['nome']
        ano = pet_encontrado['Ano']
        tipo = pet_encontrado['Tipo']
        
        print('\nDados do seu PET: ...')
        print(f'Nome: {nome}')
        print(f'Ano de nascimento: {ano}')
        print(f'Raça: {tipo}')
        print(f'ID: {id_formatado}')
    else:
        print('O ID do PET não foi encontrado no cadastro')
        print(f'Confira os dados e tente novamente!')

#def apagaCadastroPET(...)
def removerPET(lista_pets: list, id_remover: str) -> list:
    """
    Remove um pet do cadastro com base em seu ID.

    Busca o pet na lista de dicionários e, se encontrado, o remove.
    Retorna a lista atualizada de pets.
    """
    id_formatado = checaCadastroPET(id_remover)

    if "inválido" in id_formatado:
        print(f"\nErro: {id_formatado}")
        return lista_pets

    pet_removido = False
    nova_lista_pets = []

    for pet in lista_pets:
        if 'ID' in pet:
            if isinstance(pet['ID'], tuple) and len(pet['ID']) == 3:
                id_pet_cadastrado = f"{pet['ID'][0]}-{pet['ID'][1]}-{pet['ID'][2]}"
            elif isinstance(pet['ID'], str):
                id_pet_cadastrado = pet['ID']
            else:
                id_pet_cadastrado = None

            if id_pet_cadastrado == id_formatado:
                pet_removido = True
            else:
                nova_lista_pets.append(pet)
        else:
            nova_lista_pets.append(pet)
    
    if pet_removido:
        print(f'\nCadastro do PET id: {id_formatado}, removido com sucesso!')
        return nova_lista_pets
    else:
        print('\nO ID do PET não foi encontrado no cadastro.')
        print('Confira os dados e tente novamente!\n')
        return lista_pets

def listarPets(lista_pets: list) -> None:
    """
    Lista todos os pets cadastrados na lista de dicionários.
    Imprime os dados de cada pet de forma formatada.
    """
    if not lista_pets:
        print("\nNão há pets cadastrados.")
        return

    print("\n--- Lista de PETs Cadastrados ---")
    for i, pet in enumerate(lista_pets):
        print(f"\nPet #{i+1}")
        id_pet = pet.get('ID', 'N/A')
        if isinstance(id_pet, tuple):
            id_pet = f"{id_pet[0]}-{id_pet[1]}-{id_pet[2]}"
        
        print(f"Nome: {pet.get('nome', 'N/A')}")
        print(f"Tipo: {pet.get('Tipo', 'N/A')}")
        print(f"Ano: {pet.get('Ano', 'N/A')}")
        print(f"ID: {id_pet}")
    print("\n" + 50*'-')


# --- Questão 2: Testes automáticos ---
if __name__ == '__main__':
    print('Executando Testes das Funções!!!')
    
    db_pets = [
        {
            'ID': '01-00001-2024',
            'nome': 'Max',
            'Tipo': 'cachorro',
            'Ano': '2024'
        },
        {
            'ID': '02-00002-2018',
            'nome': 'Miau',
            'Tipo': 'gato',
            'Ano': '2018'
        }
    ]
    
    print(50*'-')
    print(checaCadastroPET('01-12345-2024'))
    print(50*'-')
    # O cadastroPET agora espera ano_nascimento como int, e os outros como str
    db_pets_atualizado = cadastroPET(db_pets, 'PetTeste', 'OUTRO', 2023)
    print("Base de dados após o cadastro:")
    listarPets(db_pets_atualizado)
    print(50*'-')
    print("Buscando por Miau:")
    buscaPET(db_pets_atualizado, '02000022018')
    print(50*'-')
    print("Tentando remover um pet inexistente:")
    db_pets_remover = removerPET(db_pets_atualizado, '05-00003-2023')
    print("Buscando por Miau após a tentativa de remoção:")
    buscaPET(db_pets_remover, '02000022018')
    print(50*'-')
#if __name__ == .......:

'''db_pets = [
    {
        'ID':'01-00001-2024',
        'nome':'Max',
        'Tipo':'cachorro',
        'Ano':'2024'
    },
    {
        'ID':'02-00002-2018',
        'nome':'Miau',
        'Tipo':'gato',
        'Ano':'2018'
    },
]'''

#testes...

def bubbleSort(lista: list) -> list:
    """
    Ordena uma lista de elementos em ordem crescente usando o algoritmo Bubble Sort.

    Args:
        lista (list): A lista desordenada de elementos.

    Returns:
        list: A lista ordenada.
    """
    n = len(lista)
    # Percorre a lista n-1 vezes
    for i in range(n-1):
        # O último i elementos já estão no lugar
        for j in range(0, n-i-1):
            # Percorre a lista do primeiro ao último elemento não ordenado
            if lista[j] > lista[j+1]:
                # Troca os elementos de lugar
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Teste com a lista fornecida
if __name__ == "__main__":
    lista_teste = [5, 6, 4, 8, 9, 1, 2, 7, 3, 0]
    print(f"Lista original: {lista_teste}")
    lista_ordenada = bubbleSort(lista_teste)
    print(f"Lista ordenada: {lista_ordenada}")