s=input()
list=[]
list1=[]
for i in range(len(s)):
    if s[i] not in list and s[i].islower():
        list.append(s[i])
    else:
        list1.append(s[i])
print(len(list))

