r=int(input("enter rows: "))
c=int(input("enter columns: "))
m1=[]
m2=[]
print("enter elements into the m1 matrix")
for i in range(r):
    m1.append([int(input(f"enter element m1[{i}{j}]:"))for j in range(c)])
print("enter elements into the m1 matrix")
for i in range(r):
    m2.append([int(input(f"enter element m2[{i}{j}]:"))for j in range(c)])
result=[[m1[i][j]+m2[i][j] for j in range(c)]for i in range(r)]
print("addition of matrix")
for row in result:
    print(row)