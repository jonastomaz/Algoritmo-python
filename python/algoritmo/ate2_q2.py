#Crie um programa em Python que ajude a decidir qual ´e o melhor combust´ıvel para abastecer
#um carro, considerando o pre¸co e o rendimento. Pe¸ca ao usu´ario para inserir o pre¸co do etanol e
#da gasolina, bem como o consumo m´edio do carro com cada um dos combust´ıveis. Com base nas
#informa¸c˜oes, determine se ´e mais vantajoso abastecer com etanol ou gasolina e imprima a
#decis˜ao.

preco_gas = float(input('qual o preco da gasolina? '))
preco_eta = float(input('qual o preco do etanol? '))
consumo_med_gas = float(input('quantos km o carro faz com gasolina? '))
consumo_med_eta = float(input('quantos km o carro faz com etanol? '))

rend_gas = preco_gas / consumo_med_gas
rend_eta = preco_eta / consumo_med_eta

if (rend_eta < rend_gas):
    print('melhor abastecer com etanol')

else:
    print('melhor abstecer com gasolina')