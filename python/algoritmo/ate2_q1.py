#. Fa¸ca um programa que pergunte o pre¸co de trˆes produtos e informe qual produto vocˆe deve
#comprar, sabendo que a decis˜ao ´e sempre pelo mais barato.

preco_1 = float(input('diga o preco do primeiro produto: '))
preco_2 = float(input('diga o preco do segundo produto: '))
preco_3 = float(input('diga o preco do terceiro produto: '))

if (preco_1 < preco_2) and (preco_1 < preco_3):
    print(f'voce deve comprar o primeiro produto')

elif (preco_2 < preco_3):
    print(f'voce deve comprar o segundo produto')

else:
    print(f'voce deve comprar o terceiro produto')