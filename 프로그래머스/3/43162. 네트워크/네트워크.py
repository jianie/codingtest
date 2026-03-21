def dfs(node, computers, visited):
    visited[node] = True
    for neighbor, connected in enumerate(computers[node]):
        if connected == 1 and not visited[neighbor]:
            dfs(neighbor, computers, visited)

def solution(n, computers):
    visited = [False] * n
    network_count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited)
            network_count += 1
    return network_count