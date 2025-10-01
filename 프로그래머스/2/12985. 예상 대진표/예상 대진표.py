def solution(n,a,b):
    answer = 1

    # 1 ~ N 번 배정받음
    
    # 1, 2 => 1    3,4 =>2
    
    while True:
        
        
        
        if a%2==0:
            a=a//2
        else:
            a=a+1
            a=a//2
            
        if b%2==0:
            b=b//2
        else:
            b=b+1
            b=b//2
            
        if a==b:
            break
        
        answer+=1
            
            
        

    return answer