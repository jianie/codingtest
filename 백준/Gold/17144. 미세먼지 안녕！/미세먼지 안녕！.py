'''

RxC 집


공기청정기: 항상 1열애, 두칸 차지


1초동안 일어나는 일

1.미세먼지 확산- 모든 칸에서 동시에
각 칸의 미세먼지가 인접 네 방향으로 확산 ( 공기청정기 있거나, 칸 없으면 확산 x)
확산되는 양: ⌊Ar,c/5⌋
(r, c)에 남은 미세먼지의 양:  Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수)

2. 공기청정기 작동

바람이 나온다
위쪽: 반시계 방향 순환
아래쪽: 시계 방향 순환

바람 불면 미세먼지가 바람 방향대로 한칸씩 이동
=> 공기청정ㄹ기로 들어가면 미세먼지가 모두 정하된다



T 초가 지난 후 남아있는 미세먼지 양 출력
'''

import copy

R, C, T=map(int, input().split())

board=[list(map(int, input().split())) for i in range(R)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

position=[]
# 공기청정기 위치 찾기
for i in range(R):
    if board[i][0]==-1:
        position.append(i)


def dust():
    global board
    new_board=copy.deepcopy(board)

    for i in range(R):
        for j in range(C):

            if board[i][j] <= 0:  # -1(청정기)이거나 미세먼지 0 이하일 때 확산 안 함
                continue

            measure=board[i][j]//5

            count = 0
            for dir in range(4):
                nx=i+dx[dir]
                ny=j+dy[dir]

                if 0<=nx<R and 0<=ny<C and board[nx][ny]!=-1:
                    count+=1
                    new_board[nx][ny]+=measure

            new_board[i][j]=new_board[i][j]-measure*count

    board=new_board




def wind():
    global board
    new_board = copy.deepcopy(board)

    #공기청정기 위치 (r값)
    up_r=position[0]    #(up_r,0)
    down_r=position[1]  #(down_r,))

    # 윗쪽 공기청정기

    new_board[up_r][1]=0
    for c in range(2,C,1):
        new_board[up_r][c]=board[up_r][c-1]

    for r in range(up_r-1,-1,-1):
        new_board[r][C-1]=board[r+1][C-1]

    for c in range(C-2,-1,-1):
        new_board[0][c]=board[0][c+1]

    for r in range(1, up_r, 1):
        new_board[r][0]=board[r-1][0]

    # 아래 공기청정기

    new_board[down_r][1] = 0
    for c in range(2,C,1):
        new_board[down_r][c]=board[down_r][c-1]

    for r in range(down_r+1,R,1):
        new_board[r][C-1]=board[r-1][C-1]

    for c in range(C-2,-1,-1):
        new_board[R-1][c]=board[R-1][c+1]

    for r in range(R-2, down_r, -1):
        new_board[r][0]=board[r+1][0]

    board=new_board





for second in range(T):
    dust()
    wind()


# T초 후 남아있는 미세먼지 양 구하기
answer=0
for i in range(R):
    for j in range(C):
        if board[i][j]==-1:
            continue
        answer+=board[i][j]


print(answer)


