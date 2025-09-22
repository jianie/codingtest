from collections import deque

N, M, T = map(int, input().split())

circle = [deque() for _ in range(N)]
for i in range(N):
    numbers = list(map(int, input().split()))
    for num in numbers:
        circle[i].append(num)

xdk_list = [tuple(map(int, input().split())) for _ in range(T)]

for i in range(T):
    x, d, k = xdk_list[i]

    # 원판 회전
    for n in range(1, N + 1):
        if n % x == 0:
            num = n - 1
            for _ in range(k):
                if d == 0:  # 시계방향
                    circle[num].appendleft(circle[num].pop())
                else:  # 반시계 방향
                    circle[num].append(circle[num].popleft())

    # 0이 아닌 수가 있는지 확인
    if any(any(val != 0 for val in row) for row in circle):
        remove_list = set()

        # 인접하면서 수가 같은 것을 모두 찾는다
        for i in range(N):
            for j in range(M):
                number = circle[i][j]
                if number == 0:
                    continue

                # 같은 원판 내 좌우 인접
                if circle[i][(j - 1) % M] == number:
                    remove_list.add((i, j))
                    remove_list.add((i, (j - 1) % M))
                if circle[i][(j + 1) % M] == number:
                    remove_list.add((i, j))
                    remove_list.add((i, (j + 1) % M))

                # 인접 원판 위 아래 확인
                if i - 1 >= 0:
                    if circle[i - 1][j] == number:
                        remove_list.add((i, j))
                        remove_list.add((i - 1, j))
                if i + 1 < N:
                    if circle[i + 1][j] == number:
                        remove_list.add((i, j))
                        remove_list.add((i + 1, j))

        if remove_list:
            for r, c in remove_list:
                circle[r][c] = 0
        else:
            total = 0
            cnt = 0
            for i in range(N):
                for val in circle[i]:
                    if val != 0:
                        total += val
                        cnt += 1

            if cnt == 0:
                break

            average = total / cnt

            for i in range(N):
                for j in range(M):
                    if circle[i][j] == 0:
                        continue
                    if circle[i][j] > average:
                        circle[i][j] -= 1
                    elif circle[i][j] < average:
                        circle[i][j] += 1

answer = 0
for i in range(N):
    answer += sum(circle[i])

print(answer)
