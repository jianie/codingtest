# 상어에는 1 이상 M이하 자연수 번호
# 1 번호가 가장 강력
# NxN 크기의 격자 중 M개의 칸에 상어 들어있음
#상어들은 1초마다 상하좌우 이동
# 냄새는 상어가 k번 이동하면 사라짐




# 상어의 이동: 인접한 칸 중 아무 냄새가 없는 칸, 가능한 칸이 여러개면 우선순위 따름


n,m,k= map(int,input().split())


data=[]

# 처음 상어 위치
for _ in range(n):
    data.append(list(map(int,input().split())))

# 상어 초기 방향
directions=list(map(int,input().split()))


#상어의 방향 별 우선순위 받아오기

properties=[]
for i in range(m):
    temp=[]

    for _ in range(4):
        temp.append(list(map(int,input().split())))
    properties.append(temp)




