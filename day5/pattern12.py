n=int(input("enter the no of rows "))
for i in range(n):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()

#output
# A
# B B
# C C C
# D D D D