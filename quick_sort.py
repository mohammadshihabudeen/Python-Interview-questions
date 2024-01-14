def sorting(arr):
    if len(arr)<=1:
        return arr
    pivot,smaller,larger,array=arr[0],[],[],[]
    array[:]=arr[1:]
    for elemnt in array:
        if elemnt <=pivot:
            smaller.append(elemnt)
        else:
            larger.append(elemnt)
    return sorting(smaller)+[pivot]+sorting(larger)
print(sorting([7,2,3,1,5,4,5]))
