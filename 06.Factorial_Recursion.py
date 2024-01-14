def strtoint(no):
    n=0
    for ele in no:
        n*=10
        temp=ord(ele)-48
        n+=temp
    return n
def factorial(num):
    if num<=1:
        return 1
    else:
        return num*factorial(num-1)
inp=strtoint(input("Enter a number:"))
print(factorial(inp))