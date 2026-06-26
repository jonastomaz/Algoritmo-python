class funcionario:

    def __init__(self, nome_funcionario, cod_funcionario, cargo_exercido, salario_mensal):
        self.nome_funcionario = nome_funcionario
        self.cod_funcionario = cod_funcionario
        self.cargo_exercido = cargo_exercido
        self.salario_mensal = salario_mensal


    def aumento_percentual(self, reajuste_percentual):
        salario_inicio = self.salario_mensal
        salario_reajustado = (self.salario_mensal * reajuste_percentual) / 100 + salario_inicio
        self.salario_mensal = salario_reajustado

    
    def ganho_por_ano(self):
        return f'salario anual e {self.salario_mensal * 12}'
