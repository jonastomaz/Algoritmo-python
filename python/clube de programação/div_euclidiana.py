a, b = map(int, input().split())

r = a % abs(b)
q = (a - r) // b

print(q, r)