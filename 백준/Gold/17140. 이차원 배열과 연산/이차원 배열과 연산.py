'''
이차원 배열과 연산

3x3의 배열 A

ㅂ

R연산: 행의 개수가 많을 때. 행을 정렬
C연산: 열의 개수가 많을 때. 열을 정렬


정렬
각 숫자가 몇번 나왔는지,

등장 회수가 커지는 순으로, 그게 여러개면 수가 커지는 순으로 정렬
결과를 배열에 넣을 때: 수, 등장횟수 넣음


가장 큰 행 기준으로 0 채우는 식이고,
정렬할 때 0은 무시해야 함




'''


r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

def operation_R(board):
    new_board = []
    max_len = 0
    for row in board:
        count_dict = {}
        for num in row:
            if num == 0:
                continue
            count_dict[num] = count_dict.get(num, 0) + 1
        # 등장 횟수 오름차순, 숫자 오름차순 정렬
        sorted_items = sorted(count_dict.items(), key=lambda x: (x[1], x[0]))
        new_row = []
        for num, cnt in sorted_items:
            new_row.extend([num, cnt])
        max_len = max(max_len, len(new_row))
        new_board.append(new_row)
    max_len = min(max_len, 100)  # 최대 길이 100 제한
    for row in new_board:
        row += [0] * (max_len - len(row))
    return new_board

def operation_C(board):
    transposed = list(zip(*board))
    transposed = [list(row) for row in transposed]
    operated = operation_R(transposed)
    result = list(zip(*operated))
    result = [list(row) for row in result]
    return result

second = 0

# 0초 시점에서 먼저 검사
if 0 <= r-1 < len(board) and 0 <= c-1 < len(board[0]) and board[r-1][c-1] == k:
    print(0)
    exit()

# 최대 100초까지 반복
while second < 100:
    if len(board) >= len(board[0]):
        board = operation_R(board)
    else:
        board = operation_C(board)
    second += 1
    if 0 <= r-1 < len(board) and 0 <= c-1 < len(board[0]) and board[r-1][c-1] == k:
        print(second)
        break
else:
    print(-1)


