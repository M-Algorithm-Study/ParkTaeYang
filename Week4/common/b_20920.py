import sys
input = sys.stdin.readline
m,n = map(int,input().split())
dic = {}
l = []
for i in range(m):
    word = input().rstrip()
    if len(word)>=n:
        dic[word] = dic.get(word,0)+1


for key, values in dic.items():
    l.append((key,values))

l.sort(key =lambda x : (-x[1],-len(x[0]),x[0]) )


for j in l:
    print(j[0])