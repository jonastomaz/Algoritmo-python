#Uma empresa precisa calcular o imposto baseado no sal´ario do funcion´ario. O programa deve:
#• Solicitar o sal´ario do funcion´ario.
#• Exibir o imposto:
#– Sal´ario ≤ R$2000: “Isento.”
#– Sal´ario entre R$2001 e R$5000: “Imposto de 10%.”
#– Sal´ario > R$5000: “Imposto de 20%.”
#4500
#Exemplo de Sa´ıda:
#Imposto de 10%.

salario = float(input('qual seu salario? '))

if (salario <= 2000):
    print('isento')

elif (salario <= 5000):
    print('imposto de 10%')

else:
    print('imposto de 20%')