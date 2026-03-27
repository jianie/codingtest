from collections import deque


F,S,G,U,D=map(int,input().split())







# U버튼은 위로 U층, D버튼은 아래로 D층 해당층 없으면 엘베 안움직임

# S층에서 G층으로 가야함

# S, G F 혹은 G,S, F


queue=deque()

queue.append(S)


visited=[-1]*(F+1)

visited[S]=0

while queue:
    floor=queue.popleft()

    up_floor=floor+U
    down_floor=floor-D

    if up_floor<=F and visited[up_floor]==-1:
        queue.append(up_floor)
        visited[up_floor]= visited[floor]+1

    if down_floor >=1  and visited[down_floor] == -1:
        queue.append(down_floor)
        visited[down_floor] = visited[floor]+1

if visited[G]==-1:
    print('use the stairs')
else:
    print(visited[G])
