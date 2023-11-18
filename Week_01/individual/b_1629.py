a,b,c = map(int,input().split())

def dac(a,b,c):
    if b == 1:
        return a%c

    tmp = dac(a,b//2,c)
    if b%2 == 0:
        return tmp*tmp%c
    else:
        return tmp*tmp*a%c

print(dac(a,b,c))