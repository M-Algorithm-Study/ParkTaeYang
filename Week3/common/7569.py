import sys
input = sys.stdin.readline
from collections import deque
a,b,hi= map(int,input().split())
l = [[] for _ in range(hi)]
for k in range(hi):
    for _ in range(b):
        l[k].append(list(map(int,input().split())))
d = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
def bfs():
    day = 0
    global zero_cnt
    deq = deque()                      
    for k in range(hi):
        for i in range(b):
            for j in range(a):
                if l[k][i][j] == 1:
                    deq.append((k,j,i,0))
    while deq:
        h,x,y,cnt = deq.popleft()
        if day<cnt:
            day = cnt
        for dh,dx,dy in d:
            mh = h+dh
            mx = x+dx
            my = y+dy
            if 0<=mx<a and 0<=my<b and 0<=mh<hi and l[mh][my][mx] == 0:
                l[mh][my][mx] = 1
                deq.append((mh,mx,my,cnt+1))
    for k in range(hi):
        for i in range(b):
            for j in range(a):
                if l[k][i][j] == 0:
                    return -1
    else:
        return day


print(bfs())