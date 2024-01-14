arr=[4, 3, 7, 8, 6, 2, 1]
arr.sort()
print(arr)
for i in range(1,len(arr)-1,2):
    arr[i],arr[i+1]=arr[i+1],arr[i]
print(arr)