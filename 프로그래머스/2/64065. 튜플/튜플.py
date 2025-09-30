from collections import Counter
def solution(s):
    answer = []
    
    """    
    중복원소 x인 튜플을 표현하는 집합
    """
    all=[]
    
    tmp=[]
    
    for i in s:
        if i.isdigit():
            tmp.append(i)
            
        else:
            if tmp:
                all.append(int(''.join(tmp)))
            tmp=[]
            
    num=Counter(all)
    
    sorted_items = sorted(num.items(), key=lambda x: x[1], reverse=True)
    
    for i in sorted_items:
        answer.append(i[0])
            
    
    return answer