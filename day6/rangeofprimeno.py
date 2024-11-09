x=int(input("enter the first no "))
y=int(input("enter the second no "))
for i in range(x,y):
    c=0
    for j in range(2,i):
        if i%j==0:
            c+=1
    if c==0:
        print(i)