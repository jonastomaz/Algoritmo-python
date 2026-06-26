#Imagine um sensor de velocidade que monitora gatos em uma pista. O programa deve:
#• Solicitar a velocidade (em km/h) de um gato.
#• Exibir:
#– Velocidade < 5: “Gato pregui¸coso”
#– Velocidade entre 5 e 15: “Gato normal”
#– Velocidade > 15: “Gato turbo! Cuidado!”
#Exemplo de Entrada:
#12
#Exemplo de Sa´ıda:
#Gato normal

velocidade = float(input('qual a velocidade do gato em km/h? '))

if (velocidade < 5):
    print('gato preguiçoso')

elif (velocidade <= 5 and velocidade <= 15):
    print('gato normal')

else:
    print('gato turbo cuidado')