n=int(input("enter the number of rows "))
c=int(input("enter the number of columns "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()