def josefos(n, k):
    sobrevivente = 0
    for i in range(2, n + 1):
        sobrevivente = (sobrevivente + k) % i

    return sobrevivente + 1


NC = int(input())

for caso in range(1, NC + 1):
    n, k = map(int, input().split())

    resultado = josefos(n, k)

    print(f"Caso {caso}: {resultado}")