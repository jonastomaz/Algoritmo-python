import sys

def main():
    entrada = sys.stdin.buffer.read().split()
    n, x = int(entrada[0]), int(entrada[1])
    ataque = entrada[2] 
    p, m, g = int(entrada[3]), int(entrada[4]), int(entrada[5])

    tamanhos = [0] * 128
    tamanhos[ord('P')] = p
    tamanhos[ord('M')] = m
    tamanhos[ord('G')] = g

    sz = 1
    while sz < n:
        sz *= 2
    tree = [-1] * (2 * sz)
    qtd_muralhas = 0  

    for titã in ataque:
        tamanho = tamanhos[titã]
        node = 1
        if tree[1] >= tamanho:
            while node < sz:
                esquerda = node + node
                node = esquerda if tree[esquerda] >= tamanho else esquerda + 1
            tree[node] -= tamanho
        else:
            node = qtd_muralhas + sz
            tree[node] = x - tamanho
            qtd_muralhas += 1
        node //= 2
        while node:
            a = tree[node + node]
            b = tree[node + node + 1]
            tree[node] = a if a > b else b
            node //= 2

    print(qtd_muralhas)

main()