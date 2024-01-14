n, k = list(map(int,input().split()))
l=list(map(int,input().split()))
l1=[]
l1[:]=l
li=[]
i=0
while max(l)>0:
    if i>n-1:
        i=0
    if l[i]>0:
        l[i]-=k
        li.append(i)
    i+=1
print(li)
print(li[-1]+1)


