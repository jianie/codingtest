'''

오늘부터 N+1일 째 되는날 퇴사, 남은 N일동안 최대한 많은 상담

상담 시간 T, 금액 P



'''



n=int(input())


arr=[]

for _ in range(n):
    t,p= map(int, input().split())
    arr.append([t,p])      # [ 상담 시간, 금액 ]  형태




# dp로 뒤에서부터 풀어야 함


dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if i + arr[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(arr[i][1] + dp[i + arr[i][0]], dp[i+1])

print(dp[0])












