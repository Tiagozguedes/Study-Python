# Check Point 4  - Computational Thinking Using Python  
Semestre 2

NOME: Tiago Guedes da Costa

RM: 564731

COMO SALVAR O ARQUIVO PARA ENVIAR:
 
 Crie um arquivo compactado, com todos os arquivos ('.py' e '.md'), e o nomeie usando:
  
 Seu primeiro nome, o último nome e o número de registro de aluno, como no exemplo:

    primeiroNome_ultimoNome_NRA.zip (ou rar)




## Questão 1

Subprogramas são vastamente utilizados no desenvolvimento de softwares, principalmente na construção de módulos, que juntamente à uma boa documentação, culminam em uma programação coesa e bem organizada, um dos pilares da programação em equipes.


* Crie um módulo, chamado 'cadastroPet.py', que contenha os seguintes elementos:

    ### 1-a) **(1 Ponto)** 

        Uma função que faça a verificação do número de identificação do PET, sendo que, este número deve ter 11 caracteres e a seguinte lógica:

        Os 2 primeiros digitos devem ser do tipo de animal:
            - 01 para cães;
            - 02 para gatos;
            - 03 para demais mamíferos;
            - 03 para aves no geral;
            - 04 para repteis no geral;
            - 05 para outros.

        Os 5 dígitos subsequentes são o ID sequencial;

        os demais 4 dígitos devem ser o ano do cadastro do PET (exemplo 2025).

        O número recebido deve ser no formato:

            'TT-IIIII-AAAA'

        Mas deve aceitar entradas sem os hífens:

            'TTIIIIIAAAA'

        ** E rejeitar quaisquer outros tipos de entrada!!! **

        O retorno deve ser uma string, no formato:

            'TT-IIIII-AAAA'

        Devem definir os parâmetros de entrada da função, que serão do tipo 'string' bem como o tipo e saída!

        Devem inserir o texto descritivo da função, logo a baixo da linha de abertura (def checaCadastroPET ...)


        NESTE MOMENTO não é necessário checar os elementos internos como a validade do Tipo, ID e ano. 



    ### 1-b) **(1,5 pontos)**

        Criar uma função para criar um cadastro de pets onde:

        Nos parâmetros de entrada, deve inserir:

            - A lista atual de PETS cadastrados;
            - O tipo do PET (tal como mostrado acima);
            - O ano de nascimento do PET;
            - O nome do PET.

        A lista de PETS cadastrados deve ser uma lista de dicionários, e esta mesma lista deve ser alualizada e devolvida com o **RETURN** no programa;

        Exemplo de lista de PETS cadastrados:

            db_pets = [
                {
                    'ID':('01','00001','2024'),
                    'nome':'Max',
                    'Tipo':'Cão',
                    'Ano':'2024'
                },
                {
                    'ID':('02','00002','2018'),
                    'nome':'Miau',
                    'Tipo':'Gato',
                    'Ano':'2018'
                }
            ]

        Quando executar o programa, o ID deve ser atribuído automáticamente, levando em conta que ele é sequêncial, mas pode ter buracos pela extração de algum PET que saiu do cadastro, assim deve buscar o maior ID da lista, e incrementar este id para o novo número.

        Deve também identificar o tipo do PET (dê preferência para usar uma extrutura de decisão do tipo macth/case, e não perca tempo com maiúsculas e minúsculas, deixe tudo em 'lower' case)

        Devem definir os parâmetros de entrada da função, que serão do tipos pertinentes, bem como o tipo e saída!

        Devem inserir o texto descritivo da função, logo a baixo da linha de abertura (def cadastroPET ...)!

        ** Para preencher o ID com ZEROS, use a seguinte função:

            id = idEntrada.zfill(5)



    ### 1-c) **(1,5 ponto)**
        Crie um procedimento que, ao receber a lista de cadastro de PETS, e o ID de um PET, faça a impressão dos dados de um PET cadastrado, buscando ele na lista de dicionários, gerando todas as informações, usando a formatação abaixo:

        * print('Dados do seu PET: ... \n')
        * print(f 'Nome: {nome} \n')
        * print(f'Ano de nascimento: {ano} \n')
        * print(f'Raça: {tipo}')
        * print(f'ID: {id}')

        Para casos sem erros. 

        E:

        * print('O ID no PET não foi encontrado no cadastro \n')
        * print(f'Confira os dados e tente novamente!')

        * podem criar variáveis temporárias para armazenas os dados, e não executar os 'outputs' mais de uma única vez.

        Use a função checaCadastroPET para que o ID possa ser inserido com o formato:

            'TT-IIIII-AAAA'

        Ou:

            'TTIIIIIAAAA'

        Devem definir os parâmetros de entrada da função, que serão do tipos pertinentes!

        Devem inserir o texto descritivo da função, logo a baixo da linha de abertura (def buscaPET ...)!


    ### 1-d) **(1,5 pontos)**

        Crie uma função que, ao receber a lista de cadastro de PETS, e o ID de um PET, busque o PET na lista e faça a remoção do cadastro deste PET, da lista que foi passada, RETORNANDO a nova lista, sem o elemento.

        Deve dar os avisos pertinentes:

            print('O ID no PET não foi encontrado no cadastro \n')
            print(f'Confira os dados e tente novamente!')

        Para os casos onde o elemento não esteja no cadastro, e:

            print(f'Cadastro do PET id: {id}, removido com sucesso!')


        Devem definir os parâmetros de entrada da função, que serão do tipos pertinentes, bem como o tipo e saída!

        Devem inserir o texto descritivo da função, logo a baixo da linha de abertura (def buscaPET ...)! 


    ### 1-e) **(0,5 pontos)**

        Crie um procedimento que liste, 1 a 1, os PETS que estão na lista de dicionários de PETS.
        Use a melhor formatação que achar pertinente

        Devem definir os parâmetros de entrada da função, que serão do tipos pertinentes!

        Devem inserir o texto descritivo da função, logo a baixo da linha de abertura (def listarPets ...)! 


    ### 1-f) **(1 ponto)**

        Explique a diferença entre **funções** e **procedimentos** vistos em aula: 

        RESPONDA AQUI MESMO, ou como texto no seu arquivo cadastroPET.py
        A principal diferença entre funções e procedimentos é que:

