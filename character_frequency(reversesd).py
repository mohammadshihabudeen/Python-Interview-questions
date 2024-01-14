word="mohammad"
count={}
for char in word:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
def max(li):
    m=0
    for char in li:
        if char>m:
            m=char
    return m
li={}
while count:
    for key,value in count.items():
        if max(count.values())==value:
            li[key]=value
            count.pop(key)
            break
print(li)