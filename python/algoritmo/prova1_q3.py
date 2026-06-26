#Uma academia decidiu criar um programa para classificar o n´ıvel de esfor¸co dos alunos. O
#programa deve:
#• Solicitar o n´umero de horas semanais de exerc´ıcio.
#• Exibir a classifica¸c˜ao:
#– < 2 horas: “Iniciante.”
#– Entre 2 e 5 horas: “Regular.”
#– > 5 horas: “Atleta!”
#Exemplo de Entrada:
#6
#Exemplo de Sa´ıda:
#Atleta!

num_horas = float(input('quantas horas na semana voce treinou? '))

if (num_horas < 2):
    print('inciante')

elif (num_horas <= 5):
    print('regular')

else:
    print('atleta')