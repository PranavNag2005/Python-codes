n=int(input("enter the no of rows "))
c=1
for i in range(1,n):
    for j in range(n-1-i):
        print(c,end=" ")
    for k in range(i):
        print(i,end=" ")
    print()

# output:
# 1 1 1 1 1 1 
# 1 1 1 1 2 2
# 1 1 1 3 3 3
# 1 1 4 4 4 4
# 1 5 5 5 5 5
# 6 6 6 6 6 6