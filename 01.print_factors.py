inp=input("Enter a number:")
def strtoint(no):
    n=0
    for ele in no:
        n*=10
        temp=ord(ele)-48
        n+=temp
    return n
inp=strtoint(inp)
for x in range(1,inp//2+1):
    if inp%x==0:
        print(x)