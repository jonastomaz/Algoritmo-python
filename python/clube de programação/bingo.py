while True:
    N, B = map(int, input().split())

    if N == 0 and B == 0:
        break

    bolas = list(map(int, input().split()))

    diferencas = set()
    perfeito = True

    for i in range(B):
        for j in range(i + 1, B):
            d = abs(bolas[i] - bolas[j])
            if d in diferencas:
                perfeito = False
                break
            diferencas.add(d)
        if not perfeito:
            break

    if perfeito and len(diferencas) == N:
        print("Y")
    else:
        print("N")