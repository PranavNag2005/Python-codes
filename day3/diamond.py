n=int(input())
width = 2 * n - 1  
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(n):
 
    for j in range(i):
        print(' ', end=' ') 

    for j in range(width - 2 * i):
        print('*', end=' ')  
    print()

