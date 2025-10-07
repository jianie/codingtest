from collections import deque

def check(place, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False]*5 for _ in range(5)]

    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True

    while queue:
        cx, cy, dist = queue.popleft()
        if dist > 0 and place[cx][cy] == 'P':
            return False
        if dist < 2:
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    if place[nx][ny] != 'X':  # 파티션 막기
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))
    return True

def solution(places):
    answer = []
    for place in places:
        is_safe = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not check(place, i, j):
                        is_safe = False
                        break
            if not is_safe:
                break
        answer.append(1 if is_safe else 0)
    return answer
