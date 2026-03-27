from collections import deque


answer=1
for i in range(3):
    new_num=int(input())
    answer=answer*new_num



for i in range(10):
    print(str(answer).count(str(i)))