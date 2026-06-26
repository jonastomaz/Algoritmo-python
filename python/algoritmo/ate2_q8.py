#Crie um programa que calcule o pre¸co a pagar pelo fornecimento de energia el´etrica.
#Pergunte a quantidade de kWh consumida e o tipo de instala¸c˜ao: R para residˆencias, I para
#ind´ustrias e C para com´ercios. Calcule o pre¸co a pagar conforme a tabela a seguir.
#Tipo Faixa (KWh) Pre¸co
#Residencial At´e 500 Acima de 500 R$ 0,40 R$ 0,65
#Comercial At´e 1000 Acima de 1000 R$ 0,55 R$ 0,60
#Industrial At´e 5000 Acima de 5000 R$ 0,55 R$ 0,60

kwh_cons = float(input('quantos KWH foi consumido? '))
tipo_inst = input('qual o tipo de instalação (R , I ou C): ')
tipo_inst = tipo_inst.lower()

if (kwh_cons <= 500) and (tipo_inst == 'r'):
    print(f'o preco a pagar e {kwh_cons * 0.4:.2f}')

elif (kwh_cons > 500) and (tipo_inst == 'r'):
    print(f'o preco a pagar e {kwh_cons * 0.65:.2f}')

elif (kwh_cons <= 1000) and (tipo_inst == 'c'):
    print(f'o preco a pagar e {kwh_cons * 0.55:.2f}')

elif (kwh_cons > 1000) and (tipo_inst == 'c'):
    print(f'o preco a pagar e {kwh_cons * 0.6:.2f}')

elif (kwh_cons <= 5000) and (tipo_inst == 'i'):
    print(f'o preco a pagar e {kwh_cons * 0.55:.2f}')

elif (kwh_cons > 5000) and (tipo_inst == 'c'):
    print(f'o preco a pagar e {kwh_cons * 0.6:.2f}')