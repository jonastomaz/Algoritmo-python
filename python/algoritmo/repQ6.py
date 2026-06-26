#Um pal´ındromo ´e uma palavra que ´e lida da mesma forma de tr´as para frente. Por exemplo,
#’radar’ ´e um pal´ındromo. Escreva um programa que encontre e imprima todos os n´umeros pal´ındromos de 1 a
#1000.

num_palin = []
num = " "

for i in range(1, 1001):
    num = str(i)
    if num == num[::-1]:
        num_palin.append(num)

print(num_palin)