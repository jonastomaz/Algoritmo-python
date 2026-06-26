class representa_reta:

    def __init__(self, coeficiente_angular, coeficiente_linear):
        self.coeficiente_angulo = coeficiente_angular
        self.coeficiente_linear = coeficiente_linear

    
    def mudar_coeficiente_angular(self, novo_coeficiente):
        self.coeficiente_angulo = novo_coeficiente

    
    def mudar_coeficiente_linear(self, novo_coeficiente):
        self.coeficiente_linear = novo_coeficiente

    
    def obter_coeficiente_angular(self):
        return self.coeficiente_angulo

    
    def obter_coeficiente_linear(self):
        return self.coeficiente_linear


    def forma_alfanumerio(self):
        return f'y = {self.coeficiente_angulo}x + {self.coeficiente_linear}'


    def ponto_pertence_reta(self, x, y):
        if y == self.coeficiente_angulo * x + self.coeficiente_linear:
            return f'esse ponto pertence a reta'
        else:
            return f'o ponto nao pertence a reta'