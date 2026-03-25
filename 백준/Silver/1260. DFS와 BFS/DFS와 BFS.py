'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

'''

from collections import deque

N,M,V=map(int,input().split()) #정점 개수, 간선 개수, 탐색 시작 번호

#edges = [list(map(int, input().split())) for _ in range(M)]

edges=[[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    v1,v2=map(int,input().split())
    edges[v1][v2], edges[v2][v1]=1,1


visited=[0]*(N+1)

dfs_answer=[]
bfs_answer=[]


def dfs(vertex):
    if visited[vertex]==1:
        return

    visited[vertex]=1
    dfs_answer.append(vertex)

    for v in range(1,N+1):
        if v!=vertex and edges[vertex][v]==1:
            dfs(v)


dfs(V)

for i in range(len(dfs_answer)):
    print(dfs_answer[i],end=' ')


bfs_visited=[0]*(N+1)
def bfs():
    queue=deque()
    queue.append(V)
    bfs_visited[V] = 1  # 큐에 넣는 순간 방문처리 해야함

    while queue:

        vertex=queue.popleft()

        bfs_visited[vertex]=1

        bfs_answer.append(vertex)

        for v in range(1,N+1):
            if edges[vertex][v]==1 and bfs_visited[v]==0:
                bfs_visited[v] = 1
                queue.append(v)

bfs()

print()
for i in range(len(bfs_answer)):
    print(bfs_answer[i],end=' ')
