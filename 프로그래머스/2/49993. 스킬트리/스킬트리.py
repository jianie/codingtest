from collections import deque

def solution(skill, skill_trees):
    answer = len(skill_trees)
    
    '''
    가능한 스킬트리 개수를 리턴
    '''
    
    
    
    for tree in skill_trees:
        
        queue=deque(skill)
        
        for char in tree:
            if char in skill:
                if char==queue[0]:
                    queue.popleft()
                    
                else:
                    answer-=1
                    break
                
        
    
    
    return answer