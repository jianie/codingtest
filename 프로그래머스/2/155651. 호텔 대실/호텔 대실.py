from collections import deque

def solution(book_time):
    book = []
    room_status = []
    max_room = 0
    
    for start, finish in book_time:
        sh, sm = map(int, start.split(":"))
        fh, fm = map(int, finish.split(":"))
        
        start_time = sh * 60 + sm
        finish_time = fh * 60 + fm + 10
        
        book.append((start_time, finish_time))
    
    book.sort(key=lambda x: (x[0], x[1]))
    book_queue = deque(book)
    
    while book_queue:
        start, finish = book_queue.popleft()
        
        # 현재 시작 시간까지 끝난 방 제거
        new_room_status = []
        for end_time in room_status:
            if end_time > start:
                new_room_status.append(end_time)
        
        room_status = new_room_status
        
        # 현재 예약 추가
        room_status.append(finish)
        
        max_room = max(max_room, len(room_status))
    
    return max_room