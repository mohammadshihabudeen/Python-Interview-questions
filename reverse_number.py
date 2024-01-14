no=9677867497
ans=0
while(no):
    tmp=no%10
    ans=(ans*10)+tmp
    no=no//10
print(ans)