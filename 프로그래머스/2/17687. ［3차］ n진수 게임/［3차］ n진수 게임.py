def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
def solution(n, t, m, p):
    num_str = ""
    ret = ""
    for i in range(t**2):
        num_str += convert(i, n)
    for idx, j in enumerate(num_str):
        if t == len(ret):
            return ret
        if idx % m == p - 1:
            ret += j
    return ret