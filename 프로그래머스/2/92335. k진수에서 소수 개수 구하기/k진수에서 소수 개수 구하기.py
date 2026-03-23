
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def to_base(n, k):
    result = ''
    while n > 0:
        result = str(n % k) + result
        n //= k
    return result

                   
def solution(n, k):
    answer = 0
    n_k=to_base(n,k) # k진수로 바꾸기
    
    n_list=n_k.split("0")
    
    for num in n_list:
        if num != '' and is_prime(int(num)):
            answer+=1
                   
            
    return answer
                   
                   
                   
        
                