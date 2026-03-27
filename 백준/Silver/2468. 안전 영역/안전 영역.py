from collections import deque
N=int(input())

board=[ list(map(int,input().split())) for _ in range(N)]







dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,rain):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=1

    while queue:
        x_pos,y_pos=queue.popleft()

        for i in range(4):
            nx=x_pos+dx[i]
            ny=y_pos+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny]>rain and visited[nx][ny]==0:
                    queue.append((nx,ny))
                    visited[nx][ny]=1


answer=0


for rain in range(0,max(map(max,board))):
    visited = [[0] * N for _ in range(N)]
    area = 0

    for i in range(N):
        for j in range(N):
            if board[i][j]>rain and visited[i][j]==0:
                bfs(i,j,rain)
                area+=1
    answer=max(answer,area)

print(answer)




