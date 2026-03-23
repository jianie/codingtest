def solution(m, musicinfos):
    answer = '(None)'
    
    def convert(s):
        return s.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace('B#','b').replace('E#','e')
    
    
    melody_list=[]
    m = convert(m)
    
    for idx,song in enumerate(musicinfos):
        start,finish,name,melody=song.split(',')
        start_h,start_m=start.split(':')
        finish_h,finish_m=finish.split(':')
        
        time = (int(finish_h) * 60 + int(finish_m)) - (int(start_h) * 60 + int(start_m))
        melody = convert(melody)
        
        num=time//len(melody)
        plus=time%len(melody)
        
        
        real_melody=melody*num+melody[:plus]
        
        melody_list.append((time,idx,name,real_melody))
        
    melody_list.sort(key=lambda x: (x[0],-x[1]),reverse=True)
    
    for song in melody_list:
        if m in song[3]:
            answer=song[2]
            return answer
    
    return  answer
        
    
    
