n = int(input())
dic = {'ChongChong' : 1}
for i in range(n):
    a,b = input().split()
    dic[a] = dic.get(a, 0)
    dic[b] = dic.get(b, 0)
    if dic[a] >= 1 or dic[b] >= 1:
        dic[a] = dic.get(a, 0) + 1
        dic[b] = dic.get(b, 0) + 1

value = dic.values()
ans = 0
for i in value:
    if i>=1:
        ans +=1
print(ans)