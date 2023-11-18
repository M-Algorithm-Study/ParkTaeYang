n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))

stack = []
for x in range(n):
    for y in range(n):
        if l[y][x] == 9:
            startx,starty = x,y