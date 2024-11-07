n=int(input("enter the number of rows "))
c=int(input("enter the number of columns "))
for i in range(n):
    for j in range(c):
        if(i==0 or i==n-1 or j==c-1 or j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()