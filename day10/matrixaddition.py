a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
results=[[0,0,0],[0,0,0],[0,0,0]]
rows=len(a)
columns=len(a[0])
print(columns)
print(a)
print(b)
for i in range(rows):
    for j in range(columns):
        results[i][j]=a[i][j]+b[i][j]
print(results)