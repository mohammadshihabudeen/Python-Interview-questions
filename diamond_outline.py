n=5
for i in range(n):
    for x in range(n-i):
          print(end=" ")
    for j in range(i):
        if j==0 or j==i-1:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
for i in range(n):
    for x in range(i):
          print(end=" ")
    for j in range(n-i):
        if j==0 or j==n-i-1:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
