# r=int(input("enter rows: "))
# c=int(input("enter columns: "))
# m1=[]
# m2=[]
# print("enter elements into the m1 matrix")
# for i in range(r):
#     m1.append([int(input(f"enter element m1[{i}{j}]:"))for j in range(c)])
# print("enter elements into the m1 matrix")
# for i in range(r):
#     m2.append([int(input(f"enter element m2[{i}{j}]:"))for j in range(c)])
# result=[[m1[j][i]*m2[j][i] for j in range(c)]for i in range(r)]
# print("multiplication of matrix")
# for row in result:
#     print(row)


a=[[1,2],[3,4],[5,6]]
b=[[7,8],[9,0]]
result=[[sum(a[i][k]*b[k][j]for k in range(len(b))for j in range(len(b[0])))]for i in range(len(a))]
print("matrix multiply")
for r in result:
    print(r)