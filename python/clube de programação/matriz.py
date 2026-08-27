while True:
    n = int(input())

    if n == 0:
        break

    matriz = []

    for i in range(n):
        linha = []

        for j in range(n):
            valor = 2 ** (i + j)
            linha.append(valor)

        matriz.append(linha)

    maior = matriz[n - 1][n - 1]

    tamanho = len(str(maior))

    for linha in matriz:
        print(" ".join(f"{valor:>{tamanho}}" for valor in linha))

    print()