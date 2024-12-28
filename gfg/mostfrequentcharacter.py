s=input("Enter the characters or stirngs ")
dici={}
maxvalue=float("-inf")
maxkey=None
for i in s:
    if i not in dici:
        dici[i]=1
    else:
        dici[i]+=1
print(dici)
for key,value in dici.items():
    if value>maxvalue:
        maxvalue=value
        maxkey=key
    elif value == maxvalue:
        if maxkey is None or key < maxkey:
            maxkey = key  # Update to the lexicographically smaller character
print(maxkey,maxvalue)