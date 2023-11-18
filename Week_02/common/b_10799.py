a = input()
l = []
total = 0
for i in range(len(a)):
    if a[i] =='(':
        l.append(a[i])
    else:
        if a[i-1] == '(':
            l.pop()
            total +=len(l)
        else:
            l.pop()
            total +=1
print(total)