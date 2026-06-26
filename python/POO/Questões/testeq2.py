from QUESTAO_2 import representa_reta

reta = representa_reta(3, 2)

reta.mudar_coeficiente_angular(2)

reta.mudar_coeficiente_linear(3)

print(reta.obter_coeficiente_angular)

print(reta.obter_coeficiente_linear)

print(reta.forma_alfanumerio)

print(reta.ponto_pertence_reta(3,4))