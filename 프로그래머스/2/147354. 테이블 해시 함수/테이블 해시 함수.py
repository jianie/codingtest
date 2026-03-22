def solution(data, col, row_begin, row_end):
    answer = 0
    '''첫번째 컬럼= 세로줄 은 기본키, 모든 튜플에 대해 중복 x
    
    해시함수: col 컬럼 기준으로 오름차순, 만약 동일하면 기본키 기준 내림차순
    
    모든 s_i구해서 더하기 : row_begin~row_end인 모든 행에 대한 값들을 i로 나눈 나머지 합, 
    
    행마다 s_i다 구하고, 구한 s_i다 더하기
    '''
    
    data.sort(key=lambda x:(x[col-1],-x[0]))
    
    total_si=0
    for i in range(row_begin-1,row_end):
        si=0
        for j in range(len(data[0])):
            si+=data[i][j]%(i+1)
        total_si^=si
    
        
    
    return total_si



