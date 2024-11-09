import math
n=int(input("no"))
c=0

for j in range(1,int(math.sqrt(n))+1):
    if n%j==0:
        c+=1
        if n//j!=1:
            c=c+1
if c==2:
    print("prime no")
else:
    print("not a prime")