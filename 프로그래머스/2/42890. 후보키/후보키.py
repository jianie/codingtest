from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    only_key = 0
    not_only_key = []
    candidate_keys = []

    for c in range(col):
        tmp = set()
        for r in range(row):
            tmp.add(relation[r][c])

        if len(tmp) != row:
            not_only_key.append(c)
        else:
            only_key += 1
            candidate_keys.append((c,))  # 후보키 저장

    for i in range(2, len(not_only_key) + 1):
        new_combi = list(combinations(not_only_key, i))

        for combi in new_combi:
            tmp = set()

            for r in range(row):
                tmp_tuple = []
                for key in range(i):
                    tmp_tuple.append(relation[r][combi[key]])
                tmp.add(tuple(tmp_tuple))

            if len(tmp) == row:
                # 최소성 검사: 기존 후보키가 combi의 부분집합인지 확인
                is_minimal = True
                for key in candidate_keys:
                    if set(key).issubset(set(combi)):
                        is_minimal = False
                        break
                if is_minimal:
                    only_key += 1
                    candidate_keys.append(combi)

    return only_key
