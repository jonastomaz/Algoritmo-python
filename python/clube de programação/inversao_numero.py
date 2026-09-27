n = int(input())

du = (n % 10) * 100
n = n // 10
dm = n % 10 * 10
n = n // 10
dp = n % 10

print(f'Invertido = {du + dm + dp}')