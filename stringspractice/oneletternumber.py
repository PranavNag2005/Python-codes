s=input("enter the string with characters and numbers ")
alpha=False
digit=False
for i in s:
    if i.isalpha():
        alpha=True
    if i.isdigit():
        digit=True
if alpha==True and digit==True:
    print(True)
else:
    print(False)