from cadastroPET import checaCadastroPET, cadastroPET, buscaPET, removerPET, listarPets

# Inicializa o banco de dados de pets (lista de dicionários)
db_pets = []

while True:
    print("\n--- Menu Principal ---")
    print("1. Cadastrar PET")
    print("2. Buscar PET")
    print("3. Descadastrar PET")
    print("4. Listar todos os PETS")
    print("5. Sair")
    
    escolha = input("Digite a sua opção: ")
    
    if escolha == '1':
        print("\n--- Cadastro de PET ---")
        nome = input("Digite o nome do PET: ")
        tipo = input("Digite o tipo do PET (ex: Cão, Gato, Ave): ")
        
        try:
            ano = int(input("Digite o ano de nascimento do PET: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um ano válido.")
            continue
        
        db_pets = cadastroPET(db_pets, nome, tipo, ano)
        print(f"\nPET '{nome}' cadastrado com sucesso! ID: {db_pets[-1]['ID']}")
    
    elif escolha == '2':
        if not db_pets:
            print("\nNão há PETs cadastrados.")
            continue
        
        print("\n--- Busca de PET ---")
        id_busca = input("Digite o ID do PET para buscar: ")
        
        buscaPET(db_pets, id_busca)
        
    elif escolha == '3':
        if not db_pets:
            print("\nNão há PETs cadastrados.")
            continue
        
        print("\n--- Descadastro de PET ---")
        id_remover = input("Digite o ID do PET que deseja remover: ")
        
        db_pets = removerPET(db_pets, id_remover)
        
    elif escolha == '4':
        listarPets(db_pets)

    elif escolha == '5':
        print("\nSaindo do sistema. Até mais!")
        break
    
    else:
        print("\nOpção inválida. Por favor, escolha de 1 a 5.")

