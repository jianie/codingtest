N = int(input())
top = list(map(int, input().split()))

stack = []   # (인덱스, 높이)
answer = []

for i in range(N):
    while stack and stack[-1][1] < top[i]:
        stack.pop()

    if stack:
        answer.append(stack[-1][0] + 1)   # 1번부터 시작하니까 +1
    else:
        answer.append(0)

    stack.append((i, top[i]))

print(*answer)