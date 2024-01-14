print(ord("A"),ord("Z"),ord("a"),ord("z"))
str="HeLLo"
ans=''
for ele in str:
    char=ord(ele)
    if char<91:
        ans+=chr(ord(ele)+32)
    else:
        ans+=chr(ord(ele)-32)
print(ans)
