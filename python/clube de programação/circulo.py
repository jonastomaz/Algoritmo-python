import math

while True:
    try:
        a, b, c = map(int, input().split())
    except EOFError:
        break

    p = (a + b + c) / 2

    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    r = area / p
    R = (a * b * c) / (4 * area)

    area_rosas = math.pi * r * r
    area_violetas = math.pi * R * R - area
    area_girassois = area - area_rosas

    print(f"{area_violetas:.4f} {area_girassois:.4f} {area_rosas:.4f}")