# Imagine uma caixa de xadrez de 8x8. Cada quadrado tem um gr˜ao de trigo, e o n´umero de gr˜aos
#dobra a cada quadrado. O primeiro quadrado tem um gr˜ao, o segundo tem dois, o terceiro tem quatro, e assim
#por diante. Quantos gr˜aos de trigo existem no total? Crie um programa em Python que calcula esse problema

grao = 1
total = 0
casa = int(input('informe qual casa voce quer saber a quantidade de graos: '))
for i in range(casa):
    total += grao
    grao *= 2

print(total)