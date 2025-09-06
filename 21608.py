N= int(input())


students=[]
for _ in range(N**2):
   students.append(list(map(int, input().split())))


#빈자리 배열 초기화
seats=[ [0]*N for i in range(N)]




# 상하좌우 델타
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 학생 별 좋아하는 친구 딕셔너리로 저장 (빠른 탐색 목적)
fav_dict = {}
for s in students:
   fav_dict[s[0]] = s[1:]




#학생 앉히기
for s in range(N**2):
   num=students[s][0] #지금 앉힐 학생 정보
   likes=fav_dict[num] # 지금 앉힐 학생이 좋아하는 친구


   candidates = [[0] * N for i in range(N)] # 좋아하는 친구 인접 칸 수
   empty_count = [[0] * N for _ in range(N)]  # 인접 빈 칸 수


   for i in range(N):
       for j in range(N):
           if seats[i][j] !=0: # 이미 자리 있음
               continue


           like_friends=0
           empties=0


           #해당 자리의 상하좌우 인접 칸 검사
           for d in range(4):
               nx,ny=i+dx[d],j+dy[d]


               if 0<=nx<N and 0<=ny<N:
                   if seats[nx][ny] in likes:
                       like_friends+=1


                   if seats[ny][ny]==0:
                       empties+=1


           # 해당 자리의 like friends, empites 점수
           candidates[i][j] = like_friends
           empty_count[i][j] = empties


   ## 1 if cadidate에서 max값을 자리로
   max_like=max(max(row) for row in candidates)
   like_positions=[(i,j) for i in range(N) for j in range(N) if candidates[i][j]==max_like]


   ##2 max값이 여러개면, 주변에 0인 칸 많은 칸으로 자리 정함
   max_empty=-1


   best_positions=[]


   for x,y in like_positions:
       if empty_count[x][y] > max_empty:
           best_positions=[(x,y)]
           max_empty=empty_count[x][y]
       elif empty_count[x][y] == max_empty:
           best_positions.append((x,y))






   ### 3 2를 만족하는 칸도 여러개면, 행의번호, 열의번호가 가장 작은 순으로
   # 행, 열 번호가 가장 작은 순으로 선택
   best_positions.sort()
   seat_x, seat_y = best_positions[0]
   seats[seat_x][seat_y] = num


# 만족도 구하기
# 만족도 점수 계산 함수
def satisfaction_score(x, y):
   student_num = seats[x][y]
   likes = fav_dict[student_num]
   count = 0
   for d in range(4):
       nx, ny = x + dx[d], y + dy[d]
       if 0 <= nx < N and 0 <= ny < N:
           if seats[nx][ny] in likes:
               count += 1
   if count == 0:
       return 0
   return 10 ** (count - 1)  # 1->1점, 2->10점, 3->100점, 4->1000점


# 전체 만족도 합산
total_satisfaction = 0
for i in range(N):
   for j in range(N):
       total_satisfaction += satisfaction_score(i, j)


print(total_satisfaction)