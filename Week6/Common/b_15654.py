n, m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
l = []
check = [False]*n
def recur(num):
    if num == m:
        return print(*l)
    else:
        for i in range(n):
            if check[i] == False:
                check[i] = True
                l.append(lst[i])
                recur(num+1)
                check[i] = False
                l.pop()

recur(0)