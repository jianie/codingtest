from collections import deque

M, N, H = map(int, input().split())

box = []
queue = deque()

for h in range(H):
    layer = []
    for x in range(N):
        row = list(map(int, input().split()))
        layer.append(row)

        for y in range(M):
            if row[y] == 1:
                queue.append((h, x, y))
    box.append(layer)

# 6방향: 상하좌우앞뒤
dh = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

while queue:
    h, x, y = queue.popleft()

    for i in range(6):
        nh = h + dh[i]
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M:
            if box[nh][nx][ny] == 0:
                box[nh][nx][ny] = box[h][x][y] + 1
                queue.append((nh, nx, ny))

answer = 0

for h in range(H):
    for x in range(N):
        for y in range(M):
            if box[h][x][y] == 0:
                print(-1)
                exit()
            answer = max(answer, box[h][x][y])

print(answer - 1)