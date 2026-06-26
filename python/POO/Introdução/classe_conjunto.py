#Escreva uma classe Conjunto para representar um conjunto matemático, e que contenha os métodos a seguir:
#- add: adiciona um elemento ao conjunto se não pertence ao conjunto
#- contém: determina se um elemento pertence ou não pertence ao conjunto
#- união: retorna o conjunto união entre dois conjuntos 
# (i.e., os elementos combinados dos conjuntos, sem repetição)
#- interseção: retorna o conjunto interseção entre dois conjuntos 
# (i.e. os elementos que pertencem aos conjuntos, sem repetição)
#- diferença: retorna o conjunto diferença entre dois conjuntos 
# (i.e. os elementos que pertencem ao primeiro conjunto e que não pertencem ao segundo conjunto)


class Conjunto:

    def __init__(self, elementos=None):
        self.__elementos = []
        if elementos is not None:
            self.__elementos = elementos

    @property
    def elementos(self):
        return self.__elementos

    def contem(self, valor):
        return valor in self.__elementos

    def adicionar(self, elemento):
        if self.contem(elemento):
            raise ValueError(f'O elemento {elemento} já está no conjunto!')
        self.__elementos.append(elemento)

    def uniao(self, conjunto):
        conj_uniao = self.__copiar_conjunto()
        for elemento in conjunto.__elementos:
            if not conj_uniao.contem(elemento):
                conj_uniao.adicionar(elemento)
        return conj_uniao

    def intersecao(self, conjunto):
        conj_intersecao = Conjunto()
        for elemento in self.__elementos:
            if conjunto.contem(elemento):
                conj_intersecao.adicionar(elemento)
        return conj_intersecao

    def diferenca(self, conjunto):
        conj_diferenca = Conjunto()
        for elemento in self.__elementos:
            if not conjunto.contem(elemento):
                conj_diferenca.adicionar(elemento)
        return conj_diferenca

    def __copiar_conjunto(self):
        auxilia = Conjunto()
        for elemento in self.__elementos:
            auxilia.add(elemento)
        return auxilia
