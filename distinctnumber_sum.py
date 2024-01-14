n=5
li=[n]
for x in range(1,n//2 if(n%2==0)else n//2+1):
    li.append(x)
    if len(li)==n:
        break
    if x>0:
        print(-x)
        li.append(-x)
if len(li)<n:
    li.insert(0,0) 
print(li)