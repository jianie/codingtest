
from collections import deque

vertex=int(input())
edge=int(input()) # 에지 수

graph=[[]*(vertex+1) for _ in range(vertex+1)]

for i in range(edge):
    a,b=map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)


visited=[0]*(vertex+1)

queue=deque()
queue.append(1)
visited[1]=1

answer=-1

while queue:
    computer=queue.popleft()
    answer+=1

    for v in graph[computer]:
        if visited[v]==0:
            queue.append(v)
            visited[v]=1

print(answer)


