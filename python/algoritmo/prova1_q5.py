# Um zool´ogico decidiu categorizar os animais com base no n´umero de patas. O programa deve:
#• Pedir o n´umero de patas do animal.
#• Exibir a categoria:
#– 2 patas: “Ave ou humano.”
#– 4 patas: “Mam´ıfero ou r´eptil.”
#– 8 patas: “Aracn´ıdeo.”
#– Outro valor: “Categoria desconhecida.”
#Exemplo de Entrada:
#4
#Exemplo de Sa´ıda:
#Mam´ıfero ou r´eptil.

num_patas = int(input('diga quantas patas o animal possui: '))

if (num_patas == 2):
    print('ave ou humano')

elif (num_patas == 4):
    print('mamifero ou reptil')

elif (num_patas == 8):
    print('aracnideo')

else:
    print('categoria desconhecida')