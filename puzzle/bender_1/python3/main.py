import sys
import math

class Bender:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        
        self.b = False
        self.i = False
    
    
class Board:
    SOUTH = 0
    EAST  = 1
    NORTH = 2
    WEST  = 3
    
    def __init__(self):
        self.h, self.w = [int(i) for i in input().split()]
        self.m = []

        for i in range(self.h):
            line    = list(input())
            self.m += line
    
    def entry(self):
        z = self.m.index("@")
        return (z % self.w, z // self.w)
    
    def teleport(self, x, y):
        for i in range(self.w * self.h):
            x_ = i % self.w
            y_ = i // self.w
            
            if self.m[i] == "T" and (x_ != x or y_ != y):
                return (x_, y_)
    
    def exit(self):
        z = self.m.index("$")
        return (z % self.w, z // self.w)
    
    def at(self, x, y):
        return self.m[x + self.w * y]
        
    def neigh(self, x, y, d):
        if d == Board.SOUTH:
            return (x, y+1)
        elif d == Board.EAST:
            return (x+1, y)
        elif d == Board.NORTH:
            return (x, y-1)
        elif d == Board.WEST:
            return (x-1, y)
    
    def destroy(self, x, y):
        self.m[x + self.w * y] = " "

s = ""
B = Board()
x, y = B.entry()
b = Bender(x, y, 0)
loop = False
track = []

while (b.x, b.y) != B.exit() and not loop:
    x, y = B.neigh(b.x, b.y, b.d)
    dd   = B.at(x, y)

    if dd == "#" or (dd == "X" and not b.b):
        x0, y0 = B.neigh(b.x, b.y, 0)
        x1, y1 = B.neigh(b.x, b.y, 1)
        x2, y2 = B.neigh(b.x, b.y, 2)
        x3, y3 = B.neigh(b.x, b.y, 3)
        
        d0 = B.at(x0, y0)
        d1 = B.at(x1, y1)
        d2 = B.at(x2, y2)
        d3 = B.at(x3, y3)
        
        if not b.i:
            if d0 != "#" and (d0 != "X" or b.b):
                b.d = 0
            elif d1 != "#" and (d1 != "X" or b.b):
                b.d = 1
            elif d2 != "#" and (d2 != "X" or b.b):
                b.d = 2
            else:
                b.d = 3
        else:
            if d3 != "#" and (d3 != "X" or b.b):
                b.d = 3
            elif d2 != "#" and (d2 != "X" or b.b):
                b.d = 2
            elif d1 != "#" and (d1 != "X" or b.b):
                b.d = 1
            else:
                b.d = 0
            
    else:
        x, y = B.neigh(b.x, b.y, b.d)
        
        if dd == "X":
            B.destroy(x, y)
            track = []
        
        b.x = x
        b.y = y
        
        if   b.d == 0: s += "SOUTH\n"
        elif b.d == 1: s += "EAST\n"
        elif b.d == 2: s += "NORTH\n"
        elif b.d == 3: s += "WEST\n"
        
        c = B.at(b.x, b.y)
        if c == "S":
            b.d = Board.SOUTH
        elif c == "E":
            b.d = Board.EAST
        elif c == "N":
            b.d = Board.NORTH
        elif c == "W":
            b.d = Board.WEST
        elif c == "I":
            b.i = not b.i
        elif c == "B":
            b.b = not b.b
        elif c == "T":
            b.x, b.y = B.teleport(b.x, b.y)
    
    if (b.x, b.y, b.d, b.b, b.i) in track:
        s = "LOOP"
        loop = True
    else:
        track.append((b.x, b.y, b.d, b.b, b.i))

print(s)
