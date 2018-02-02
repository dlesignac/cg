L_ =  1
R_ = -1
T_ =  2
B_ = -2

roomT = {
    ( 1, L_): B_, ( 1, R_): B_, ( 1, T_): B_,
    ( 2, L_): R_, ( 2, R_): L_, ( 3, T_): B_,
    ( 4, R_): B_, ( 4, T_): L_, ( 5, L_): B_,
    ( 5, T_): R_, ( 6, L_): R_, ( 6, R_): L_,
    ( 7, R_): B_, ( 7, T_): B_, ( 8, L_): B_,
    ( 8, R_): B_, ( 9, L_): B_, ( 9, T_): B_,
    (10, T_): L_, (11, T_): R_, (12, R_): B_,
    (13, L_): B_
}


def coords(x, y, rt, in_):
    direction = roomT[(rt, in_)]
    
    if direction == L_:
        return (x - 1, y)
    elif direction == R_:
        return (x + 1, y)
    
    return (x, y + 1)


w, h = [int(i) for i in input().split()]
maze = []

for j in range(h):
    line  = [int(i) for i in input().split()]
    maze += line

exit = int(input())


while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    
    if pos == "TOP":
        in_ = T_
    elif pos == "LEFT":
        in_ = L_
    else:
        in_ = R_
        
    x, y = coords(xi, yi, maze[yi * w + xi], in_)

    print("{} {}".format(x, y))
