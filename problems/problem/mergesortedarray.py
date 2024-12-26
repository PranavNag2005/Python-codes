l1=[1,2,3,0,0,0]
l2=[2,5,6]
for i in range(0,len(l1)):
    if l1[i]==0:
        l1.pop()
print(l1)