Função: Retorna um valor (return). Ela é usada para calcular ou processar algo e devolver o resultado.
Procedimento: Não retorna um valor. Ele serve apenas para executar uma ação, como imprimir algo na tela ou modificar um objeto.
Em Python, a função que não tem return ou que tem return sem um valor, retorna None por padrão, tornando-a, conceitualmente, um procedimento.


## Questão 2 (1 Ponto)

    Podemos incluir testes a serem executados em nossos módulos, de maneira que estes só executem no caso de executarmos a função **DIRETAMENTE** sem ser chamada pelo programa principal:

    Para os testes use este pré cadastro abaixo:

    db_pets = [
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
    ]

    Inclua no módulo 'cadastroPET.py' um laço condicional que verifique, por meio da palavra reservada "_ _ name _ _', se o programa foi executado diretamente, e caso positivo execute testes com os elementos abaixo:

    print('Executando Testes das Funções!!! \n')
    print(50*'-')
    print(checaCadastroPet('01-12345-2024'))
    print(50*'-')
    print(cadastroPET(db_pets,'OUTRO','2023','PetTeste'))
    print(50*'-')
    buscaPET(db_pets,'02000022018')
    print(50*'-')
    apagaCadastroPET(db_pets,'05-00003-2023')
    print(50*'-')


## Questão 3 (1 Ponto)

Crie um arquivo principal.py, importe o módulo cadastroPET.py, ou suas funções diretamente e crie um menu que contenha as opções:

 - Listar todos os PETS;
 - Buscar PET;
 - Cadastrar PET;
 - Descadastrar PET;
 - Sair


## Questão 4 (1 ponto)

  Crie um arquivo bubbleSort.py, e neste arquivo desenvolva uma função que ordene, EM ORDEM CRESCENTE, com o o método de ordenação 'Bubble Sort', uma lista com qualquer 'n' número de elementos. Deve retornar uma lista ordenada!!!

  Devem definir os parâmetros de entrada da função, que serão do tipos pertinentes, bem como o tipo e saída!

  Devem inserir o texto descritivo da função, logo a baixo da linha de abertura (def bubbleSort(...))! 

    Teste com a lista abaixo:

    lista = [5,6,4,8,9,1,2,7,3,0]


