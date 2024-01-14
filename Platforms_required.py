arr = [100, 300, 500]
dep = [900, 400, 600]
ma=0
c=0
for i in range(len(arr)):
    for j in range(i+1,len(dep)+1):
        if dep[i]>arr[j]:
            c