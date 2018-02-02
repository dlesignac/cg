w, h = [int(i) for i in input().split()]
n = int(input())
x, y = [int(i) for i in input().split()]

xmin, ymin = (0,0)
xmax, ymax = (w - 1, h - 1)

while True:
    bomb_dir = input()
    
    if "D" in bomb_dir:
        ymin = y + 1
        y = ymin + (int) ((ymax - y) / 2)
    elif "U" in bomb_dir:
        ymax = y - 1
        y = ymax + (int) ((ymin - y) / 2)
    if "R" in bomb_dir:
        xmin = x + 1
        x = xmin + (int) ((xmax - x) / 2)
    elif "L" in bomb_dir:
        xmax = x - 1
        x = xmax + (int) ((xmin - x) / 2)

    print("{} {}".format(x, y))
