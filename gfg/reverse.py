s=input("enter any string ")
a=""
for i in range(len(s)-1,-1,-1):
    a+=s[i]
print(a)