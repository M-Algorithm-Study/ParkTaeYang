N, S = map(int, input().split())
l = list(map(int, input().split()))

start, end = 0, 0
s = l[0]
ans = 100001

while True:
    if s < S:
        end += 1
        if end == N: 
            break
        s += l[end]
    else:
        s -= l[start]
        ans = min(ans, end-start+1)
        start += 1

if ans == 100001:        
    print(0)
else:
    print(ans)