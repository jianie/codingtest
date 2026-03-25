

K=int(input())


num=[]

for i in range(K):
    newnum=int(input())

    if newnum==0:
        num.pop()
    else:
        num.append(newnum)

print(sum(num))
