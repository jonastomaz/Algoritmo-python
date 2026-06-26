#Escreva um programa em Python que determine se um ano ´e um ano de Copa do Mundo da
#FIFA. Os anos de Copa do Mundo s˜ao aqueles que ocorrem a cada 4 anos, come¸cando a partir
#de 1930. Pe¸ca ao usu´ario para inserir um ano, e o programa deve imprimir se ´e um ano de Copa
#do Mundo ou n˜ao.

ano_copa = int(input('digite um ano para saber se teve/tem copa do mundo: '))

if (ano_copa < 1930):
    print('antes do ano de 1930 nao teve copa')

elif ((ano_copa - 1930)%4 == 0):
    print('esse ano teve copa do mundo')

else:
    print('esse ano nao teve copa')