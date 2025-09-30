import math

def solution(fees, records):
    times, fee, plus_times, plus_fee = map(int, fees)
    parking_lot = dict()
    total_times = dict()
    
    for record in records:
        clock, num, in_out = record.split()
        num = int(num)
        
        if in_out == 'IN':
            parking_lot[num] = clock
        else:
            in_clock = parking_lot.pop(num)
            in_hour, in_min = map(int, in_clock.split(':'))
            out_hour, out_min = map(int, clock.split(':'))
            duration = (out_hour * 60 + out_min) - (in_hour * 60 + in_min)
            
            total_times[num] = total_times.get(num, 0) + duration
    
    # 출차 기록 없는 차량 23:59까지 주차시간 누적
    for num, in_clock in parking_lot.items():
        in_hour, in_min = map(int, in_clock.split(':'))
        duration = (23 * 60 + 59) - (in_hour * 60 + in_min)
        total_times[num] = total_times.get(num, 0) + duration
    
    answer = []
    for num in sorted(total_times.keys()):
        total = total_times[num]
        if total <= times:
            total_fee = fee
        else:
            total_fee = fee + math.ceil((total - times) / plus_times) * plus_fee
        answer.append(total_fee)
    
    return answer
