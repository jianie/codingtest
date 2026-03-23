def solution(n):
    arr = [[0] * n for _ in range(n)]
    
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:      # 아래
                x += 1
            elif i % 3 == 1:    # 오른쪽
                y += 1
            else:               # 왼쪽 위 대각선
                x -= 1
                y -= 1
            
            arr[x][y] = num
            num += 1
    
    answer = []
    for i in range(n):
        for j in range(i + 1):
            answer.append(arr[i][j])
    
    return answer