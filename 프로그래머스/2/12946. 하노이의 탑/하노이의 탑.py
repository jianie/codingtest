def solution(n):
    answer = []
    
    def hanoi(n, start, end, mid):
        if n == 1:
            answer.append([start, end])
            return
        
        hanoi(n - 1, start, mid, end)   # 위 n-1개를 보조기둥으로
        answer.append([start, end])     # 가장 큰 원판 이동
        hanoi(n - 1, mid, end, start)   # 보조기둥의 n-1개를 목적지로
    
    hanoi(n, 1, 3, 2)
    return answer