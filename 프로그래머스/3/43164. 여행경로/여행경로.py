from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    # 그래프 구성
    for a, b in tickets:
        graph[a].append(b)
    
    # 도착지 알파벳 순 정렬
    for key in graph:
        graph[key].sort()
    
    route = []
    N = len(tickets)
    answer = []

    def dfs(airport):
        # 경로에 현재 공항 추가
        route.append(airport)
        
        # 모든 티켓 사용완료 → 정답 저장
        if len(route) == N + 1:
            answer.extend(route)
            return True  # 경로 완성
        
        if airport in graph:
            for idx, next_airport in enumerate(graph[airport]):
                if graph[airport][idx] is None:  # 이미 사용된 티켓 건너뛰기
                    continue
                # 티켓 사용
                dest = graph[airport][idx]
                graph[airport][idx] = None
                if dfs(dest):  # 다음 공항에서 탐색
                    return True  # 정답 찾았으면 바로 종료
                # 복구 (백트래킹)
                graph[airport][idx] = dest
        
        route.pop()
        return False
    
    dfs("ICN")
    return answer
