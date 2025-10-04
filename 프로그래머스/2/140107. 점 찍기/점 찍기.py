import math

def solution(k, d):
    answer = 0
    x = 0
    while x <= d:
        max_y = int(math.sqrt(d*d - x*x))
        answer += (max_y // k) + 1
        x += k
    return answer
