n=int(input("rows "))
c=64
for i in range(n):
    for j in range(1,i):
        print(chr(c+j),end=" ")
        
    print()

# output
# A
# A B
# A B C
# A B C D
# A B C D E
