#Escreva uma classe para representar um Copo com os atributos e métodos a seguir:
#ATRIBUTOS:
#- material: plástico, alumínio, vidro...
#- térmico: indica se é térmico ou não
#- cor: azul, vermelho, rosa, amarelo...
#- capacidade máxima: quantidade de líquido máxima de um copo dada em ml, 
# p.ex., 50ml, 100ml, 250ml... deve ser maior ou igual a 50ml 
#- capacidade atual: quantidade de líquido atualmente armazenado num copo dada em ml
#MÉTODOS:
#- construtor: parametrizado com o material, cor, capacidade máxima e se é ou não térmico
#- métodos acessores do tipo get
#- encher: adiciona uma quantidade de ml a um copo, de modo que deve-se lançar um erro caso o copo transborde
#- esvaziar: diminui cinco unidades de ml da capacidade atual, 
# considerando que só ocorre esvaziamento quanto tem líquido no copo 
# (deve-se lançar um erro caso o copo já esteja vazio)

class Copo:

    def __init__(self, material, cor, capacidade, e_termico):
        if capacidade <= 50:
            raise ValueError('A capacidade do copo tem que ser maior ou igual a 50ml!')
        self.__material = material
        self.__cor = cor
        self.__capacidade = capacidade
        self.__e_termico = eh_termico
        self.__capacidade_atual = 0

    @property
    def material(self):
        return self.__material

    @property
    def cor(self):
        return self.__cor

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def e_termico(self):
        return self.__e_termico

    @property
    def capacidade_atual(self):
        return self.__capacidade_atual

    def encher(self, quantidade):
        if self.__capacidade_atual + quantidade > self.__capacidade:
            raise ValueError('O copo irá transbordar com a quantidade informada!')
        self.__capacidade_atual += quantidade

    def esvaziar(self):
        if self.__capacidade_atual == 0:
            raise ValueError('O copo já está vazio!')
        self.__capacidade_atual -= 5
        if self.__capacidade_atual < 0:
            self.__capacidade_atual = 0