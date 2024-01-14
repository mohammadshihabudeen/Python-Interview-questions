n=int(input("Enter the range:"))+1
prime=[True for x in range(n)]
p=2
while(p*p<=n):
    if prime[p]:
        for x in range(p*p,n,p):
            prime[x]=False
    p+=1
for no in range(n):
    if prime[no]:
        print(no) 