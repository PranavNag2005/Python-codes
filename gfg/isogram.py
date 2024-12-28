s=input("enter the string ")
dici={}
for i in s:
    if i not in dici:
        dici[i]=1
    else:
        dici[i]+=1
yes=False
for key,value in dici.items():
    if max(dici.values())==1:
        yes=True
    else:
        yes=False
print(yes)