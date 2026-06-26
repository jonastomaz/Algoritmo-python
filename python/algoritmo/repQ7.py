# Se uma tartaruga est´a subindo um poste de 2 metros de altura e desce 1 metro a cada dia, mas a
#cada noite ela escorrega e desce 0.5 metros, em quantos dias ela chegar´a ao topo? Crie um programa em Python
#que fa¸ca esse c´alculo.

poste = 2
dias = 1
escalada = 0

while (escalada != poste):
    escalada += 1
    if (escalada != poste):
        dias += 1
        escalada -= 0.5
    

print(dias)

print('\n questao escada')
escada = 5
dia = 1
subida = 0

while (escada > subida):
    subida += 1
    if (subida < escada):
        dia += 1
        subida -= 0.3

print(dia)