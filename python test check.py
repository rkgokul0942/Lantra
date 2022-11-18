a= input("Enter a word------   ")# Getting a input
b = {}#creating an empty dictionary
c=[]


for i in a:
    if i in b:
       b[i]+=1#if index in dictionaary increment 1

    else:
        b[i]=1#if index not in add 1


print(b)#printing the dictionary



# for j in b:
#     print(max(b,b))