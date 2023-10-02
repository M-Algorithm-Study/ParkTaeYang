# Ch = input()
# BB = int(input())
# l = [i for i in range(0,10)]
# if BB!=0:
#     l2 = list(map(int,input().split()))
#     for i in l2:
#         l.remove(i)
# Max = ""
# Max_check = 0
# Min = ""
# Min_check = 0
# if BB == 10:
#     print(abs(int(Ch)-100))
# else:
#     for i in range(len(Ch)):
#         n = int(Ch[i])
#         if Max_check == 0:
#             if n in l:
#                 Max = Max + str(n)
#             else:
#                 j = n
#                 while j not in l:
#                     j += 1
#                     if j>10:
#                         Max_check = 2
#                         break
#                 if Max_check == 0:
#                     Max = Max + str(j)
#                     Max_check = 1 
#         elif Max_check == 1:
#             Max = Max + str(min(l))


#         if Min_check == 0:
#             if n in l:
#                 Min = Min + str(n)
#             else:
#                 k = n
#                 while k not in l:
#                     k -= 1
#                     if k<0:
#                         Min_check = 2
#                         break
#                 if Min_check == 0:
#                     Min = Min + str(k)
#                     Min_check = 1        
#         elif Min_check == 1:
#             Min = Min + str(max(l))

#     answer = [abs(int(Ch)-100)]
#     if Max_check != 2:
#         answer.append(int(Max)-int(Ch)+len(Ch))
#     if Min_check != 2:
#         answer.append(int(Ch)-int(Min)+len(Ch))
#     print(answer)
#     print(min(answer))




Ch = int(input())
BB = int(input())
answer = [abs(int(Ch)-100)]
l = [i for i in range(0,10)]
if BB!=0:
    l2 = list(map(int,input().split()))
    for i in l2:
        l.remove(i)
Ch_up = Ch
Ch_down = Ch

if BB !=10:
    while len(answer) == 1:
        for i in str(Ch_up):
            if int(i) not in l:
                Ch_up+=1
                break
        else:
            answer.append(Ch_up-Ch+len(str(Ch_up)))
            
    
        if Ch_down>=0:
            for i in str(Ch_down):
                if int(i) not in l:
                    Ch_down-=1
                    break
            else:
                answer.append(Ch-Ch_down+len(str(Ch_down)))
print(min(answer))