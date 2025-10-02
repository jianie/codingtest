def solution(s):
    total_len = len(s)
    answer = total_len

    for tmp_len in range(total_len // 2, 0, -1):
        tmp_answer = total_len
        i = 0
        while i < total_len:
            char = s[i:i+tmp_len]

            count = 1
            while char == s[i + tmp_len*count:i + tmp_len*(count+1)]:
                count += 1

            if count > 1:
                tmp_answer = tmp_answer - tmp_len * (count - 1) + len(str(count))
                
            i += tmp_len * count

        if tmp_answer < answer:
            answer = tmp_answer

    return answer


