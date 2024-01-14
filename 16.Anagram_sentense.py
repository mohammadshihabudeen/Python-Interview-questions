s=input("Enter the first word:").lower()
t=input("Enter the second word:").lower()
def sort(arr):
    arr=list(arr)
    if len(arr)<=1:
        return arr
    pivot,smaller,larger=arr[0],[],[]
    arr[:]=arr[1:]
    for ele in arr:
        if ele<=pivot:
            smaller.append(ele)
        else:
            larger.append(ele)
    return sort(smaller)+[pivot]+sort(larger)
if sort(s) == sort(t):
    print("anagram")
else:
    print("Not a anagram")