def solution(n, lost, reserve):
    answer = 0
    #앞이나 뒷번호 학생에게만 체육복 빌려줌
    
    # lost = 도난당한 사람
    # reserve = 여분 체육복 있는 사람
    
    # 여벌 가져온 사람이 도난당했으면 자기가 가져온거 씀
    
    lost.sort()
    reserve.sort()
    

    
    lost2=set(lost)-set(reserve) ### 여벌 가져온 사람이 도난당했으면 자기가 가져온거 씀
    reserve2=set(reserve)-set(lost)
    
    answer=n-len(lost2)
    
    for i in lost2:
        if i-1 in reserve2:
            answer+=1
            reserve2.remove(i-1)
            continue
        elif i+1 in reserve2:
            answer+=1
            reserve2.remove(i+1)
            continue
        
    
    
    
    return answer