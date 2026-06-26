from QUESTAO_3 import televisao

tv1 = televisao('samsung', 10, '50B')
tv2 = televisao('LG', 30, '65UP')

#TV 1
tv1.ligar_tv()
print(tv1.ligada_ou_nao())
try:
    tv1.mudar_canal(9)
    tv1.mudar_canal(17)
except ValueError as erro:
    print('canal invalido')
tv1.desligar_tv()
tv1.ligada_ou_nao()

#TV 2
tv2.ligar_tv()
print(tv2.ligada_ou_nao())
try:
    tv2.mudar_canal(14)
    tv2.mudar_canal(100)
except ValueError as erro:
    print('canal invalido')
tv1.desligar_tv()
tv2.ligada_ou_nao()