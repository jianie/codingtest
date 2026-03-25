
N=int(input())

time=list(map(int,input().split()))

time.sort()


answer=0
for i in range(N):
    answer+=sum(time[:i+1])

print(answer)