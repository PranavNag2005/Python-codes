s=int(input("enter the number "))
count=0
if s==0:
    count=1
else:

    while s>0:
        count+=1
        s=s//10
print(count)