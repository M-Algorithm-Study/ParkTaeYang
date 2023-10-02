dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph = []
n,m = map(int,input().split())
for _ in range(n):
    graph.append(list(input()))
visited = [[0 for _ in range(m)] for _ in range(n)]
check = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            queue = [(i,j)]
            visited[i][j] = 1
            check = 1
            break
    if check == 1:
        break

answer = 0 
while queue:
    y,x = queue.pop()
    if graph[y][x] == 'P':
        answer +=1
    for i in range(4):
        mx = x+dx[i]
        my = y+dy[i]
        if 0<=mx<m and 0<=my<n:
            if graph[my][mx] !='X' and visited[my][mx] == 0:
                queue.append((my,mx))
                visited[my][mx] = 1

if answer == 0 :
    print("TT")
else:
    print(answer)

