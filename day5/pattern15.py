n=int(input("enter the no of rows "))
c=1
for i in range(1,n):
    for j in range(n-1-i):
        print(i,end=" ")
    for k in range(i):
        print(c,end=" ")
    print()

# output:
# 1 1 1 1 1 
# 2 2 2 1 1 
# 3 3 1 1 1 
# 4 1 1 1 1 
# 1 1 1 1 1 