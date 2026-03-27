# 직접연결- 1촌,
# 두 사람의 촌수 계산하는 프로그램

from collections import deque


N=int(input()) # 전체 사람 수= 정점 수

n1, n2=map(int,input().split())

m=int(input()) # 부모 자식들 간의 관계의 개수 = 에지 수


graph=[[] for _ in range(N+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


queue=deque()
visited=[-1]*(N+1)

queue.append(n1)
visited[n1]=0

while queue:
    person=queue.popleft()

    if person==n2:
        print(visited[person])
        break

    for family in graph[person]:
        if visited[family]==-1:
            queue.append(family)
            visited[family]=visited[person]+1

else:
    print(-1)
