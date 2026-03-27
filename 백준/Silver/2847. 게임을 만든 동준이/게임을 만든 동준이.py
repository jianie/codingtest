from collections import deque


N=int(input())
levels=[]

for i in range(N):
    levels.append(int(input()))


answer=0
current_num=levels[-1]

for i in range(N-2,-1,-1):
    if levels[i]>=current_num:
        decrease=levels[i]-current_num+1
        answer+=decrease
        current_num=current_num-1

    else:
        current_num=levels[i]

print(answer)