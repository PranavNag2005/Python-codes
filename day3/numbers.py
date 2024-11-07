n=int(input("enter the number of rows "))
c=int(input("enter the number of columns "))
ans=1
for i in range(1,n):
    for j in range(1,i):
        print(ans,end=" ")
        ans+=1
    print()