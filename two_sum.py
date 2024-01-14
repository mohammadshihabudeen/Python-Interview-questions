li=[12,13,7,1,32,3,4]
target=8
nums=[]
i=0
for number in li:
    diff=target-number
    if diff in nums:
        print(diff,number)
    nums+=(number)
    i+=1