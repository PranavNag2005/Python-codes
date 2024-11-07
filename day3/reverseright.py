n=int(input("enter the number of rows "))
c=int(input("enter the number of columns "))
for i in range(n):
    for j in range(c-i):
        print("*",end=" ")
    print()