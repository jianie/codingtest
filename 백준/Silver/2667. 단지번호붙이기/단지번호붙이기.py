from collections import deque
N=int(input())

board=[list(map(int,input())) for _ in range(N)]



dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[[0]*N for _ in range(N)]

answer=[]


def bfs(x,y):
    queue = deque()

    queue.append((x,y))
    visited[x][y]=1

    total_house=1

    while queue:
        x_pos,y_pos=queue.popleft()

        for i in range(4):
            new_x,new_y=x_pos+dx[i],y_pos+dy[i]

            if 0<=new_x<N and 0<=new_y<N:
                if board[new_x][new_y]==1 and visited[new_x][new_y] == 0:
                    queue.append((new_x,new_y))
                    visited[new_x][new_y]=1
                    total_house+=1

    return total_house

for i in range(N):
    for j in range(N):
        if board[i][j]==1 and visited[i][j]!=1:
            danji_house=bfs(i,j)
            answer.append(danji_house)


print(len(answer))
answer.sort()
for n in answer:
    print(n)


