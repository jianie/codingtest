from collections import deque
import heapq
import sys
input=sys.stdin.readline

lecture=[]
N=int(input())



for i in range(N):
    start,end=map(int,input().split())
    lecture.append((start,end))

lecture.sort(key=lambda x:(x[0],x[1]))


heap=[]
heapq.heappush(heap,lecture[0][1])
room=1

for lec in lecture[1:]:
    if heap[0]<=lec[0]:
        heapq.heappop(heap)

    heapq.heappush(heap,lec[1])








print(len(heap))
