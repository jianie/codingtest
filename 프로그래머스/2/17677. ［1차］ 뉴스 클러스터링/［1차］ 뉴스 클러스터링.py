from collections import Counter

def solution(str1, str2):
    answer = 0    
    '''
    자카드 유사도
    A,B 모두 공집합이면 나눗셈 정의 x, 1임
    
    '''
    
    str1_list=Counter()
    str2_list=Counter()
    
    i=0
    
    while i <= len(str1) - 2:
        if str1[i].isalpha() and str1[i+1].isalpha():
            pair = str1[i].upper() + str1[i+1].upper()
            str1_list[pair] += 1  # append 대신 카운트 증가
        i += 1

    i = 0  # i 초기화 꼭 해줘야함

    while i <= len(str2) - 2:
        if str2[i].isalpha() and str2[i+1].isalpha():
            pair = str2[i].upper() + str2[i+1].upper()
            str2_list[pair] += 1
        i += 1
        
    
    tmp=str1_list-str2_list
    intersect=str1_list-tmp
    
    union=str1_list+str2_list
    
    for i in union:
        if i in intersect:
            union[i]=max(str1_list[i],str2_list[i])
            
    
    
    
    all_union=0
    for i,j in union.items():
        all_union+=j
        
    all_intersect=0
    for i,j in intersect.items():
        all_intersect+=j
        
        
    if all_intersect==0 and all_union==0:
        answer=int((1)*65536)
    else:
        answer=int((all_intersect/all_union)*65536)
        
        
    
    
    return answer