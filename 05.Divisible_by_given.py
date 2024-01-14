def strtoint(no):
    n=0
    for ele in no:
        temp=ord(ele)-48
        n=n*10+temp
    return n
u_number=strtoint(input("Enter a number:"))
rang=strtoint(input("Enter the range:"))
for x in range(0,rang+1,u_number):
    print(x)
