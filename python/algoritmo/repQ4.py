#Escreva um programa em Python que solicita ao usu´ario uma string e conta quantas vezes uma
#determinada letra aparece nessa string.

palavra = input('digite uma palavra: ').lower()
letra = input('informe uam letra para saber quantas tem na palavra: ').lower()
count = 0

for i in palavra:
    if letra == i:
        count += 1

print(count)