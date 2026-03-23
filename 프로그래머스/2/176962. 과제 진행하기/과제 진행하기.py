from collections import deque

def solution(plans):
    answer = []
    
    todo=[]
    stop_list=[]
    
    for plan in plans:
        
        h,m=plan[1].split(':')
        start=int(h)*60+int(m)

        todo.append((plan[0],start, int(plan[2])))  # 과목명, 시작시간, 소요 시간
        
    todo.sort(key=lambda x: x[1]) # start시간 기준으로 정렬
    
    queue=deque(todo)
    
    while queue:
            
        name,start,time=queue.popleft()
        if queue and queue[0][1]< start+time: # 현재 꺼낸 과목 끝나는 것보다 다음 과목 시작시간 더 빠르면
            stop_list.append([name, time - (queue[0][1] - start)]) # 과목명, 남은 시간
        else:
            answer.append(name)
            
            if queue:
            
                left_time=queue[0][1] - (start+time)
                while left_time > 0 and stop_list:
                    if stop_list[-1][1] <= left_time:
                        left_time -= stop_list[-1][1]
                        answer.append(stop_list[-1][0])
                        stop_list.pop()
                    else:
                        stop_list[-1][1] -= left_time
                        left_time = 0
                
                
    while stop_list:
        answer.append(stop_list.pop()[0])
    
    
    return answer