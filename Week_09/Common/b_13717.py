def count_evo(y,x):
    cnt = 0
    while x>=y:
        cnt += x//y
        x = x%y + 2*(x//y)
    return cnt  

n = int(input())
p = input()
k,m = map(int,input().split())
max_evo = count_evo(k,m)
max_name = p
sum_evo = max_evo

for i in range(n-1):
    p = input()
    cnt = 0
    k,m = map(int,input().split())
    t = count_evo(k,m)
    sum_evo +=t
    if t> max_evo:
        max_evo = t
        max_name = p


print(sum_evo)
print(max_name)
   
        