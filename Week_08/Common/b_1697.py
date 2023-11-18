from collections import deque
n,k = map(int,input().split())
second = [-1] * 200001

def bfs(x,y):
    queue = deque()
    queue.append(x)
    second[x] = 0
    while queue:
        check = queue.popleft()
        if check == y:
            return second[check]+1
        else:
            if 0<=check+1<=100001 and second[check+1] == -1:
                second[check+1] = second[check]+1
                queue.append(check+1)
            if 0<=2*check<=100001 and second[2*check] == -1:
                second[2*check] = second[check]+1
                queue.append(2*check)
            if 0<=check-1<=100001  and second[check-1] == -1:
                second[check-1] = second[check]+1
                queue.append(check-1)

print(bfs(n,k)-1)

