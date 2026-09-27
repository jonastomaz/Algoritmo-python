while True:
    N, B = input().split()

    if N == "0" and B == "0":
        break

    N = N.zfill(max(len(N), len(B)))
    B = B.zfill(max(len(N), len(B)))

    cont = 0
    vai_um = 0

    for i in range(len(N) - 1, -1, -1):
        soma = int(N[i]) + int(B[i]) + vai_um

        if soma >= 10:
            cont += 1
            vai_um = 1
        else:
            vai_um = 0

    if cont > 1:
        print(f"{cont} operações de transporte.")
    elif cont == 1:
        print("1 operação de transporte.")
    else:
        print("Nenhuma operação de transporte.")