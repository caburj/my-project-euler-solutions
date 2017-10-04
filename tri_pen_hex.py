tri = lambda n : n * (n+1) // 2
pen = lambda n : n * (3*n-1) // 2
hex = lambda n : n * (2*n-1)

i, j, k = 0, 0, 0

tris = list(tri(x) for x in range(300000))
pens = list(pen(x) for x in range(200000))
hexs = list(hex(x) for x in range(150000))

for t in tris:
    if t in pens and t in hexs:
        print(t)
        
print(list(map(max, [tris, pens, hexs])))