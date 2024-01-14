dic={"a":0,"e":0,"i":0,"o":0,"u":0}
inp=input("Enter the String:")
for char in inp:
    if char in dic.keys():
        dic[char]+=1
print(dic)