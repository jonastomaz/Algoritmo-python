while True:
    try:
        n = int(input())
    except EOFError:
        break

    resto = 0
    quantidade = 0

    while True:
        resto = (resto * 10 + 1) % n
        quantidade += 1

        if resto == 0:
            break

    print(quantidade)