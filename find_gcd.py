li=[45,323]
gcd=1
for ele in range(min(li),1,-1):
    if li[0]%ele==0 and li[1]%ele==0:
        gcd=ele
lcm=int((li[0]*li[1])/gcd)
print(gcd,lcm)