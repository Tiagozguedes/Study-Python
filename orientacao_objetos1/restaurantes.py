from modelos.avaliacao import Avaliacao

class Restaurante:
    # O construtor faz com que todas as informações que podem ser repetidas entre os restaurantes
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() #Deixa a primeira letra maiuscula automático
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    # O método de representação de string do objeto
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)}")
        
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {str(restaurante._categoria).ljust(25)} | {restaurante.media_avaliacao.ljust(25)}| {restaurante._ativo}')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self.avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas)
        return media