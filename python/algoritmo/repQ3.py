#Escreva um programa que calcula o fatorial de um n´umero dado pelo usu´ario usando um loop for
#ou while. O fatorial de um n´umero n ´e o produto de todos os inteiros positivos menores ou iguais a n.

num = int(input('informe um numeo: '))
fat = 1

for i in range(1, num+1):
    fat *= i

print(f'o fatorial de {num} e: {fat}')