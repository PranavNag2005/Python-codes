r=int(input("enter the rows size "))
c=int(input("enter the columns size "))
matrix=[]
for i in range(r):
    matrix.append([int(input("enter elements in to matrix ")) for j in range(c)])
for i in matrix:
    print(i)
n=len(matrix)
b=[[matrix[n-j-1][i] for j in range(len(matrix))]for i in range(len(matrix[0]))]
print(b)