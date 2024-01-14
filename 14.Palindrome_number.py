inp=int(input("Enter a number:"))
def reverse(no):
    n=0
    while no:
        temp=no%10
        n=n*10+temp
        no=no//10
    return n
if (inp==reverse(inp)):
    print("Palindrome number!")
else:
    print("Not palindrome number!")