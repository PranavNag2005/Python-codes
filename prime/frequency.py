a=input("enter")
dic={}
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
