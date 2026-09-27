def gerar_primos(n):
    primos = []
    num = 2
    while len(primos) < n:
        primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primo = False
                break
        if primo:
            primos.append(num)
        num += 1
    return primos


def josephus(n):
    pessoas = list(range(1, n + 1))
    primos = gerar_primos(n)
    posicao = 0
    for i in range(n - 1):
        posicao = (posicao + primos[i] - 1) % len(pessoas)
        pessoas.pop(posicao)
    return pessoas[0]

n = -1
while n != 0:
    n = int(input())
    if n != 0:
        print(josephus(n))