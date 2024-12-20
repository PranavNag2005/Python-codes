s=input("enter the sentences ")
a=s.split(" ")
b=""
for i in a:
    b+=i[0].upper()+i[1:-1].lower()+i[-1].upper()+" "
print(b)