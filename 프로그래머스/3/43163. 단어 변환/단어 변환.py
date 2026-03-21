from collections import deque

def is_connected(word1, word2):
    # 두 단어가 한 글자만 다르면 True
    diff = 0
    for a, b in zip(word1, word2):
        if a != b:
            diff += 1
        if diff > 1:
            return False
    return diff == 1

def solution(begin, target, words):
    if target not in words:
        return 0  # target이 words에 없으면 변환 불가능
    
    visited = set()
    queue = deque()
    queue.append((begin, 0))  # (현재 단어, 변환 횟수)
    
    while queue:
        current, steps = queue.popleft()
        
        if current == target:
            return steps
        
        for w in words:
            if w not in visited and is_connected(current, w):
                visited.add(w)
                queue.append((w, steps + 1))
    
    return 0  # 변환 불가능한 경우
