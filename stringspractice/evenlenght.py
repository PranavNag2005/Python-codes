s=input("enter the sentences ")
a=s.split(" ")
b=[]
for i in a:
    if len(i)%2==0:
        b.append(i+" ")
print(b)