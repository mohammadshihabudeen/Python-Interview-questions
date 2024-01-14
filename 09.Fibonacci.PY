def strtoint(no):
    n=0
    for ele in no:
        n*=10
        temp=ord(ele)-48
        n+=temp
    return n
inp=strtoint(input("Enter a number:"))
fno=0
sno=1
print(f"{0}\n{1}")
for _ in range(inp):
    temp=fno+sno
    print(temp)
    fno=sno
    sno=temp

    