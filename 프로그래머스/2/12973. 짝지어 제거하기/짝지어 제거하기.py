from collections import deque

def solution(s):
    stack = deque()
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # 중복 제거(짝 지어 제거)
        else:
            stack.append(char)
    return 1 if not stack else 0
