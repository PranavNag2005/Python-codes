
n=int(input("enter the no of rows"))
width = 2 * n - 1  
for i in range(n):
 
    for j in range(i):
        print(' ', end=' ') 

    for j in range(width - 2 * i):
        print('*', end=' ')  
    print()