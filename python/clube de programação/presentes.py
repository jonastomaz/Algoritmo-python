import sys
dados = list(map(int, sys.stdin.buffer.read().split()))
i = 0

while i < len(dados):
    n = dados[i]
    i += 1

    if n == 0:
        break

    presentes = dados[i:i + 2 * n]
    i += 2 * n
    maior = 0
    menor = 10**18

    for j in range(n):
        par = presentes[j] + presentes[2 * n - 1 - j]

        if par > maior:
            maior = par

        if par < menor:
            menor = par

    print(maior, menor)