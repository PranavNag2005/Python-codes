n=int(input("enter the no of rows "))
c=1
for i in range(n):
    for j in range(n-i-1):
        print(c,end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

# output:
# 1 1 1 1 
# 1 1 1 *
# 1 1 * *
# 1 * * *
# * * * *