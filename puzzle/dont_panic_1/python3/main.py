class Floor:
    def __init__(self):
        self.managed = False
        self.objective = -1

nf, w, nr, ef, ep, nc, nae, ne = [int(i) for i in input().split()]
floors = [Floor() for i in range(nf)]

for i in range(ne):
    y, x = [int(j) for j in input().split()]
    floors[y].objective = x

floors[ef].objective = ep


while True:
    cy, cx, cd = input().split()
    cy = int(cy)
    cx = int(cx)
    
    obj_dir = -1
    
    if cx == -1:
        print("WAIT")
    else:
        if floors[cy].objective < cx:
            obj_dir = "LEFT"
        elif floors[cy].objective > cx:
            obj_dir = "RIGHT"
            
        _managed    = floors[cy].managed
        _blockElevU = cy != 0 and cx == floors[cy - 1].objective
        _blockElevD = cx == floors[cy].objective
        _rightDir   = cd == obj_dir
        
        if not _managed and not _blockElevU and not _blockElevD and not _rightDir:
            print("BLOCK")
            floors[cy].managed = True
        else:
            print("WAIT")
