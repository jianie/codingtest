# 1. 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다.
# 2. 가장 왼쪽에 있는 어항을 그 어항의 오른쪽에 있는 어항의 위에 올리기
# 3. 행이 2 이상이면, 시계방향으로 90도 회전 후 어항 위에 올리기
# 4. 바닥에 있는 어항의 범위보다 초과되면 안됌
# 5. 물고기의 수를 조절 : 동시에 발생
# 6. 어항을 다시 일렬로 놓기
# 7. 반으로 나눠 왼쪽 부분을 180도 회전 -> 2번 반복
# 8. 다시 물고기의 수를 조절
# 9. 바닥에 일렬로 놓기

from collections import deque

n, k = map(int, input().split())
# 상 하 좌 우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = [deque(list(map(int, input().split())))]

result = 0

def get_diff(board) :
    get_q = board[0]
    return max(get_q) - min(get_q)

def rotate_stack(arr) :
    while True :
        if len(arr) > len(arr[0]) - len(arr[-1]) :
            break
        blocks = []
        r = len(arr)
        c = len(arr[-1])

        for i in range(r) :
            temp_q = deque()
            for _ in range(c) :
                temp_q.append(arr[i].popleft())
            blocks.append(temp_q)

        arr = [arr[0]]
        rotated = rotate_90(blocks)
        for row in rotated :
            arr.append(deque(row))

    return arr


def rotate_90(block) :
    temp = [[0] * len(block) for _ in range(len(block[0]))]
    for i in range(len(block[0])) :
        for j in range(len(block)) :
            temp[i][j] = block[j][len(block[0])-1-i]
    return temp

def fix_fish(arr) :
    dp = [[0] * len(arr[x]) for x in range(len(arr))]
    for x in range(len(arr)) :
        for y in range(len(arr[x])) :
            for dir in directions :
                nx = x + dir[0]
                ny = y + dir[1]

                if 0 <= nx < len(arr) and 0 <= ny < len(arr[nx]) :
                    # 현재 칸이 인접한 칸보다 크면
                    if arr[x][y] > arr[nx][ny] :
                        diff = (arr[x][y] - arr[nx][ny]) // 5
                        if diff >= 1 :
                            dp[x][y] -= diff
                    else : # 현재 칸이 인접한 칸보다 작으면
                        diff = (arr[nx][ny] - arr[x][y]) // 5
                        if diff >= 1 :
                            dp[x][y] += diff
    for i in range(len(arr)) :
        for j in range(len(arr[i])) :
            arr[i][j] += dp[i][j]

def make_one_line(arr) :
    temp = deque()
    for i in range(len(arr[-1])) :
        for j in range(len(arr)) :
            temp.append(arr[j][i])

    for i in range(len(arr[-1]), len(arr[0])) :
        temp.append(arr[0][i])

    return [temp]

def half_rotation(arr) :
    temp = deque()
    for i in range(n // 2) :
        temp.append(arr[0].popleft())
    rotated = rotate_180([temp])
    arr += rotated

    left = []
    for i in range(2) :
        data = deque()
        for j in range(n // 4) :
            data.append(arr[i].popleft())
        left.append(data)
    rotated = rotate_180(left)
    arr += rotated

def rotate_180(arr) :
    temp = []
    for i in reversed(range(len(arr))) :
        arr[i].reverse()
        temp.append(arr[i])

    return temp


while True :
    # 물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이 구하기
    diff = get_diff(board)
    if diff <= k :
        print(result)
        break

    # 1번 수행
    min_value = min(board[0])
    for i in range(len(board[0])) :
        if board[0][i] == min_value :
            board[0][i] += 1

    # 2번 수행
    value = board[0].popleft()
    board.append(deque([value]))
    # 3번 수행
    board = rotate_stack(board)
    # 5번 수행
    fix_fish(board)
    # 6번 수행
    board = make_one_line(board)
    # 7번 수행
    half_rotation(board)
    # 8번 수행
    fix_fish(board)
    # 9번 수행
    board = make_one_line(board)

    result += 1