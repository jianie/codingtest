
N=int(input())

meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 끝나는 시간 우선, 같으면 시작 시간 우선
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)