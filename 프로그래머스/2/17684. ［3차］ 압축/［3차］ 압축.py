def solution(msg):
    answer = []
    
    '''
    dictionary={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    '''
    # dictionary 이렇게 선언하면 더 쉬움
    dictionary = {chr(i+64): i for i in range(1, 27)}
    idx = 27
    i = 0
    while i < len(msg):
        w = msg[i]
        j = i + 1
        while j <= len(msg) and msg[i:j] in dictionary:
            w = msg[i:j]
            j += 1
        answer.append(dictionary[w])
        if j <= len(msg):
            dictionary[msg[i:j]] = idx
            idx += 1
        i += len(w)
    return answer