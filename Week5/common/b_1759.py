a,b = map(int,input().split())
l = list(input().split())
l = sorted(l)
k = []
m = ['a','e','i','o','u']
check = [True]*(b+1)
def pwd(num):
    if num == a:
        c1 = 0
        c2 = 0
        for q in k:
            if q in m:
                c1+=1
            else:
                c2+=1    
        if c1>=1 and c2>=2:
            return print(*k,sep='')
        else:
            return 0  

    else:
        for i in range(b):
            if check[i] == True:
                for j in range(i+1):
                    check[j] = False
                k.append(l[i])
                pwd(num+1)
                for j in range(i+1):
                    check[j] = True
                k.pop()

pwd(0)