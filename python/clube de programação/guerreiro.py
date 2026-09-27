while True:
    try:
        M, N = map(int, input().split())
    except EOFError:
        break

    print(f"{abs(M-N)}")