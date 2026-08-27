def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def digitos_primos(n):
    for i in str(n):
        if i not in ["2","3","5","7"]:
            return False
    return True

while True:
    try:
        n = int(input())
    except EOFError:
        break

    if eh_primo(n):
        if digitos_primos(n):
            print("Super")
        else:
            print("Primo")
    else:
        print("Nada")