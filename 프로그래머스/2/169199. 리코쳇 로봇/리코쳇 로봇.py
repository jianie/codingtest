from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    
    # 시작 위치 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
    
    queue = deque()
    queue.append((start[0], start[1], 0))
    
    visited = [[False]*m for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    while queue:
        x, y, cnt = queue.popleft()
        
        # 목표 도착
        if board[x][y] == 'G':
            return cnt
        
        for dx, dy in directions:
            nx, ny = x, y
            
            # 👉 여기 핵심: 끝까지 미끄러짐
            while True:
                tx = nx + dx
                ty = ny + dy
                
                if not (0 <= tx < n and 0 <= ty < m):
                    break
                if board[tx][ty] == 'D':
                    break
                
                nx, ny = tx, ty
            
            # 방문 안 했으면
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt+1))
    
    return -1