n=int(input("enter the no of rows "))
for i in range(n):
    for j in range(i):
        print(i,end=" ")
    print()

# output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5