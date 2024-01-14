arr=[1, 20, 6, 4, 5]
n=len(arr)
c=0
for x in range(n):
    for y in range(x+1,n):
        if arr[x]>arr[y]:
            c+=1
print(c)