def solution(record):
    answer = []
    
    '''
    닉네임 변경 두가지
    1. 채팅방 내에서 change로 바꾸는 경우
    2. 나갔다가 들어오면서 바꾸는 경우 
    '''
    
    name_dict=dict() # userid:name 형태
    
    # 최종 이름 dict 만들기
    for log in record:
        if log[0]=='L':
            action,userid=log.split()
        else:
            action,userid,name =log.split()
        
        if action=='Enter' or action=='Change':
            name_dict[userid]=name
        
    # result 만들기
    
    for log in record:
        if log[0]=='L':
            action,userid=log.split()
        else:
            action,userid,name =log.split()
        
        if action=='Enter':
            answer.append(name_dict[userid]+'님이 들어왔습니다.')
            
        elif action=='Leave':
            answer.append(name_dict[userid]+'님이 나갔습니다.')
            
        
    
    
    return answer