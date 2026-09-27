while True:
    G, P = map(int, input().split())

    if G == 0 and P == 0:
        break

    corridas = []
    for _ in range(G):
        corrida = list(map(int, input().split()))
        corridas.append(corrida)

    S = int(input())

    for _ in range(S):
        sistema = list(map(int, input().split()))

        K = sistema[0]
        pontos = sistema[1:]

        total = [0] * P
        for corrida in corridas:
            for piloto in range(P):
                posicao = corrida[piloto]
                if posicao <= K:
                    total[piloto] += pontos[posicao - 1]

        maior = max(total)

        campeoes = []

        for piloto in range(P):
            if total[piloto] == maior:
                campeoes.append(piloto + 1)

        print(*campeoes)