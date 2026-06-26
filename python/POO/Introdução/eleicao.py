#Em uma eleição presidencial existem quatro candidatos e os votos são informados pelos eleitores 
#escolhendo-se um dos seguintes números: 1 para voto no candidato A: 2 
#para voto no candidato B, 3 para voto no candidato C, 4 para voto no candidato D, 
#5 para voto branco, e qualquer outro número para voto nulo. 
#Escreva um programa em Python para ler 1000 votos e calcular e imprimir o total de votos para cada candidato,
#o total de votos nulos, o total de votos em branco, e o percentual de votos válidos



def contagem_votos(num_candidato):

    candidato_A = 0
    candidato_B = 0
    candidato_C = 0
    candidato_D = 0
    votos_nulos = 0
    votos_brancos = 0

    for voto in num_candidato:
        if voto == 1:
            candidato_A += 1
        elif voto == 2:
            candidato_B += 1
        elif voto == 3:
            candidato_C += 1
        elif voto == 4:
            candidato_D += 1
        elif voto == 5:
            votos_brancos += 1
        else:
            votos_nulos += 1

    total_votos_validos = candidato_A + candidato_B + candidato_C + candidato_D 

    percentual_validos = (total_votos_validos / len(num_candidato)) * 100

    resultado = (f'Total de votos para o candidato A: {candidato_A}\n'
                 f'Total de votos para o candidato B: {candidato_B}\n'
                 f'Total de votos para o candidato C: {candidato_C}\n'
                 f'Total de votos para o candidato D: {candidato_D}\n'
                 f'Total de votos nulos: {votos_nulos}\n'
                 f'Total de votos em branco: {votos_brancos}\n'
                 f'Percentual de votos válidos: {percentual_validos}')

    return resultado

votos_usuario = []

for i in range(1000):
    voto = int(input(f"Digite o voto {i + 1}: "))
    votos_usuario.append(voto)

resultados = contagem_votos(votos_usuario)
print(resultados)