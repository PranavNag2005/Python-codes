n=int(input("enter the no of rows "))
for i in range(n):
    for j in range(1,n-i):
        print(j,end=" ")
    print()

# output:

# 1 2 3 4 5 6 7 8 9 
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1