def solution(sequence, k):
    left = 0
    current_sum = 0
    answer = []
    min_length = float('inf')
    
    for right in range(len(sequence)):
        current_sum += sequence[right]
        
        while current_sum > k:
            current_sum -= sequence[left]
            left += 1
        
        if current_sum == k:
            if right - left < min_length:
                min_length = right - left
                answer = [left, right]
    
    return answer

'''시간초과
def solution(sequence, k):
    answer = []
    # 합이 k인것중 짧은 수열, 앞쪽 나오는 수열
    
    for num in range(1,len(sequence)+1): #부분 수열의 개수가 될수 있는건 1부터 수열총길이
        for i in range(0,len(sequence)-num+1): # 부분 수열 시작 지점
            
            list_sum=sum(sequence[i:i+num])
            if list_sum==k:
                return [i,i+num-1]
            
        
    return answer
'''

