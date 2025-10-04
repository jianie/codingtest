def solution(elements):
    n = len(elements)
    result = set()
    elements = elements * 2  # 원형 효과

    for size in range(1, n+1):    # 부분 수열 길이
        for start in range(n):    # 시작 인덱스
            result.add(sum(elements[start:start+size]))
    return len(result)
