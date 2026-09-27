N = int(input())
for _ in range(N):
    X = float(input())
    dias = 0
    while X > 1:
        X /= 2
        dias += 1
    print(f"{dias} dias")