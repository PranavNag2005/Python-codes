
s=int(input("enter the number "))
count=0
if s==0:
    count=1
else:

    while s>0:
        count+=1
        s=s//10
print(count)

import math
n=int(input("ënter the no "))
# print(int(math.log10(n)+1))
# s=str(n)
# print(len(s))