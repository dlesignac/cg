sn = int(input())

for i in range(sn):
    lx, ly = [int(j) for j in input().split()]

while True:
    x, y, vx, vy, f, r, p = [int(i) for i in input().split()]

    if vy <= -40:
        print("0 4")
    elif vy <= -38:
        print("0 3")
    elif vy <= -35:
        print("0 2")
    else:
        print("0 0")

