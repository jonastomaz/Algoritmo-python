#Uma lanchonete lançou uma oferta relâmpago de lanches conforme a tabela abaixo. 
# Os clientes podem fazer os seus pedidos livremente, solicitando vários tipos de lanches num mesmo pedido. 
# Escreva uma classe Pedido que represente um pedido de um cliente e que contenha os métodos a seguir:
#- construtor: parametrizado com o nome do cliente e opcionalmente uma lista de códigos de lanches 
# para o pedido. Se houver uma lista de códigos, deve haver uma validação para verificar se correspondem 
# aos códigos da tabela abaixo.
#- métodos acessores do tipo get
#- adicionar: adiciona um código de lanche ao pedido. Deve haver uma validação para verificar se o código 
# existe na tabela abaixo
#- remover: remove um código de lanche do pedido. Deve haver uma validação para verificar se 
# o código existe no pedido
#- calcular total: retorna o valor total a ser pago pelo pedido, considerando os preços 
# conforme a tabela abaixo.
#CÓDIGO    LANCHE         PREÇO
#101           Suco                R$2,50
#102           Refrigerante   R$3,50
#103           Bauru              R$1,50
#104           Misto               R$2,00
#105           Burguer           R$3,00
#106           X-Burger          R$3,50
#107           X-Egg               R$3,50


class Pedido:

    def __init__(self, nome_cliente, lanches=None):
        self.__cliente = nome_cliente
        self.__codigos = {
            101: 2.5,
            102: 3.5,
            103: 1.5,
            104: 2,
            105: 3,
            106: 3.5,
            107: 3.5
        }
        self.__lanches = []
        if lanches is not None:
            self.__validar_lanches(lanches)
            self.__lanches = lanches

    @property
    def cliente(self):
        return self.__cliente

    @property
    def lanches(self):
        return self.__lanches

    def adicionar_lanche(self, codigo):
        self.__validar_pedido(codigo)
        self.__lanches.append(codigo)

    def remover_lanche(self, codigo):
        for codigo in self.__lanches:
            self.__lanches.remove(codigo)
        else:
            return f'o codigo {codigo} nao esta no pedido'

    def calcular_total(self):
        total = 0
        for codigo in self.__lanches:
            total += self.__codigos[codigo]
        return total

    def __validar_lanches(self, lanches):
        for codigo in lanches:
            self.__validar_pedido(codigo)

    def __validar_pedido(self, codigo):
        for codigo in self.__codigos:
            self.__codigos[codigo]
        else:
            raise ValueError(f'esse codigo {codigo} nao esta disponivel')