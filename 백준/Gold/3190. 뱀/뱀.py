'''
사과 먹으면 뱀 길이 늘어님

벽 또는 자기 몸과 부딪히면 게임 끝

NxN 보드 위에서 진행

뱀 처음엔 왼쪽 위에 있고, 길이는 1, 오른쪽을 향한다
매초 이동함

게임이 몇 초에 끝나는지를 출력
'''

from collections import deque

N=int(input()) # 보드 크기
K=int(input()) # 사과 개수

#보드
board=[[0]*N for _ in range(N)]
board[0][0]=1 # 초기 뱀의 위치



#상, 우, 하, 좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#사과 위치 저장
apple=set()
for i in range(K):
    r, c = map(int, input().split())
    apple.add((r - 1, c - 1))

L=int(input()) # 뱀의 방향 변환 횟수
direction=dict()
for i in range(L):
    X, C = input().split()
    X = int(X)
    direction[X]=C




current_direction=1 # 초기 방향은 오른쪽
head_x=0
head_y=0

tail_x=0
tail_y=0

# 큐 왼쪽이 꼬리, 오른쪽이 머리
snake=deque()

snake.append((head_x,head_y))

second = 0
while True:
    new_head_x = head_x + dx[current_direction]
    new_head_y = head_y + dy[current_direction]

    if not (0 <= new_head_x < N and 0 <= new_head_y < N and (new_head_x, new_head_y) not in snake):
        break

    snake.append((new_head_x, new_head_y))
    head_x, head_y = new_head_x, new_head_y

    if (new_head_x, new_head_y) in apple:
        apple.discard((new_head_x, new_head_y))
    else:
        snake.popleft()

    second += 1

    if second in direction:
        if direction[second] == 'L':
            current_direction = (current_direction - 1) % 4
        else:
            current_direction = (current_direction + 1) % 4

print(second + 1)
