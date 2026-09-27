import math
while True:
    try:
        M, N = map(int, input().split())
    except EOFError:
        break

    print(math.factorial(M) + math.factorial(N))