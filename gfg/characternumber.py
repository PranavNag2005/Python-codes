s=input("enter the startcharacter ")

end=input("enter the end character ")
dici={}
for i in range(ord(s),ord(end)+1):
    if i not in dici:
        dici[i]=chr(i)
print(dici)
for key,value in dici.items():
    print(f"{value} {key}")
