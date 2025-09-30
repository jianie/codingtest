'''
단품 메뉴를 조합해서 코스요리 형태로 재구성



최소 2명 손님에게서 주문된 단품 조합을 후보로

코스요리는 최소 2가지 이상의 단품메뉴 
'''

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for k in course:  # 코스 메뉴 길이 하나씩 순회
        candidates = []
        
        for menu_li in orders:  # 각 손님 주문 메뉴별로
            # 메뉴를 알파벳 정렬하고 길이 k인 조합을 구함
            for comb in combinations(sorted(menu_li), k):
                candidates.append(''.join(comb))  # 조합을 문자열로 저장
        
        # 각 조합별 빈도 계산
        sorted_candidates = Counter(candidates).most_common()
        
        # 빈도가 2 이상이고, 최빈값과 같은 조합만 answer에 추가
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    
    # 결과 알파벳 순 정렬하여 반환
    return sorted(answer)
