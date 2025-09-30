def solution(n):
    answer = 0
    next_num=n
    
    while True:
        next_num+=1
        
        if bin(n).count('1')==bin(next_num).count('1'):
            return next_num
        
        
