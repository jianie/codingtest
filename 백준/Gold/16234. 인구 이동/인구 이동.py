'''
인구이동

NxN 크기 땅,
모든 나라는 1x1

하루동안의 인구 이동
국경선 공유하는 두 나라 인구차이 L 이상, R 이하면: 국경선 연다

위 조건 국경선 모두 열고 인구이동 시작

인구수는
연합의 인구수 다 더해서 / 연합 이루는 칸 개수

연합 해체하고 국경선 닫는다


인구이동 며칠동안 발생하는지?


'''


'''
bfs로 그룹 만들고, 그룹당 인구수 갱신해야할 듯 
'''

from collections import deque

N, L, R=map(int, input().split())
board=[list(map(int, input().split())) for i in range(N)]

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,visited):
    global L, R

    group=[]
    group.append((x,y))

    queue=deque()
    queue.append((x,y))
    visited[x][y] = True

    total = board[x][y]



    while queue:
        current=queue.popleft()


        for idx in range(4): #상하좌우 탐색
            nx = current[0] + dx[idx]
            ny = current[1] + dy[idx]

            if 0<=nx<N and 0<=ny<N and (nx,ny) and not visited[nx][ny]: #범위 안에 있고 탐색 안한 곳이라면
                if L<= abs(board[current[0]][current[1]]-board[nx][ny])<=R: # 인구수 차이 조건 만족하면
                    queue.append((nx,ny))
                    visited[nx][ny] = True # 큐에 넣을 때 방문처리하는게 나음

                    group.append((nx,ny))

                    total +=board[nx][ny]

    new_population = total // len(group)
    for gx, gy in group:
        board[gx][gy] = new_population

    return len(group) > 1  # 연합 크기가 1보다 크면 인구 이동 발생




days=0

while True:

    visited = [[False]*N for _ in range(N)]
    ##groups=[] 그룹으로 관리하면 시간초과..

    moved = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    moved = True

    if not moved:
        print(days)
        break

    days += 1



'''

    for group in groups:
        group_num=len(group)    #해당 그룹의 나라 수

        total=0

        for country in group:
            x,y=country
            total+=board[x][y]

        new_people=total//group_num

        for country in group:
            x,y=country
            board[x][y]=new_people
            
    '''





