

N,M,K=map(int,input().split())  # n개 격자, M개 파이어볼, K번 이동





#위치 r c  질량m 속력s 방향d
fireballs=[list(map(int,input().split())) for _ in range(M)]



# 0-based 인덱스를 위한 빈 격자 초기화 (빈 리스트 각 칸에 배정)
board = [[[] for _ in range(N)] for _ in range(N)]


# 초기 파이어볼 위치 보드에 저장
for fb in fireballs:
    r, c, m, s, d = fb
    r -= 1  # 0-based 인덱스 변환
    c -= 1
    board[r][c].append([m, s, d])

# 이동 방향(예: 8방향: 0~7)
directions = [
    (-1, 0), (-1, 1), (0, 1), (1, 1),
    (1, 0), (1, -1), (0, -1), (-1, -1)
]



for _ in range(K):
    # 1) 파이어볼 이동
    new_board = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if board[r][c]:
                for fb in board[r][c]:
                    m, s, d = fb
                    dr, dc = directions[d]
                    nr = (r + dr * s) % N  # 격자 경계 넘어가면 반대편으로 이동 (모듈로 연산)
                    nc = (c + dc * s) % N
                    new_board[nr][nc].append([m, s, d])
    board = new_board

    # 2) 같은 칸에 파이어볼 여러 개 있으면 합치고 나눠서 처리 (문제 조건에 맞게 구현)
    for r in range(N):
        for c in range(N):
            if len(board[r][c]) > 1:
                total_m = sum(fb[0] for fb in board[r][c])
                total_s = sum(fb[1] for fb in board[r][c])
                count = len(board[r][c])

                # 질량이 0인 경우 제거
                if total_m // 5 == 0:
                    board[r][c] = []
                    continue

                mass = total_m // 5
                speed = total_s // count

                # 방향이 모두 홀수 또는 모두 짝수인지 체크
                directions_parity = [fb[2] % 2 for fb in board[r][c]]
                if all(p == directions_parity[0] for p in directions_parity):
                    new_dirs = [0, 2, 4, 6]
                else:
                    new_dirs = [1, 3, 5, 7]

                board[r][c] = [[mass, speed, d] for d in new_dirs]








#최종 질량 합 구하기
answer = 0
for r in range(N):
    for c in range(N):
        for fb in board[r][c]:
            answer += fb[0]

print(answer)