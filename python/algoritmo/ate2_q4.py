#Fa¸ca um programa que pe¸ca ao usu´ario o comprimento dos trˆes lados de um triˆangulo. O
#programa deve classificar o triˆangulo em:
#• Equil´atero: todos os lados s˜ao iguais;
#• Is´osceles: dois lados s˜ao iguais;
#• Escaleno: todos os lados s˜ao diferentes.

lado_a = float(input('qual o comprimento do lado A? '))
lado_b = float(input('qual o comprimento do lado B? '))
lado_c = float(input('qual o comprimento do lado C? '))

if (lado_a + lado_b < lado_c) and (lado_a + lado_c < lado_b) and (lado_b + lado_c < lado_a):
    print('essa figura nao e um triangulo')

else:
    if (lado_a != lado_b != lado_c):
        print('triangulo escaleno')

    elif (lado_a == lado_b == lado_c):
        print('triangulo equilatero')
    
    else:
        print('triangulo isoscelos')