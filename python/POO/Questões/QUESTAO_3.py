class televisao:

    def __init__(self, marca, quantidade_canais, modelo):
        self.ligada = 0
        self.canal_atual = 1
        self.marca = marca
        self.quantidade_canais = quantidade_canais
        self.modelo = modelo


    def ligar_tv(self):
        if self.ligada == 0:
            self.ligada = 1
        else:
            return f'a televisao esta ligada'

    def desligar_tv(self):
        if self.ligada == 1:
            self.ligada = 0
        else:
            return f'a televisao esta desligada'

    def ligada_ou_nao(self):
        if self.ligada == 1:
            return f'a televisao esta ligada'
        else:
            return f'a televisao desligada'

    def mudar_canal(self, novo_numero_canal):
        self.canal_atual = novo_numero_canal


    def qual_canal_esta(self):
        return self.canal_atual