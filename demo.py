varia="h e l l o".split(" ")
li=[]
for i in varia:
    if i not in li:
        li.append(i)
    else:
        print(i)
    print(varia.count(i))