a=[]
s=int(input("enter the size of the array "))
for i in range(s):
    a.append(int(input("enter the numbers ")))
print(a)
for i in range(1,s+2):
    if i not in a:
        print(i)