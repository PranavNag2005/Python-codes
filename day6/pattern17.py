n=int(input("rows "))
c=64
for i in range(n):
    for j in range(i):
        print(chr(c+i),end=" ")
        
    print()


# output:

# A 
# B B 
# C C C 
# D D D D 
# E E E E E 