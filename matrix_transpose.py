b=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]#[[0 for _ in range(4)]for x in range(4)]
print(b)
a=[]
for _ in range(4):
    a.append(list(map(int,input().split())))
for i in range(4):
    for j in range(4):
        b[i][j]=a[j][i]
print("ans:")
for i in range(4):
    for j in range(4):
        print(b[i][j],end=" ")
    print()