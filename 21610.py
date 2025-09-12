'''




하늘에 비구름 만들기

각 칸에 바구니,

바구니 채울수 있는 물의 양에는 제한이 없다


비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름
구름에 이동을 M번 명령

i번째 이동 병령 : 방향 d, 거리 s

1. 구름 이동
2. 이동한 칸에 비가 내려 물 +1
3. 구름 사라짐
4. 2에서 물이 증가한 칸에 대해 => 대각선에 물이 있는 바구니 수만큼, 바구니의 물 양 증가
5. 물 2 이상인 모든 칸에 구름 생기고, 물의 양 -2 : 3에서 사라진 칸 제외


'''


N,M=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(N)]

#cloud NxN 격자로 만들지 말고 이렇게 위치만 튜플로 저장 => 시간초과때문
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]


move=[]

for _ in range(M):
    d,s=map(int,input().split())
    move.append((d,s))


directions=[(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

diagonal=[(-1,-1),(-1,1),(1,-1),(1,1)]



for m in range(M):

    m_dir_num=move[m][0]
    m_dir=directions[m_dir_num-1]

    m_dis=move[m][1]

    dr=m_dir[0]* m_dis
    dc=m_dir[1]*m_dis



    #### 시간 초과로 인해 water copy를 집합으로 변경
    ###water_copy=[] #물복사 마법 시전할 위치
    water_copy = set()
    ##new_cloud = [[0] * N for _ in range(N)]  # 이동 후 구름 임시 저장소

    #구름 이동
    for i,j in cloud:

                d_i=(i+dr)%N    #이동한 위치
                d_j=(j+dc)%N

                ##new_cloud[d_i][d_j] = 1   # 1. 구름 이동
                ###cloud[i][j]=0

                board[d_i][d_j]+=1 # 2. 물의 양 증가
                water_copy.add((d_i,d_j))


    ###cloud = [[0] * N for _ in range(N)] # 구름 모두 사라짐

    #물복사 마법
    for r,c in water_copy:
        count=0
        for d_r,d_c in diagonal:
            if 0<=r+d_r<N and 0<=c+d_c<N:
                if board[r + d_r][c + d_c] >=1:
                    count+=1
        board[r][c]+=count

    cloud = []
    #물 2 이상인 모든 칸에 구름 생기고, 물의 양 -2
    for r in range(N):
        for c in range(N):
            if board[r][c]>=2 and (r,c) not in water_copy:
                cloud.append((r, c))
                board[r][c]-=2







answer=0
# 정답 구하기
for i in range(N):
    for j in range(N):
        answer+=board[i][j]


print(answer)



