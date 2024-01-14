def strtoint(no):
    n=0
    for ele in no:
        n*=10
        temp=ord(ele)-48
        n+=temp
    return n
inp=strtoint(input("Enter a number:"))
fact=1
for x in range(1,inp+1):
    fact=fact*x
print("Factorial is:",fact)
