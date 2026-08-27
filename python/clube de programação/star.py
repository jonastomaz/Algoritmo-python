n = int(input())
ovelhas = list(map(int, input().split()))

pos = 0
atacadas = set()

while 0 <= pos < n:
    atacadas.add(pos)
    quantidade = ovelhas[pos]

    if ovelhas[pos] > 0:
        ovelhas[pos] -= 1

    if quantidade % 2 == 0:
        pos -= 1
    else:
        pos += 1

print(len(atacadas), sum(ovelhas))