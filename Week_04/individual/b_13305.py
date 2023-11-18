a=  int(input())
dis = list(map(int,input().split()))
op = list(map(int,input().split()))
total = 0
oil = op[0]
for i in range(a-1):
    if oil>op[i]:
        oil=op[i]
    total += oil*dis[i]

print(total)