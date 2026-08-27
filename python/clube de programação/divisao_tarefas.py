import sys

dados = list(map(int, sys.stdin.buffer.read().split()))

i = 0

while i < len(dados):
    n = dados[i]
    i += 1

    tarefas = dados[i:i + n]
    i += n

    total = sum(tarefas)
    rangel = 0
    menor = total

    for x in tarefas:
        rangel += x
        gugu = total - rangel

        diferenca = abs(rangel - gugu)

        if diferenca < menor:
            menor = diferenca

    print(menor)