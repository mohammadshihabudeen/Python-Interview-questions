ran=int(input("Enter the range:"))
for inp in range(ran):
    arm=0
    for no in str(inp):
        arm+=int(no)**len(str(inp))
    if arm==int(inp):
        print(arm)
