caso = 1

while True:
    try:
        n = int(input())
    except EOFError:
        break

    sequencia = "0"

    for i in range(1, n + 1):
        sequencia += (" " + str(i)) * i

    quantidade = n * (n + 1) // 2 + 1

    if quantidade == 1:
        print(f"Caso {caso}: 1 número")
    else:
        print(f"Caso {caso}: {quantidade} números")

    print(sequencia)
    print()
    
    caso += 1