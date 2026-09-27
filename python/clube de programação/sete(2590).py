import sys

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    ns = map(int, data[1:t + 1])
    digitos = "1793"
    saida = "\n".join(digitos[n % 4] for n in ns)
    sys.stdout.write(saida + "\n")

main()

t = int(input())
digitos = [1,7,9,3]
for i in range(t):
    n = int(input())
    print(digitos[n % 4])
