import sys

dados = list(map(int, sys.stdin.buffer.read().split()))

i = 0

while i < len(dados):
    X = dados[i]
    Y = dados[i + 1]
    M = dados[i + 2]
    i += 3

    for _ in range(M):
        Xi = dados[i]
        Yi = dados[i + 1]
        i += 2

        if (Xi <= X and Yi <= Y) or (Xi <= Y and Yi <= X):
            print("Sim")
        else:
            print("Nao")