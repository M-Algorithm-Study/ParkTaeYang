a,b = map(int,input().split())
d = [(0,1),(1,0),(0,-1),(-1,0)]
k = int(input())
if a*b<k:
    print(0)
else:
    l = [[0]*a for _ in range(b)]
    x,y = 0,0
    t = 0
    cnt = 1
    for i in range(a*b):
        if l[y][x] == 0:
            l[y][x] = cnt
            cnt+=1
        
        
        for _ in range(4):
            dx,dy = d[t]
            if 0<=y+dy<b and 0<=x+dx<a:
                if l[y+dy][x+dx] == 0:
                    y = y+dy
                    x = x+dx
                    break
                else:
                    t = (t+1)%4
            else:
                t = (t+1)%4
            
    
    for x in range(a):
        for y in range(b):
            if l[y][x] == k:
                print(x+1, y+1)