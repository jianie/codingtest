"""
연구소

연구소 크기 NxM


빈칸 or 벽 으로 이루어짐

바이러스는 상하좌우로 퍼져나가

새로 세울수 있는 벽은 3개

0:빈칸
1: 벽
2: 바이러스


안전 영역 최대 구하기

==> back Tracking,  모든 경우의수를 탐색해야 함

"""

from collections import deque
import copy  # copy 는 어떨 때 쓰는거지

N,M=map(int,input().split())


virus_map=[list(map(int,input().split())) for _ in range(N)]
result=0


dx=[-1,1,0,0]
dy=[0,0,-1,1]



# 백트래킹으로 3개의 벽을 설치한 모든 조합을 만듬
def createWall(wall_cnt):
    if wall_cnt==3:
        bfs()
        return

    for  x in range(N):
        for y in range(M):
            if virus_map[x][y]==0:
                virus_map[x][y]=1
                createWall(wall_cnt+1)
                virus_map[x][y]=0


def bfs():
    global result
    wall_Arr=copy.deepcopy(virus_map)
    q=deque()

    for x in range(N):  # 바이러스 정보 큐에 저장
        for y in range(M):
            if wall_Arr[x][y]==2:
                q.append((x,y))

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0 <= nx < N and 0 <= ny < M and wall_Arr[nx][ny] == 0:
                wall_Arr[nx][ny] = 2
                q.append((nx, ny))

    # 안전지대 개수 카운팅
    safezone = 0
    for line in wall_Arr:
        safezone += line.count(0)
    result = max(safezone, result)








createWall(0)
print(result)




