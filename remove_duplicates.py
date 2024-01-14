inp=[1,2,3,4,2,4,6]
ans=[]
for input_element in inp:
    flag=True
    for ans_element in ans:
        if ans_element==input_element:
            flag=False
            break
    if flag:
        ans.append(input_element)
print(ans)