#Escreva um programa que imprima uma pirˆamide de asteriscos com uma altura especificada pelo
#usu´ario. Por exemplo, se o usu´ario inserir 5 como altura da pirˆamide, o programa deve imprimir:

alt = int(input('informe o tamanho da piramide: '))

for i in range(1, alt + 1):
    print(f'{" " * ((alt) - i)}{"*" * ((i*2)-1)}')

print('piramide ao contrario')
print(' ')
for i in range(alt, 0, -1):
    print(f'{" " * (alt-i)}{"*" * ((i*2)-1)}')

print(' ')
print('piramide lado direito')
for i in range(1, alt + 1):
    print("*" * ((i*2)-1))
for i in range(alt - 1, 0, -1):
    print("*" * ((i*2)-1))

print(' ')
print('piramide lado esquerdo')
for i in range(1, alt + 1):
    print(f'{" " * (alt - i)}{"*" * i}')
for i in range(alt - 1, 0, -1):
    print(f'{" " * (alt - i)}{"*" * i}')