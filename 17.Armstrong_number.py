inp=input("Enter a number:")
arm=0
n=len(inp)
for no in inp:
    arm+=int(no)**n
if arm==int(inp):
    print("Armstrong Number!")
else:
    print("Not an Armstrong Number!")

