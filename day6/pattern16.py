n=int(input("rows "))
for i in range(1,n+1):
    num=i
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+n-j
    print()

# output:
# 1
# 2 6
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15