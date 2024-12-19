n=int(input("ent6er anumnber"))
c=0
for i in range(1,n):
    if n%i==0:
        c+=1
    if n%i!=i:
        c+=1
print(c)
if c==2:
    print("prime number")
else:
    print("not a prime number")


