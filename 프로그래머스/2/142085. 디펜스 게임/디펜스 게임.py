import heapq

def solution(n, k, enemy):
    answer = 0
    '''
    병사 n 명
    매 라운드마다 enemy[i]마리의 적 등장
    
    남은 병사수보다 현재 라운드 적의 수가 더 많으면 게임 종료
    
    무적권 스킬 ( 최대 k번): 병사 소모 없이 한 라운드의 공격 막음
    
    무적권 스킬을 
    '''
    
    heap=[] # 무적권 스킬 쓸 라운드의 적 수
    remain_soldier=n
    
    for round in range(len(enemy)):
        if len(heap)<k: # 무적권 스킬 아직 남았으면
            heapq.heappush(heap,enemy[round])
            
            answer+=1 #라운드 증가
            
        else: #무적권 스킬 다 썼으면  
            min_round_enemy=heapq.heappop(heap) # 힙에서 꺼내서 비교 
            
            if enemy[round]>=min_round_enemy: # 이번 라운드 적 수가, 힙 안의 최소 적 수 보다 크면 
                heapq.heappush(heap,enemy[round])
                
                remain_soldier-=min_round_enemy
                
                if remain_soldier<0:
                    break
                
                    
                
            else: #원래대로 되돌리기, 이번라운드에선 병사 감소
                heapq.heappush(heap,min_round_enemy)
                
                remain_soldier-=enemy[round]
                
                if remain_soldier<0:
                    break
                
                
                
            answer+=1 #라운드 증가
                
    
    
    return answer