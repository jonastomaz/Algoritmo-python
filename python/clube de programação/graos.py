N = int(input())

for i in range(N):
    X = int(input())

    graos = 2 ** X - 1
    kg = graos // 12000

    print(f"{kg} kg")