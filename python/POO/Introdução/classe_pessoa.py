#Escreva uma classe Pessoa para representar uma pessoa com um nome, um pai e uma mãe 
# (que também são objetos do tipo Pessoa). A classe deve conter os métodos a seguir:
#- construtor: parametrizado com o nome e os pais. 
# Caso o pai e/ou a mãe sejam desconhecidos, 
# deve-se passar o valor None como parâmetro na criação de uma pessoa
#- métodos acessores do tipo get
#- é igual: determina se duas pessoas são iguais, i.e. possuem mesmo nome e mesma mãe
#- é irmã: determina se duas pessoas são irmãs, i.e., possuem mesmo pai ou mesma mãe
#- é pai: determina se uma pessoa é pai de outra
#- é mãe: determina se uma pessoa é mãe de outra
#- info: retorna um texto contendo o nome da pessoa e os nomes de seus pais

class Pessoa:

    def __init__(self, nome, pai, mae):
        self.__nome = nome
        self.__pai = pai
        self.__mae = mae

    @property
    def nome(self):
        return self.__nome

    @property
    def pai(self):
        return self.__pai

    @property
    def mae(self):
        return self.__mae

    def e_igual(self, pessoa):
        return self != pessoa and self.__nome == pessoa.nome and self.__mae == pessoa.mae

    def e_irma(self, pessoa):
        return self != pessoa and (self.__pai == pessoa.pai or self.__mae == pessoa.mae)

    def e_pai(self, pessoa):
        return self != pessoa and self == pessoa.__pai

    def e_mae(self, pessoa):
        return self != pessoa and self == pessoa.__mae

    def info(self):
        return (f'Nome: {self.__nome}\n'
                f'\tPai: {self.__pai.__nome if self.__pai is not None else "desconhecido"}\n'
                f'\tMãe: {self.__mae.__nome if self.__mae is not None else "desconhecida"}')