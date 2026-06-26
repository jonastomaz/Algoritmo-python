#Vocˆe foi contratado para programar um robˆo que decide o prato do dia baseado no saldo do
#cliente. O programa deve:
#• Solicitar o saldo do cliente.
#• Exibir o prato sugerido:
#– Saldo ≥ R$50: “Bife com batata frita”
#– Saldo ≥ R$20 e < R$50: “Macarr˜ao com molho”
#– Saldo ≥ R$10 e < R$20: “Sandu´ıche de presunto”
#– Saldo < R$10: “Bolacha ´agua e sal”
#Exemplo de Entrada:
#R$ 35
#Exemplo de Sa´ıda:
#Macarr~ao com molho

saldo = float(input('qual seu saldo? '))

if (saldo >= 50):
    print('bife com batata frita')

elif (saldo >= 20):
    print('macarrao com molho')

elif (saldo >= 10):
    print('sanduiche de presunto')

else:
    print('bolacha agua e sal')