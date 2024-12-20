r=int(input("enter the no of rows "))
c=int(input("Enter the no of columns "))
A=[]
for i in range(r):
    A.append([int(input(f"enter values A{i}{j}")) for j in range(c)])
print(A)

B=[]
for i in range(r):
    B.append([int(input(f"enter values B{i}{j}")) for j in range(c)])
print(B)

C =[[0 for j in range(c)] for i in range(r)]
for i in range(r):
    for j in range(c):
        C[i][j]=A[i][j]+B[i][j]
print(C)