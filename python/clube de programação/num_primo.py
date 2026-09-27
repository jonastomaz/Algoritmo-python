def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  
            
    return True

N = int(input())
for _ in range(N):
    X = int(input())
    if eh_primo(X):
        print("Prime")
    else:
        print("Not Prime")