#Crie um programa em Python que verifique se um ano ´e bissexto ou n˜ao. O usu´ario deve
#inserir o ano, e o programa deve imprimir se o ano ´e bissexto ou n˜ao seguindo as regras: anos
#divis´ıveis por 4 s˜ao bissextos, exceto anos divis´ıveis por 100 (a menos que tamb´em sejam
#divis´ıveis por 400).

ano = int(input('digite um ano: '))

if (ano%4 == 0) and (ano%100 != 0 or ano%400 == 0):
    print('esse ano e bissexto')

else:
    print('esse ano nao e bissexto')