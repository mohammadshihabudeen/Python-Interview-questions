import math
inp=int(input("Enter the range:"))
for y in range(2,inp+1):
    prime=True
    for x in range(2,int(math.sqrt(y))+1):
        if y%x==0:
            prime=False
    if prime:
        print(y)