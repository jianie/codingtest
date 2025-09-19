import copy

R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
W = int(input())

wall = set()
for _ in range(W):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    # t == 0 -> 위쪽 벽, t == 1 -> 오른쪽 벽
    if t == 0:
        wall.add((x, y, x-1, y))
        wall.add((x-1, y, x, y))
    else:
        wall.add((x, y, x, y+1))
        wall.add((x, y+1, x, y))

room = [[0]*C for _ in range(R)]

# 방향: 오른쪽(0), 왼쪽(1), 위(2), 아래(3)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def can_move(x1, y1, x2, y2):
    # 범위 체크와 벽 체크
    if not (0 <= x2 < R and 0 <= y2 < C):
        return False
    if (x1, y1, x2, y2) in wall:
        return False
    return True

def blow(direction, x, y, power, visited):
    if power == 0:
        return
    if not (0 <= x < R and 0 <= y < C):
        return
    if visited[x][y]:
        return

    visited[x][y] = True
    room[x][y] += power

    # 바람 진행 방향 벡터
    d = direction
    nx, ny = x + dx[d], y + dy[d]

    if not (0 <= nx < R and 0 <= ny < C):
        return

    # 직진 방향 벽 체크 후 진행
    if can_move(x, y, nx, ny):
        blow(direction, nx, ny, power-1, visited)

    # 대각선 방향 전파 처리 (벽 2개 체크 필요)
    if direction == 0 or direction == 1:  # 오른쪽 또는 왼쪽 바람
        # 아래 대각선
        diag_x, diag_y = nx + 1, ny
        if (0 <= diag_x < R and 0 <= diag_y < C and not visited[diag_x][diag_y]):
            # 바람이 들어가는 두 칸 모두 벽이 없어야 함
            if can_move(x, y, x+1, y) and can_move(x+1, y, x+1, ny):
                blow(direction, diag_x, diag_y, power-1, visited)

        # 위 대각선
        diag_x, diag_y = nx - 1, ny
        if (0 <= diag_x < R and 0 <= diag_y < C and not visited[diag_x][diag_y]):
            if can_move(x, y, x-1, y) and can_move(x-1, y, x-1, ny):
                blow(direction, diag_x, diag_y, power-1, visited)

    else:  # 위쪽 또는 아래쪽 바람
        # 오른쪽 대각선
        diag_x, diag_y = nx, ny + 1
        if (0 <= diag_x < R and 0 <= diag_y < C and not visited[diag_x][diag_y]):
            if can_move(x, y, x, y + 1) and can_move(x, y + 1, nx, ny + 1):
                blow(direction, diag_x, diag_y, power-1, visited)
        # 왼쪽 대각선
        diag_x, diag_y = nx, ny - 1
        if (0 <= diag_x < R and 0 <= diag_y < C and not visited[diag_x][diag_y]):
            if can_move(x, y, x, y - 1) and can_move(x, y - 1, nx, ny - 1):
                blow(direction, diag_x, diag_y, power - 1, visited)

def wind():
    for x in range(R):
        for y in range(C):
            if 1 <= board[x][y] <= 4:
                direction = board[x][y] - 1
                start_x = x + dx[direction]
                start_y = y + dy[direction]
                visited = [[False]*C for _ in range(R)]
                blow(direction, start_x, start_y, 5, visited)

def temperature():
    global room
    new_room = copy.deepcopy(room)
    # 인접 칸 쌍을 중복 없이 처리하기 위한 방문 체크
    for x in range(R):
        for y in range(C):
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if (x, y, nx, ny) in wall or (nx, ny, x, y) in wall:
                        continue
                    # 중복 계산 방지를 위해 (x,y) < (nx, ny) 조건으로 정렬
                    if (x, y) < (nx, ny):
                        diff = abs(room[x][y] - room[nx][ny]) // 4
                        if diff > 0:
                            if room[x][y] > room[nx][ny]:
                                new_room[x][y] -= diff
                                new_room[nx][ny] += diff
                            else:
                                new_room[x][y] += diff
                                new_room[nx][ny] -= diff
    room = new_room

def side_temperature():
    for i in range(C):
        if room[0][i] > 0:
            room[0][i] -= 1
        if room[R-1][i] > 0:
            room[R-1][i] -= 1
    for i in range(1, R-1):
        if room[i][0] > 0:
            room[i][0] -= 1
        if room[i][C-1] > 0:
            room[i][C-1] -= 1

chocolate = 0
while True:
    wind()
    temperature()
    side_temperature()
    chocolate += 1

    finish = True
    for r in range(R):
        for c in range(C):
            if board[r][c] == 5 and room[r][c] < K:
                finish = False
                break
        if not finish:
            break
    if finish or chocolate > 100:
        print(min(chocolate, 101))
        break
