def solution(s):
    answer = ''
    
    
    data=list(map(int,s.split()))
    
    data.sort()
    
    
    return str(min(data))+' '+str(max(data))