def solution(citations):
    # 1. 내림차순 정렬
    citations.sort(reverse=True)
    
    # 2. 인덱스(i)와 인용수(citation)를 비교
    for i, citation in enumerate(citations):
        # i + 1은 현재 확인 중인 논문의 개수입니다.
        if citation < i + 1:
            return i
            
    # 모든 논문의 인용 횟수가 전체 논문 개수보다 많은 경우
    return len(citations)