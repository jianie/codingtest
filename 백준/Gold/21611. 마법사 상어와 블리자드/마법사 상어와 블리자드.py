from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magic = [list(map(int, input().split())) for _ in range(M)]

shark_x = (N - 1) // 2
shark_y = (N - 1) // 2


def make_spiral_coords(N):
    x, y = shark_x, shark_y
    coords = []
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 좌, 하, 우, 상
    length = 1

    while len(coords) < N * N - 1:
        for i, (dx_, dy_) in enumerate(directions):
            for _ in range(length):
                x += dx_
                y += dy_
                if 0 <= x < N and 0 <= y < N:
                    coords.append((x, y))
                if len(coords) == N * N - 1:
                    return coords
            if i % 2 == 1:  # 하 또는 상 방향 후 길이 증가
                length += 1


spiral_coords = make_spiral_coords(N)
pos_to_idx = {pos: i for i, pos in enumerate(spiral_coords)}

queue = deque(board[x][y] for x, y in spiral_coords)
answer = 0


def destroy(queue, d, s):
    dir_map = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
    dx_, dy_ = dir_map[d]
    destroyed_indices = []
    x, y = shark_x, shark_y

    for dist in range(1, s + 1):
        nx, ny = x + dx_ * dist, y + dy_ * dist
        if (nx, ny) in pos_to_idx:
            destroyed_indices.append(pos_to_idx[(nx, ny)])

    new_queue = deque(0 if i in destroyed_indices else val for i, val in enumerate(queue))
    return new_queue


def move(queue):
    return deque(x for x in queue if x != 0)


def bump(queue):
    global answer
    while True:
        new_queue = deque()
        i = 0
        length = len(queue)
        exploded = False

        while i < length:
            j = i + 1
            while j < length and queue[j] == queue[i]:
                j += 1
            count = j - i

            if count >= 4 and queue[i] != 0:
                answer += queue[i] * count
                exploded = True
                # 폭발 구간은 추가하지 않음 (제거)
            else:
                for k in range(i, j):
                    new_queue.append(queue[k])

            i = j

        queue = move(new_queue)

        if not exploded:
            return queue


def adjust(queue):
    new_queue = deque()
    length = len(queue)
    i = 0
    max_len = N * N - 1

    while i < length:
        j = i + 1
        while j < length and queue[j] == queue[i]:
            j += 1
        count = j - i
        new_queue.append(count)
        new_queue.append(queue[i])
        i = j

        if len(new_queue) >= max_len:
            break

    # 길이 초과 시 자르기
    while len(new_queue) > max_len:
        new_queue.pop()

    return new_queue


def update_board(queue):
    for i, (x, y) in enumerate(spiral_coords):
        if i < len(queue):
            board[x][y] = queue[i]
        else:
            board[x][y] = 0


for d, s in magic:
    queue = destroy(queue, d, s)
    queue = move(queue)
    queue = bump(queue)
    queue = adjust(queue)
    update_board(queue)

print(answer)
