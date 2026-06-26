#Escreva um programa que gere um n´umero secreto aleat´orio entre 1 e 100. O usu´ario tem 10
#tentativas para adivinhar o n´umero secreto. Ap´os cada tentativa, o programa deve informar 
# se o palpite ´e muito
#alto, muito baixo ou correto. O programa deve terminar quando o usu´ario adivinhar 
# corretamente o n´umero ou
#quando acabarem as tentativas.

import random

num = random.randint(1,100)
tent = 1
numero = int(input('informe um numero: '))

if (numero == num):
    print('numero correto')

else:
    while (tent < 10) and (num != numero):
        if (numero > num):
            print('numero digitado muito alto')
        
        else:
            print('numero muito abaixo')

        print(f'tentativa {tent}')
        tent += 1
        numero = int(input('informe um numero: '))

    if (numero == num):
        print('numero correto')
    
    else:
        print('numero de tentativas esgotados')