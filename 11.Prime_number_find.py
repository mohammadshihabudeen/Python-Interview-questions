inp=int(input("Enter a number:"))
prime=True
for x in range(2,int(inp**0.5)+1):
    if inp%x==0:
        prime=False
        break
if prime:
    print("Prime number!")
else:
    print("Not a Prime number!")

