'''
N개의 수로 이루어진 순열,
N-1개의 연산자 : + - x /

나눗셈은 정수나눗셈: 몫만
음수를 양수로 나눌때는: 양수로 바꾼뒤 , 몫을 음수로 바꿈



식 최대인것, 최소인것 구하기


'''

num=int(input())

number=list(map(int,input().split()))

add,sub,multi,divi=map(int,input().split())


answer_max=-1e9
answer_min=1e9

def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a, b):
    if a * b < 0:  # 두 값의 곱이 음수이면 부호 반전 처리
        return - (abs(a) // abs(b))
    else:
        return a // b



def dfs(idx, total, add, sub, multi, divi):
    global answer_max, answer_min
    if idx == num - 1:
        if total < answer_min:
            answer_min = total
        if total > answer_max:
            answer_max = total
        return

    if add > 0:
        dfs(idx+1, addition(total, number[idx+1]), add-1, sub, multi, divi)
    if sub > 0:
        dfs(idx+1, subtraction(total, number[idx+1]), add, sub-1, multi, divi)
    if multi > 0:
        dfs(idx+1, multiplication(total, number[idx+1]), add, sub, multi-1, divi)
    if divi > 0:
        dfs(idx+1, division(total, number[idx+1]), add, sub, multi, divi-1)

dfs(0, number[0], add, sub, multi, divi)



print(int(answer_max))
print(int(answer_min))
