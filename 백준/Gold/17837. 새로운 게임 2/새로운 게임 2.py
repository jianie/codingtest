from collections import deque

N, K = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(N)]

board = [[deque() for _ in range(N)] for _ in range(N)]
horses = []

for i in range(K):
    r, c, d = map(int, input().split())
    horses.append([r-1, c-1, d-1])
    board[r-1][c-1].append(i)

# 방향: 오른쪽(0), 왼쪽(1), 위(2), 아래(3)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def reverse_dir(d):
    return d+1 if d % 2 == 0 else d-1

def game_end_check():
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 4:
                return True
    return False

turn = 0
while turn <= 1000:
    turn += 1

    for i in range(K):
        r, c, d = horses[i]
        idx_in_stack = board[r][c].index(i)
        moving_horses = deque()
        while len(board[r][c]) > idx_in_stack:
            moving_horses.append(board[r][c].pop())

        nr = r + dx[d]
        nc = c + dy[d]

        # 파란색이거나 범위 벗어나면 방향 반대로
        if not (0 <= nr < N and 0 <= nc < N) or chess[nr][nc] == 2:
            d = reverse_dir(d)
            horses[i][2] = d
            nr = r + dx[d]
            nc = c + dy[d]

            # 다시 한번 파란색이거나 밖이면 이동 안함
            if not (0 <= nr < N and 0 <= nc < N) or chess[nr][nc] == 2:
                # 원래 상태 유지
                for mh in reversed(moving_horses):
                    board[r][c].append(mh)
                continue

        # 흰색: 순서 유지, 빨간색: 순서 뒤집기
        if chess[nr][nc] == 0:
            for mh in reversed(moving_horses):
                board[nr][nc].append(mh)
        else:  # 빨간색
            for mh in moving_horses:
                board[nr][nc].append(mh)

        # 말 위치 갱신
        for mh in moving_horses:
            horses[mh][0], horses[mh][1] = nr, nc

        if game_end_check():
            print(turn)
            exit(0)

print(-1)
