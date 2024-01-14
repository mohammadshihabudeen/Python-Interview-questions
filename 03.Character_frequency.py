inp=input("Enter a String:")
dic={}
for x in inp:
    if x in dic:
        dic[x]+=1
    else:
        dic[x]=1
print(dic)