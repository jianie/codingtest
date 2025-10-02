def solution(m, n, board):
    answer = 0
    
    #아래, 대각선, 오른쪽
    dx=[1,1,0]
    dy=[0,1,1]
    
    
    '''
    for i in range(m):
        board[i]=list(board[i])
    '''
    board = [list(row) for row in board] # 이렇게 하는게 더 낫다
        
        
    
    
    while True:
        
        visited=[[0]*n for _ in range(m)]
    
        for i in range(m):
            for j in range(n):

                character=board[i][j]
                
                if character == 0:
                    continue

                for dir in range(3):
                    nx=i+dx[dir]
                    ny=j+dy[dir]
                    
                    if nx<0 or nx>=m or ny<0 or ny>=n:
                        break

                    if board[nx][ny]!=character:
                        break

                else:
                    visited[i][j]=1
                    for dir in range(3):
                        nx=i+dx[dir]
                        ny=j+dy[dir]
                        visited[nx][ny]=1
                        
        rem_num=0                
        # 1 표시된것들(4개 캐릭터같은것) 보드에서 0으로 표시하기
        for i in range(m):
            for j in range(n):
                if visited[i][j]==1:
                    
                    rem_num+=1
                    board[i][j]=0
                    
        if rem_num==0:
            return answer
        else:
            answer+=rem_num
            
        # 지워진 것들 아래로 내리기 
        for j in range(n):
            empty_row = m - 1  # 아래에서부터 채울 위치 초기화
            for i in range(m - 1, -1, -1):
                if board[i][j] != 0:  # 0이 아니면 아래에서부터 채울 위치에 복사
                    board[empty_row][j] = board[i][j]
                    if empty_row != i:
                        board[i][j] = 0
                    empty_row -= 1
            # 빈 칸이 나머지 위로 남아있으면 0으로 채우기
            for k in range(empty_row, -1, -1):
                board[k][j] = 0
                
                
            
    
    return answer