
### BFS에서 최단거리는 큐에서 꺼낸 횟수가 아니라 그 좌표까지 도달할 때의 거리값으로 관리해야 해.

# 1은 이동 가능, 0은 이동 불가
#N,M까지 가야 함
# 지나가야 하는 최소 칸 수
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue.append((0, 0))
visited[0][0] = 1

while queue:
    nx, ny = queue.popleft()

    for i in range(4):
        x = nx + dx[i]
        y = ny + dy[i]

        if 0 <= x < N and 0 <= y < M:
            if visited[x][y] == 0 and board[x][y] == 1:
                visited[x][y] = visited[nx][ny] + 1 ###############
                queue.append((x, y))

print(visited[N-1][M-1])