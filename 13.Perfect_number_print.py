inp=int(input("Enter thr range:"))
for y in range(1,inp):
    fact=0
    for x in range(1,y//2+1):
        if y%x==0:
            fact+=x
    if(y==fact):
        print(y)
