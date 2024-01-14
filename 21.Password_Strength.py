s_alpha="abcdefghijklmnopqrstuvwxyz"
c_alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
spl="!#$%&'\"()*+,-./:;<=>?@[\]^_`{|}~"
is_s_alpha=is_c_alpha=is_num=is_spl=False
inp=input("Enter Password:")
for char in inp:
    if char in s_alpha:
        is_s_alpha=True
    elif char in c_alpha:
        is_c_alpha=True
    elif char in num:
        is_num=True
    elif char in spl:
        is_spl=True
if any([is_c_alpha,is_s_alpha,is_num,is_spl]):
    print("Strong password!")
else:
    print("Weak password!")
