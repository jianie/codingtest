def solution(n):
    answer = []
    
    while (n) :
        tmp = n % 3
        if ( tmp == 0) :
            tmp = 4
            n -= 1
        answer.append(str(tmp))
        n //= 3    
        
    answer.reverse()
    return ''.join(answer)