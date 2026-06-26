#Vocˆe est´a desenvolvendo um sistema de caixa para um supermercado. O sistema deve
#calcular o desconto aplicado a uma compra com base nas seguintes regras:
#• Se o valor da compra for maior que R$ 100, aplique um desconto de 10%;
#• Se o valor da compra for maior que R$ 200, aplique um desconto de 15%;
#• Se o valor da compra for maior que R$ 300, aplique um desconto de 20%.
#Escreva um programa que solicite o valor da compra e imprima o valor total com o desconto
#aplicado.

valor_compra = float(input('qual foi o valor da compra? '))

if (valor_compra > 300):
    print(f'o preco total a pagar com o desconto e {valor_compra * 0.8}')

elif (valor_compra > 200):
    print(f'o preco total a pagar com o desconto e {valor_compra * 0.85}')

elif (valor_compra > 100):
    print(f'o preco total a pagar com o desconto e {valor_compra * 0.9}')

else:
    print(f'o preco total a pagar e {valor_compra}')