from collections import deque

def solution(n, wires):
    answer = float('inf')
    
    # wires의 각 전선을 하나씩 끊어봄
    for cut_a, cut_b in wires:
        graph = [[] for _ in range(n + 1)]
        
        # 끊은 전선 제외하고 그래프 만들기
        for a, b in wires:
            if (a == cut_a and b == cut_b) or (a == cut_b and b == cut_a):
                continue
            graph[a].append(b)
            graph[b].append(a)
        
        # BFS로 한 쪽 전력망 크기 세기
        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True
        count = 1
        
        while queue:
            now = queue.popleft()
            for nxt in graph[now]:
                if not visited[nxt]:
                    visited[nxt] = True
                    queue.append(nxt)
                    count += 1
        
        # 나머지 전력망 크기 = n - count
        diff = abs(count - (n - count))
        answer = min(answer, diff)
    
    return answer