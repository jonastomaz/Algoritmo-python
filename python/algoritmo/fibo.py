n = int(input('informe um numero: '))
fibonacci = []
a = 0 
b = 1
for i in range(n):
    a = a + b
    b = a - b
    fibonacci.append(a)

print(fibonacci)