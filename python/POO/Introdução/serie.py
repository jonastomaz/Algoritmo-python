class Fibonacci:
    def __init__(self, quant_num_serie):
        if quant_num_serie <= 0:
            raise ValueError (f'O valor de {quant_num_serie} deve ser maior que zero')
        self.__serie = quant_num_serie

    @property
    def termos_serie(self):
        return self.__gerar_serie()

    def __gerar_serie(self):
        termos = [1, 1]
        for _ in range(2, self.__serie):
            termo_atual = termos[-1] + termos[-2]
            termos.append(termo_atual)

        return termos



sequencia = Fibonacci(1000000)
print(sequencia.termos_serie)