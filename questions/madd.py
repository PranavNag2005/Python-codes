# r=[[1,2,3],[4,5,6],[7,8,9]]
# n=[[3,2,1],[6,5,4],[9,8,7]]
# c=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(r)):
#     for j in range(len(r[0])):
#         c[i][j]=r[i][j]*n[i][j]
# print(c)

r=int(input("enter the rows "))
c=int(input("enter the columns "))
a=[]
b=[]
print("enter the first matrix")
for i in range(r):
    a.append([int(input(f"enter the first matrix a{i}{j}")) for j in range(c)])
print("enter the second matrix")
for i in range(r):
    b.append([int(input(f"enter the second matrix b{i}{j}")) for j in range(c)])
res=[[a[i][j]*b[i][j] for j in range(c)]for i in range(r)]
print(res)