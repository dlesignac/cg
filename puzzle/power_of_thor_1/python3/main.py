a, b, x, y = [int(i) for i in input().split()]

while True:
    input()
    r = ""

    if b > y:
        r = "S"
        y += 1
    if b < y:
        r = "N"
        y -= 1
    if a > x:
        r += "E"
        x += 1
    if a < x:
        r += "W"
        x -= 1

    print(r)
