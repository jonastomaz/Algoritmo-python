def eh_pico(n, h):
    for i in range(n - 1):
        if i % 2 == 0:
            if h[i] >= h[i + 1]:
                return False
        else:
            if h[i] <= h[i + 1]:
                return False

    return True


def eh_vale(n, h):
    for i in range(n - 1):
        if i % 2 == 0:
            if h[i] <= h[i + 1]:
                return False
        else:
            if h[i] >= h[i + 1]:
                return False

    return True


n = int(input())
h = list(map(int, input().split()))

if eh_pico(n, h) or eh_vale(n, h):
    print(1)
else:
    print(0)