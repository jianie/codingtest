def solution(dirs):
    answer = 0
    '''처음 걸어본 길의 길이 구하기,
    좌표평면 넘어가는 명령어는 무시
    '''
    
    x_pos=0
    y_pos=0
    nx=0
    ny=0
    
    direction={'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    
    
    visited=set()
    
    for move in dirs:
        dx,dy=direction[move]
        
        nx=x_pos+dx
        ny=y_pos+dy
        
        if nx>5 or nx<-5 or ny>5 or ny<-5:
            
            continue
            
      
        
        if (nx,ny,x_pos,y_pos) not in visited and (x_pos,y_pos,nx,ny) not in visited:
            visited.add((nx,ny,x_pos,y_pos))
            visited.add((x_pos,y_pos,nx,ny))
            answer+=1
            
        x_pos=nx
        y_pos=ny
            
        
            

    
    
    return answer