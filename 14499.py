'''

주사위 굴리기

NxM 지도 위에 주사위가 있다

지도 각 칸에는 정수 써있음

주사위 굴렸을 때
지도칸 0이면 -> 주사위 바닥면 수가 칸에 복사
지도칸 0이 아니면 -> 칸 숫자가 주사위 바닥면으로 복사, 칸 숫자는 0으로



지도 바깥으로 이동 -> 무시해야 함, 출력도 x




주사위 놓은 곳 좌표, 이동 명령어 주어지면, -> 주사위 상단 값을 출력
'''



N, M, x, y, K= map(int,input().split())

board=[list(map(int,input().split())) for _ in range(N)]

moves=list(map(int,input().split()))


directions=[(0,1),(0,-1),(-1,0),(1,0)]


dice=[[0,2,0],
      [4,1,3],
      [0,5,0],
      [0,6,0]]


def roll_dice(direction):
    global dice

    new_dice=[[0]*3 for _ in range(4)]

    if direction==1: # 동쪽
        new_dice[0][1]=dice[0][1]

        new_dice[1][0]=dice[3][1]
        new_dice[1][1]=dice[1][0]
        new_dice[1][2]=dice[1][1]

        new_dice[2][1]=dice[2][1]

        new_dice[3][1]=dice[1][2]


    elif direction==2: #서쪽
        new_dice[0][1] = dice[0][1]

        new_dice[1][0] = dice[1][1]
        new_dice[1][1] = dice[1][2]
        new_dice[1][2] = dice[3][1]

        new_dice[2][1] = dice[2][1]

        new_dice[3][1] = dice[1][0]

    elif direction==3: #북쪽
        new_dice[0][1] = dice[1][1]

        new_dice[1][0] = dice[1][0]
        new_dice[1][1] = dice[2][1]
        new_dice[1][2] = dice[1][2]

        new_dice[2][1] = dice[3][1]

        new_dice[3][1] = dice[0][1]


    elif direction==4: #남쪽
        new_dice[0][1] = dice[3][1]

        new_dice[1][0] = dice[1][0]
        new_dice[1][1] = dice[0][1]
        new_dice[1][2] = dice[1][2]

        new_dice[2][1] = dice[1][1]

        new_dice[3][1] = dice[2][1]


    dice=new_dice




#주사위 굴리기

for move in moves:
    dn=directions[move-1][0]
    dm=directions[move-1][1]

    if 0<=x+dn<N and 0<=y+dm<M:
        # 주사위 이동
        x=x+dn
        y=y+dm

        #주사위 굴리기
        roll_dice(move)

        print(dice[1][1])

        if board[x][y]==0:
            board[x][y]=dice[3][1]
        else:
            dice[3][1]=board[x][y]
            board[x][y]=0

    # 이동 범위가 지도 밖이면
    else:
        continue


