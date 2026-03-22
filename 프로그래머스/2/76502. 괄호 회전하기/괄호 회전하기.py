from collections import deque

def solution(s):
    answer = 0
    queue = deque(s)
    
    for i in range(len(s)):
        if i > 0:
            a = queue.popleft()
            queue.append(a)
        
        temp = deque(queue)
        check = []
        valid = True
        
        while temp:
            symbol = temp.popleft()
            
            if symbol in '([{':
                check.append(symbol)
            else:
                if not check:
                    valid = False
                    break
                
                top = check[-1]
                
                if symbol == ')' and top == '(':
                    check.pop()
                elif symbol == ']' and top == '[':
                    check.pop()
                elif symbol == '}' and top == '{':
                    check.pop()
                else:
                    valid = False
                    break
                    
        if valid and len(check) == 0:
            answer += 1
    
    return answer