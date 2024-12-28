s=input("enter a string ")
sub=input("enter a substring ")
istrue=False
for i in range(len(sub)):
    if sub[i] in s:
        istrue=True
    else:
        istrue=False
sa=-1
for i in range(len(s)):
    if sub[0]==s[i]:
        sa=i
print(istrue,sa)