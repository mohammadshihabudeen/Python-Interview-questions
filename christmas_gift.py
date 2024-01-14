names=["Alice", "Bob", "Charlie", "David", "Eve"]
n=len(names)
f_gift="David"
s_gift="Bob"
diff=names.index(s_gift)-names.index(f_gift)
if diff>0:
    print("clockwise") 
else:
    names[:]=reversed(names)
print(diff)
choks={}
i=names.index(f_gift)
while len(choks)<n:
    if i>=n:
        i-=n
    curr=names[i]
    print(i)
    if curr not in choks.keys():
        choks[curr]=1
    else:
        choks[curr]+=1
    i+=abs(diff)
print(choks)


