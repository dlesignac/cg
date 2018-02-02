import sys
import math

def dist(latA, lonA, latB, lonB):
    x = (lonB - lonA) * math.cos((latA + latB) / 2)
    y = latB - latA
    return math.sqrt(x * x + y * y) * 6371

lon = float(input().replace(",", "."))
lat = float(input().replace(",", "."))

n = int(input())
min = float('Inf')
min_v = ""

for i in range(n):
    defib = input().replace(",", ".").split(";")
    d = dist(float(defib[5]), float(defib[4]), lat, lon)
    
    if d < min:
        min = d
        min_v = defib[1]

print(min_v)
