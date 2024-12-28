s=input("enter the binary numbers ")
yes=False
for i in range(len(s)):
    if s[i]=='1' or s[i]=='0':
        yes=True
    else:
        yes=False

print(yes)