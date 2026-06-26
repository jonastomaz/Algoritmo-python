from QUESTAO_1 import funcionario

funcionario_1 = funcionario('jonas',100, 'teste', 100)
funcionario_1.aumento_percentual(10)
print(funcionario_1.ganho_por_ano())


funcionario_2 = funcionario('tarcisio', 200, 'programador', 200)
funcionario_2.aumento_percentual(10)
print(funcionario_2.ganho_por_ano())