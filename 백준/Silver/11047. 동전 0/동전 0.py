


N,K=map(int,input().split())


coins=[]

for _ in range(N):
    coins.append(int(input()))


idx=len(coins)-1
answer=0
while idx>-1:
    a,b=K//coins[idx], K%coins[idx]
    if a>=1:
        answer+=a
        K=b

    idx-=1

print(answer)