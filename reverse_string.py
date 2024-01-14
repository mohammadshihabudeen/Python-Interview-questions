name="mohammad"
def strtolist(s):
    li=[]
    for char in s:
        li+=[char]
    return li
name=strtolist(name)
left=0
right=len(name)-1
def listtostr(li):
    st=""
    for char in li:
        st+=char
    return st
while left<right:
    name[left],name[right]=name[right],name[left]
    left+=1
    right-=1
print(listtostr(name))


