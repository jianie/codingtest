'''
격자 NxN

블록은 검은색 -1 , 무지개 0 , 일반 M가지 색

블록 그룹 : 2개 이상의 블록, 일반 블록 적어도 하나, 일반 블록 색 다 같아야함 , 검은블록 없어야함

기준 블록 : 일반 블록 중의 행, 열 가장 작은 블록


중력: 검은색 블록 제외하고 이동

오토플레이: 블록 그룹이 존재하는 한 계속 반복, 오토플레이 끝났을 떄 획득 점수를 출력



'''

from collections import deque







dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 가장 큰 블록 찾기
def find_big_block(i, j, block_number):
  q = deque()
  q.append((i, j)) # 시작점

  normal = [[i, j]] # 일반 블럭
  rainbow = [] # 무지개 블럭

  while q:
    x, y = q.popleft()
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < N and 0 <= ny < N:
        # 범위 내 무지개 블록이면서 방문 안한 경우
        if block[nx][ny] == 0 and not visited[nx][ny]:
          visited[nx][ny] = 1
          q.append((nx, ny))
          rainbow.append([nx, ny]) # 무지개 리스트에 추가

        # 같은 색상의 일반 블록이면서 방문 안한 경우
        elif block[nx][ny] == block_number and not visited[nx][ny]:
          visited[nx][ny] = 1
          q.append((nx, ny))
          normal.append([nx, ny]) # 일반 리스트에 추가

  for x, y in rainbow: # 무지개 블록 방문 초기화
    visited[x][y] = 0

  # 블록 크기, 무지개블록 수, 블록 리스트
  return [len(normal+rainbow), len(rainbow), normal+rainbow]

# 블록 제거해주기
def remove(group):
  global score
  for x, y in group[2]:
    block[x][y] = -2 # 제거된 블록 = -2로 표시
  score += group[0] ** 2

# 중력 작용시키기
def gravity():
  for i in range(N-2, -1, -1): # 아래에서 위로
    for j in range(N):
      if block[i][j] != -1: # 검은색 블록이 아닐 때
        g = i
        while g+1 < N and block[g+1][j] == -2: # 빈 칸인 경우
          block[g+1][j] = block[g][j] # 아래로 이동
          block[g][j] = -2 # 원래 자리는 빈 칸으로 표시
          g += 1 # 한 칸 아래로 이동

# 90도 반시계 방향으로 회전
def rotate():
  global block
  new_block = [[0] * N for _ in range(N)] # 90도 돌렸을 때 블록판
  for i in range(N):
    for j in range(N):
      new_block[N-j-1][i] = block[i][j] # 90도 회전

  block = new_block # 새 블록판으로 업뎃

N,M=map(int,input().split())
#block = []
block=[list(map(int,input().split())) for _ in range(N)]
#for _ in range(N):
#  info = list(map(int, input().strip().split()))
#  block.append(info)

score = 0
while True:
  visited = [[0] * N for _ in range(N)]
  group = [] # 그룹 리스트
  for i in range(N):
    for j in range(N):
      if block[i][j] >= 1 and not visited[i][j]:
        visited[i][j] = 1
        find_group = find_big_block(i, j, block[i][j]) # 블록 그룹 찾기
        if find_group[0] >= 2: # 2 이상일 때
          group.append(find_group) # 그룹 리스트에 추ㄱ

  group.sort(reverse=True) # 그룹 크기, 무지개 블록 수, 기준 블록 순으로 정렬

  if not group: # 그룹 없으면 종료
    break

  remove(group[0])
  gravity()
  rotate()
  gravity()

print(score)