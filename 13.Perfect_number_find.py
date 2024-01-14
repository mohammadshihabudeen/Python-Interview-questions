inp=int(input("Enter a number:"))
fact=0
for x in range(1,inp//2+1):
    if inp%x==0:
        fact+=x
if fact==inp:
    print("Perfect number!")
else:
    print("Not a perfect number")