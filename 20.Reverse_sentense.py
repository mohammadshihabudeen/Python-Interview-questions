# print(" ".join((list(input("Enter the sentense:").split()))[::-1]))
s="hi hello welcome"
def split(s):
    word=""
    result=[]
    for char in s:
        if char==" ":
            result.append(word)
            word=""
        else:
            word+=char
    result.append(word)
    return result
def reverse(s):
    l=0
    r=len(s)-1
    if l<r:
        s[l],s[r]=s[r],s[l]
        l,r=l+1,r-1
    return s
def listtostr(s):
    li=""
    for char in s:
        li+=(char)+" "
    return li
print(listtostr(reverse(split(s))))